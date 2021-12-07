from read_calls_db_artifact.TraversInputDir import read_files_directory_keep_history
from read_calls_db_artifact.ReadConfig import read_config_file
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("Config_file_path")
    args = parser.parse_args()
    config_file_path = args.Config_file_path
    config_file_dict = read_config_file(config_file_path)
    # print(config_file_dict)
    m_dbuser=config_file_dict["m_dbuser"]
    m_dbpass=config_file_dict["m_dbpass"]
    m_dbhost = config_file_dict["m_dbhost"]
    m_dbservice=config_file_dict["m_dbservice"]
    input_dir = config_file_dict["calls_db_archive_dir"]
    out_dir = config_file_dict["out_dir"]
    history_dir = config_file_dict["history_dir"]
    back_days_min = config_file_dict["back_days_min"]
    back_days_max = config_file_dict["back_days_max"]
    if back_days_max < back_days_min:
        print("Back_day_max should be larger then back_day_min")
        raise ValueError
    ne_list = config_file_dict["ne_id_list"]
    try:
        history_days = config_file_dict["history_days"]
    except KeyError:
        history_days = 7
    read_files_directory_keep_history(dbhost=m_dbhost, bdusr=m_dbuser, bdpass=m_dbpass, dbport=1521, dbservice=m_dbservice, input_db_artifact_dir=input_dir, out_directory=out_dir, history_dir=history_dir, history_days=history_days, back_days_min=back_days_min, back_days_max=back_days_max, ne_id_list=ne_list)



