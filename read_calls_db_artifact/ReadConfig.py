import re


def read_config_file(config_file_path):
    calls_db_archive_dir_pat =re.compile("calls_db_archive_dir=(.*)")
    out_dir_pat=re.compile("out_dir=(.*)")
    history_dir_pat=re.compile("history_dir=(.*)")
    history_days_pat=re.compile("keep_history_for_days=(.*)")
    back_days_max_pat = re.compile("back_days_max=(.*)")
    back_days_min_pat = re.compile("back_days_min=(.*)")
    ne_id_list_pat = re.compile("ne_id_list=(.*)")
    m_dbuser_pat = re.compile("mentor_db_user=(.*)")
    m_dbpass_pat = re.compile("mentor_db_pass=(.*)")
    m_dbhost_pat = re.compile("mentor_db_host=(.*)")
    m_dbservice_pat = re.compile("mentor_db_service=(.*)")
    config_dict= {}
    with open(config_file_path) as config_file:
        for line in config_file.readlines():
            if calls_db_archive_dir_pat.search(line):
                config_dict["calls_db_archive_dir"] = calls_db_archive_dir_pat.search(line).group(1)
            elif out_dir_pat.search(line):
                config_dict["out_dir"]=out_dir_pat.search(line).group(1)

            elif back_days_max_pat.search(line):
                try:
                    config_dict["back_days_max"] = int(back_days_max_pat.search(line).group(1))
                except ValueError:
                    print("Incorrect back_days_max")
            elif back_days_min_pat.search(line):
                try:
                    config_dict["back_days_min"] = int(back_days_min_pat.search(line).group(1))
                except ValueError:
                    print("Incorrect back_days_min")

            elif history_days_pat.search(line):
                try:
                    config_dict["history_days"] = int(history_days_pat.search(line).group(1))
                except ValueError:
                    print("Incorrect History days, or No history provided, will consider default 7")
            elif ne_id_list_pat.search(line):
                config_dict["ne_id_list"] = ne_id_list_pat.search(line).group(1).split(",")
            elif history_dir_pat.search(line):
                config_dict["history_dir"] = history_dir_pat.search(line).group(1)
            elif m_dbuser_pat.search(line):
                config_dict["m_dbuser"] = m_dbuser_pat.search(line).group(1)
            elif m_dbpass_pat.search(line):
                config_dict["m_dbpass"] = m_dbpass_pat.search(line).group(1)
            elif m_dbhost_pat.search(line):
                config_dict["m_dbhost"]=m_dbhost_pat.search(line).group(1)
            elif m_dbservice_pat.search(line):
                config_dict["m_dbservice"] = m_dbservice_pat.search(line).group(1)

    return config_dict

