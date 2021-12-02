from read_calls_db_artifact.CellNameIdReader import CellNameIdReader
from read_calls_db_artifact.JoinNWriter import JoinNWriter
import os
import re
import json


def read_files_directory_keep_history(bdusr, bdpass, dbhost, dbport, dbservice, input_db_artifact_dir, out_directory, history_dir):

    cell_name_reader = CellNameIdReader(bdusr, bdpass, dbhost, dbport, dbservice)
    cell_id_V_name = cell_name_reader.get_cell_name()

    try:
        with open(os.path.join(history_dir, "history.json")) as history_input:
            input_files_history = json.load(history_input)
    except FileNotFoundError:
        input_files_history = dict()

    for key in input_files_history.keys():
        input_files_history[key]=set(input_files_history[key])

    input_file_patt = re.compile(".*.gz")
    for cur_dir, dirs, files in os.walk(input_db_artifact_dir):
        for file in files:
            if input_file_patt.search(file):
                try:
                    files_set = input_files_history[cur_dir]
                except KeyError:
                    input_files_history[cur_dir]={file}
                    # Process the file
                    file_path = os.path.join(cur_dir, file)
                    print("Processing file = {}".format(file_path))
                    join_n_writer_object_per_file = JoinNWriter(file_path, cell_id_V_name,
                                                                out_directory)
                    join_n_writer_object_per_file.print_updated_content_on_console()
                else:
                    if file not in files_set:
                        input_files_history[cur_dir].add(file)
                        # Process the file
                        file_path = os.path.join(cur_dir, file)
                        print("Processing file = {}".format(file_path))
                        join_n_writer_object_per_file = JoinNWriter(file_path, cell_id_V_name,
                                                                    out_directory)
                        join_n_writer_object_per_file.print_updated_content_on_console()

    for dir_path in input_files_history.keys():
        input_files_history[dir_path]=list(input_files_history[dir_path])
    with open(os.path.join(history_dir, "history.json"), 'w') as history:
        json.dump(input_files_history, history)



