from read_calls_db_artifact.CellNameIdReader import CellNameIdReader
from read_calls_db_artifact.JoinNWriter import JoinNWriter
import os
import re
import json
import datetime
import pdb


def read_files_directory_keep_history(bdusr, bdpass, dbhost, dbport, dbservice, input_db_artifact_dir, out_directory, history_dir, history_days, ne_id_list, back_days_min, back_days_max):
    cell_name_reader = CellNameIdReader(bdusr, bdpass, dbhost, dbport, dbservice)
    cell_id_V_name = cell_name_reader.get_cell_name()

    """Read and manage history """
    try:
        with open(os.path.join(history_dir, "history.json")) as history_input:
            input_files_history = json.load(history_input)
    except FileNotFoundError:
        input_files_history = dict()
    history_day = int(history_days)
    key_patt_to_keep = []
    remove_list = set()
    for day in range(history_day):
        key_patt_to_keep.append(re.compile((datetime.datetime.today() - datetime.timedelta(days=day)).strftime("%Y%m%d")))

    for key in input_files_history.keys():
        for date_patt in key_patt_to_keep:
            if date_patt.search(key):
                input_files_history[key] = set(input_files_history[key])
                break
            else:
                continue
        else:
            print("Dir {} to be removed from history".format(key))
            try:
                remove_list.add(key)
            except KeyError:
                raise
    for del_key in remove_list:
        input_files_history.pop(del_key)

    """Create set of dates and NE we want to process """
    intended_dates_YYYYMMDD = set()
    for day in range(back_days_min, back_days_max+1):
        pdb.set_trace()
        intended_dates_YYYYMMDD.add((datetime.datetime.today() - datetime.timedelta(days=day)).strftime("%Y%m%d"))
    intended_ne_id = set(ne_id_list)

    """This has support to read only .gz as archive input"""
    input_file_patt = re.compile(".*.gz")
    dir_date_patt = re.compile("(2\d{7})")
    ne_id_patt = re.compile("2\d+_(\d+)$")
    for cur_dir, dirs, files in os.walk(input_db_artifact_dir):
        pdb.set_trace()
        cur_dir_base = os.path.basename(cur_dir)
        try:
            cur_dir_date = dir_date_patt.search(cur_dir_base).group(1)
            cur_dir_ne_id = ne_id_patt.search(cur_dir_base).group(1)

        except AttributeError:
            continue
        else:
            if cur_dir_date not in intended_dates_YYYYMMDD or cur_dir_ne_id not in intended_ne_id:
                continue
            else:
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
                            try:
                                join_n_writer_object_per_file.print_updated_content_on_console()
                            except Exception:
                                for dir_path in input_files_history.keys():
                                    input_files_history[dir_path] = list(input_files_history[dir_path])
                                with open(os.path.join(history_dir, "history.json"), 'w') as history:
                                    json.dump(input_files_history, history)
                                raise
                        else:
                            if file not in files_set:
                                input_files_history[cur_dir].add(file)
                                # Process the file
                                file_path = os.path.join(cur_dir, file)
                                print("Processing file = {}".format(file_path))
                                join_n_writer_object_per_file = JoinNWriter(file_path, cell_id_V_name,
                                                                            out_directory)
                                try:
                                    join_n_writer_object_per_file.print_updated_content_on_console()
                                except Exception:
                                    for dir_path in input_files_history.keys():
                                        input_files_history[dir_path] = list(input_files_history[dir_path])
                                    with open(os.path.join(history_dir, "history.json"), 'w') as history:
                                        json.dump(input_files_history, history)
                                    raise

    for dir_path in input_files_history.keys():
        input_files_history[dir_path]=list(input_files_history[dir_path])
    with open(os.path.join(history_dir, "history.json"), 'w') as history:
        json.dump(input_files_history, history)


if __name__ == "__main__":
    for i in range(1,4):
        print(i)
