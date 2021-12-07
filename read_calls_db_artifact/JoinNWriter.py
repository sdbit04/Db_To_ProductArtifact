from read_calls_db_artifact.ReadCallsDbArtifact import CallsDbArtReader
import pdb
import csv
import os


class JoinNWriter(object):
    """
    This class need the object cell_id_vs_name_dict, which we can create once while we connect to DB,
    and use for all objects created for each input-files
    Then it join the input-file with DB output, and write into a file
    """

    def __init__(self, input_file_path, cell_id_vs_name_dict, out_directory):
        self.input_file_path = input_file_path
        self.input_file_name = os.path.basename(self.input_file_path).rstrip('.gz')
        self.out_dir = out_directory
        self.calls_db_artifact_reader = CallsDbArtReader(self.input_file_path)
        self.cell_id_vs_cell_name = cell_id_vs_name_dict

    def populate_cell_name(self):
        updated_content_of_file = dict()
        selected_columns_of_file = self.calls_db_artifact_reader.read_calls_db_artifact()
        cell_id_vs_name = self.cell_id_vs_cell_name

        for row_id, row_items in selected_columns_of_file.items():
            # pdb.set_trace()
            try:
                cell_id = row_items[2]
            except IndexError:
                # Then this row is value less, go to next dont process any other field of this row
                continue
            else:
                if cell_id == '' or cell_id is None:
                    continue
                else:
                    try:
                        cell_id = int(cell_id)
                        cell_p_name = cell_id_vs_name[cell_id]
                    except ValueError:
                        print("Obtained Cell_ID is not an integer")
                        # pdb.set_trace()

                    except (KeyError):
                        print("Cell_ID {} doesn't present into Mentor_DB".format(cell_id))
                        # pdb.set_trace()
                        # Then this row is value less
                        # No need to check for next item of this row, but as cell_id=row_items[2] didnt get exception
                        # it is going to next item of the row, which is not needed.
                        # So taking it to next line only.
                        continue
                    else:
                        row_items[2] = cell_p_name
                        #############################333
                        try:
                            cell_id = row_items[5]
                        except IndexError:
                            # Then this row is done, no more fields into input row, dont process any other field of this row, go to nex row
                            updated_content_of_file[row_id]=row_items
                            # pdb.set_trace()
                            continue
                        else:
                            if cell_id == '' or cell_id is None:
                                updated_content_of_file[row_id] = row_items
                                continue
                            else:
                                try:
                                    cell_id = int(cell_id)
                                    cell_p_name = cell_id_vs_name[cell_id]
                                except ValueError:
                                    pass
                                except (KeyError):
                                    print("Exception while reading cell from {}".format(self.input_file_path))
                                    continue
                                else:

                                    row_items[5] = cell_p_name
                                    ###################################
                                    try:
                                        cell_id = row_items[8]
                                    except IndexError:
                                        # Then this row, dont process any other field of this row, go to nex row
                                        updated_content_of_file[row_id] = row_items
                                        continue
                                    else:
                                        if cell_id == '' or cell_id is None:
                                            updated_content_of_file[row_id] = row_items
                                            continue
                                        else:
                                            try:
                                                cell_id = int(cell_id)
                                                cell_p_name = cell_id_vs_name[cell_id]
                                            except ValueError:
                                                pass
                                            except (KeyError):
                                                print("Cell_ID {} doesn't present into Mentor_DB".format(cell_id))
                                                continue
                                            else:

                                                row_items[8] = cell_p_name
                                                ###################################
                                                try:
                                                    cell_id = row_items[11]
                                                except (IndexError):
                                                    # Then this row, dont process any other field of this row, go to nex row
                                                    updated_content_of_file[row_id] = row_items
                                                    continue
                                                else:
                                                    if cell_id == '' or cell_id is None:
                                                        updated_content_of_file[row_id]=row_items
                                                        continue
                                                    else:
                                                        try:
                                                            cell_id = int(cell_id)
                                                            cell_p_name = cell_id_vs_name[cell_id]
                                                        except ValueError:
                                                            pass
                                                        except (KeyError):
                                                            print("Exception while reading cell from {}".format(
                                                                self.input_file_path))
                                                            continue
                                                        else:

                                                            row_items[11] = cell_p_name
                                                            ###################################
                                                            try:
                                                                cell_id = row_items[14]
                                                            except (IndexError):
                                                                # Then this row, dont process any other field of this row, go to nex row
                                                                updated_content_of_file[row_id] = row_items
                                                                continue
                                                            else:
                                                                if cell_id == '' or cell_id is None:
                                                                    updated_content_of_file[row_id] = row_items
                                                                    continue
                                                                else:
                                                                    try:
                                                                        cell_id = int(cell_id)
                                                                        cell_p_name = cell_id_vs_name[cell_id]
                                                                    except ValueError:
                                                                        pass
                                                                    except (KeyError):
                                                                        print(
                                                                            "Cell_ID {} doesn't present into Mentor_DB".format(cell_id))
                                                                        continue
                                                                    else:

                                                                        row_items[14] = cell_p_name
                                                                        ###################################
                                                                        try:
                                                                            cell_id = row_items[17]
                                                                        except (IndexError):
                                                                            # Then this row, dont process any other field of this row, go to nex row
                                                                            updated_content_of_file[row_id] = row_items
                                                                            continue
                                                                        else:
                                                                            if cell_id == '' or cell_id is None:
                                                                                updated_content_of_file[
                                                                                    row_id] = row_items
                                                                                continue
                                                                            else:
                                                                                try:
                                                                                    cell_id = int(cell_id)
                                                                                    cell_p_name = cell_id_vs_name[cell_id]
                                                                                except ValueError:
                                                                                    pass
                                                                                except (KeyError):
                                                                                    print(
                                                                                        "Cell_ID {} doesn't present into Mentor_DB".format(cell_id))
                                                                                    continue
                                                                                else:

                                                                                    row_items[17] = cell_p_name
                                                                                    ###################################
                                                                                    try:
                                                                                        cell_id = row_items[20]
                                                                                    except (IndexError):
                                                                                        # Then this row, dont process any other field of this row, go to nex row
                                                                                        updated_content_of_file[row_id] = row_items
                                                                                        continue
                                                                                    else:
                                                                                        if cell_id == '' or cell_id is None:
                                                                                            updated_content_of_file[
                                                                                                row_id] = row_items
                                                                                            continue
                                                                                        else:
                                                                                            try:
                                                                                                cell_id = int(cell_id)
                                                                                                cell_p_name = cell_id_vs_name[cell_id]
                                                                                            except ValueError:
                                                                                                pass
                                                                                            except (KeyError):
                                                                                                print(
                                                                                                    "Cell_ID {} doesn't present into Mentor_DB".format(cell_id))
                                                                                                continue
                                                                                            else:

                                                                                                row_items[20] = cell_p_name
                                                                                                ###################################
                                                                                                try:
                                                                                                    cell_id = row_items[23]
                                                                                                except IndexError:
                                                                                                    # Then this row, dont process any other field of this row, go to nex row
                                                                                                    updated_content_of_file[row_id] = row_items
                                                                                                    continue
                                                                                                else:
                                                                                                    if cell_id == '' or cell_id is None:
                                                                                                        updated_content_of_file[
                                                                                                            row_id] = row_items
                                                                                                        continue
                                                                                                    else:
                                                                                                        try:
                                                                                                            cell_id = int(cell_id)
                                                                                                            cell_p_name = cell_id_vs_name[cell_id]
                                                                                                        except ValueError:
                                                                                                            pass
                                                                                                        except (KeyError):
                                                                                                            print("Cell_ID {} doesn't present into Mentor_DB".format(cell_id))
                                                                                                            continue
                                                                                                        else:

                                                                                                            row_items[23] = cell_p_name
                                                                                                            ###################################
                                                                                                            try:
                                                                                                                cell_id = row_items[26]
                                                                                                            except (IndexError):
                                                                                                                # Then this row, dont process any other field of this row, go to nex row
                                                                                                                updated_content_of_file[row_id] = row_items
                                                                                                                continue
                                                                                                            else:
                                                                                                                if cell_id == '' or cell_id is None:
                                                                                                                    updated_content_of_file[
                                                                                                                        row_id] = row_items
                                                                                                                    continue
                                                                                                                else:
                                                                                                                    try:
                                                                                                                        cell_id = int(cell_id)
                                                                                                                        cell_p_name = cell_id_vs_name[cell_id]
                                                                                                                    except ValueError:
                                                                                                                        pass
                                                                                                                    except (KeyError):
                                                                                                                        print("Cell_ID {} doesn't present into Mentor_DB".format(cell_id))
                                                                                                                        continue
                                                                                                                    else:

                                                                                                                        row_items[26] = cell_p_name
                                                                                                                        ###################################
                                                                                                                        try:
                                                                                                                            cell_id = row_items[29]
                                                                                                                        except (IndexError):
                                                                                                                            # Then this row, dont process any other field of this row, go to nex row
                                                                                                                            updated_content_of_file[
                                                                                                                                row_id] = row_items
                                                                                                                            continue
                                                                                                                        else:
                                                                                                                            if cell_id == '' or cell_id is None:
                                                                                                                                updated_content_of_file[
                                                                                                                                    row_id] = row_items
                                                                                                                                continue
                                                                                                                            else:
                                                                                                                                try:
                                                                                                                                    cell_id = int(cell_id)
                                                                                                                                    cell_p_name = cell_id_vs_name[cell_id]
                                                                                                                                except ValueError:
                                                                                                                                    pass
                                                                                                                                except (KeyError):
                                                                                                                                    print("Cell_ID {} doesn't present into Mentor_DB".format(cell_id))
                                                                                                                                    continue
                                                                                                                                else:
                                                                                                                                    row_items[29] = cell_p_name
                                                                                                                                    updated_content_of_file[row_id]=row_items
        else:
            return updated_content_of_file

    def print_updated_content_on_console(self):
        updated_content = self.populate_cell_name()
        # pdb.set_trace()
        # print("Number of rows in file = {}".format(len(updated_content.keys())))
        if len(updated_content.keys()) !=0:
            out_file_path = os.path.join(self.out_dir, self.input_file_name)
            with open(out_file_path, 'w', newline='') as out_file:

                field_names = ['Long','Lat','Cell_P','RSRQ_P','RSCP_P','CellID_1','RSRQ_1','RSCP_1','CellID_2','RSRQ_2','RSCP_2','CellID_3','RSRQ_3','RSCP_3','CellID_4','RSRQ_4','RSCP_4','CellID_4','RSRQ_4','RSCP_4','CellID_5','RSRQ_5','RSCP_5','CellID_6','RSRQ_6','RSCP_6','CellID_7','RSRQ_7','RSCP_7','CellID_8','RSRQ_8','RSCP_8','CellID_9','RSRQ_9','RSCP_9']
                writer = csv.writer(out_file, delimiter='|')
                writer.writerow(field_names)
                for row_ind, row in updated_content.items():
                    writer.writerow(row)


