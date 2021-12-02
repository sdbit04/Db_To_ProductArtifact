import csv
import json


def print_updated_content_on_console():
    updated_content = {1:['swapan', 'Sonai'], 2:['swapan','swarnali']}
    with open("Out_file", 'w', newline='') as out_file:
        field_names = []
        writer = csv.writer(out_file, delimiter='|')
        for row_ind, row in updated_content.items():
            writer.writerow(row)

# print_updated_content_on_console()

import os
import re


def read_files_directory_keep_history(input_db_artifact_dir, history_file):
    input_file_patt = re.compile(".*")
    # We have load history into input_file_history
    with open(history_file) as history_input:
        input_files_history = json.load(history_input)
    print("Length of history = {}".format(len(input_files_history.keys())))
    for key in input_files_history.keys():
        input_files_history[key]=set(input_files_history[key])
    print(input_files_history)
    for cur_dir, dirs, files in os.walk(input_db_artifact_dir):
        for file in files:
            if input_file_patt.search(file):
                try:
                    files_set = input_files_history[cur_dir]
                except KeyError:
                    input_files_history[cur_dir]={file}
                    # Process the file
                    file_path = os.path.join(cur_dir, file)
                    print(file_path)
                    # join_n_writer_object_per_file = JoinNWriter(file_path, cell_id_V_name,
                    #                                             out_directory)
                    # join_n_writer_object_per_file.print_updated_content_on_console()
                else:
                    if file not in files_set:
                        input_files_history[cur_dir].add(file)
                        # Process the file
                        file_path = os.path.join(cur_dir, file)
                        # join_n_writer_object_per_file = JoinNWriter(file_path, cell_id_V_name,
                        #                                             out_directory)
                        # join_n_writer_object_per_file.print_updated_content_on_console()
                        print(file_path)

    for dir_path in input_files_history.keys():
        input_files_history[dir_path]=list(input_files_history[dir_path])
    with open("history.json", 'w') as history:
        json.dump(input_files_history, history)

read_files_directory_keep_history("D:\\D_drive_BACKUP\\MENTOR\CWC", "D:\\D_drive_BACKUP\\study\\PycharmProjects\\CallsDbArtifact4Asset\\read_calls_db_artifact\\history.json")

