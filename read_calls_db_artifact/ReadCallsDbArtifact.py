import gzip
import pdb


class CallsDbArtReader(object):

    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def read_calls_db_artifact(self):
        # required_column_dict=[LON:33, LAT:34,CELL_PRIMARY:81,Q_D_P:82, P_D_P:84, cell_0:94, Q_0:95, P_0:97]
        with gzip.open(self.input_file_path) as input_zip_file:
            whole_files = dict()
            row_num = 0
            for line in input_zip_file.readlines():
                # pdb.set_trace()
                line_items = line.decode().split(sep="\t")
                # index of RECORD_TYPE = 7
                if int(line_items[7]) == 0:
                    selected_line_items = [line_items[33], line_items[34], line_items[81], line_items[82], line_items[84],
                                           line_items[94], line_items[95],line_items[97],line_items[105], line_items[106],
                                           line_items[108],line_items[116],line_items[117],line_items[119],line_items[127],
                                           line_items[128], line_items[130],line_items[138], line_items[139], line_items[141],
                                           line_items[149], line_items[150], line_items[152],
                                           line_items[160], line_items[161], line_items[163],
                                           line_items[174], line_items[175], line_items[176],
                                           line_items[185], line_items[186], line_items[188],
                                           line_items[196], line_items[197], line_items[199]]
                    whole_files[row_num]= selected_line_items
                    row_num +=1
        return whole_files


