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
                cell_p_name = None
                if cell_id != '' and cell_id is not None:
                    try:
                        cell_id = int(cell_id)
                    except (ValueError, TypeError):
                        print("Exception while reading {}".format(self.input_file_path))
                        break
                    else:
                        cell_p_name = cell_id_vs_name[cell_id]
                        print(cell_p_name)
                else:
                    pass
            except KeyError:
                pass
                # print("Cell_id {0} missing in mentor-db".format(row_items[2]))
            else:
                row_items[2] = cell_p_name
            try:
                cell_id = row_items[5]
                cell_0_name = None
                if cell_id != '' and cell_id is not None:
                    try:
                        cell_id = int(cell_id)
                    except (ValueError, TypeError):
                        print("Exception while reading {}".format(self.input_file_path))
                        break
                    else:
                        cell_0_name = cell_id_vs_name[cell_id]
            except KeyError:
                pass
                # print("Cell_id_missing in mentor")
            else:
                row_items[5] = cell_0_name
            try:
                cell_id = row_items[8]
                cell_1_name = None
                if cell_id != '' and cell_id is not None:
                    try:
                        cell_id = int(cell_id)
                    except (ValueError, TypeError):
                        print("Exception while reading {}".format(self.input_file_path))
                        break
                    else:
                        cell_1_name = cell_id_vs_name[cell_id]
            except KeyError:
                pass
                # print("Cell_id_missing in mentor")
            else:
                row_items[8] = cell_1_name
            try:
                cell_id = row_items[11]
                cell_2_name = None
                if cell_id != '' and cell_id is not None:
                    try:
                        cell_id = int(cell_id)
                    except (ValueError, TypeError):
                        print("Exception while reading {}".format(self.input_file_path))
                        break
                    else:
                        cell_2_name = cell_id_vs_name[cell_id]
            except KeyError:
                pass
                # print("Cell_id_missing in mentor")
            else:
                row_items[11] = cell_2_name
            try:
                cell_id = row_items[14]
                cell_3_name = None
                if cell_id != '' and cell_id is not None:
                    try:
                        cell_id = int(cell_id)
                    except (ValueError, TypeError):
                        print("Exception while reading {}".format(self.input_file_path))
                        break
                    else:
                        cell_3_name = cell_id_vs_name[cell_id]
            except KeyError:
                pass
                # print("Cell_id_missing in mentor")
            else:
                row_items[14] = cell_3_name
            try:
                cell_id = row_items[17]
                cell_4_name = None
                if cell_id != '' and cell_id is not None:
                    try:
                        cell_id = int(cell_id)
                    except (ValueError, TypeError):
                        print("Exception while reading {}".format(self.input_file_path))
                        break
                    else:
                        cell_4_name = cell_id_vs_name[cell_id]
            except KeyError:
                pass
                # print("Cell_id_missing in mentor")
            else:
                row_items[17] = cell_4_name

            try:
                cell_id = row_items[20]
                cell_5_name = None
                if cell_id != '' and cell_id is not None:
                    try:
                        cell_id = int(cell_id)
                    except (ValueError, TypeError):
                        print("Exception while reading {}".format(self.input_file_path))
                        break
                    else:
                        cell_5_name = cell_id_vs_name[cell_id]
            except KeyError:
                pass
                # print("Cell_id_missing in mentor")
            else:
                row_items[20] = cell_5_name

            try:
                cell_id = row_items[23]
                cell_6_name = None
                if cell_id != '' and cell_id is not None:
                    try:
                        cell_id = int(cell_id)
                    except (ValueError, TypeError):
                        print("Exception while reading {}".format(self.input_file_path))
                        break
                    else:
                        cell_6_name = cell_id_vs_name[cell_id]
            except KeyError:
                pass
                # print("Cell_id_missing in mentor")
            else:
                row_items[23] = cell_6_name

            try:
                cell_id = row_items[26]
                cell_7_name = None
                if cell_id != '' and cell_id is not None:
                    try:
                        cell_id = int(cell_id)
                    except (ValueError, TypeError):
                        print("Exception while reading {}".format(self.input_file_path))
                        break
                    else:
                        cell_7_name = cell_id_vs_name[cell_id]
            except KeyError:
                pass
                # print("Cell_id_missing in mentor")
            else:
                row_items[26] = cell_7_name

            try:
                cell_id = row_items[29]
                cell_8_name = None
                if cell_id != '' and cell_id is not None:
                    try:
                        cell_id = int(cell_id)
                    except (ValueError, TypeError):
                        print("Exception while reading {}".format(self.input_file_path))
                        break
                    else:
                        cell_8_name = cell_id_vs_name[cell_id]
            except KeyError:
                pass
                # print("Cell_id_missing in mentor")
            else:
                row_items[29] = cell_8_name

            updated_content_of_file[row_id] = row_items
        return updated_content_of_file

    def print_updated_content_on_console(self):
        updated_content = self.populate_cell_name()
        print("Number of rows in file = {}".format(len(updated_content.keys())))
        if len(updated_content.keys()) !=0:
            out_file_path = os.path.join(self.out_dir, self.input_file_name)
            with open(out_file_path, 'w', newline='') as out_file:

                field_names = ['Long','Lat','Cell_P','RSRQ_P','RSCP_P','CellID_1','RSRQ_1','RSCP_1','CellID_2','RSRQ_2','RSCP_2','CellID_3','RSRQ_3','RSCP_3','CellID_4','RSRQ_4','RSCP_4','CellID_4','RSRQ_4','RSCP_4','CellID_5','RSRQ_5','RSCP_5','CellID_6','RSRQ_6','RSCP_6','CellID_7','RSRQ_7','RSCP_7','CellID_8','RSRQ_8','RSCP_8','CellID_9','RSRQ_9','RSCP_9']
                writer = csv.writer(out_file, delimiter='|')
                writer.writerow(field_names)
                for row_ind, row in updated_content.items():
                    writer.writerow(row)


