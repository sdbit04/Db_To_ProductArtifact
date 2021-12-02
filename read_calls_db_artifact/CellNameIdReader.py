import cx_Oracle


class CellNameIdReader(object):

    def __init__(self, bdusr, bdpass, dbhost, dbport, dbservice):
        self.con_string = "{}/{}@{}:{}/{}".format(bdusr, bdpass, dbhost, dbport, dbservice)

    def get_cell_name(self):
        cell_id_v_cell_name = dict()
        con_ob = cx_Oracle.connect(self.con_string)
        query = "select distinct sector_id, sector_name from SECTOR_CARRIERS where sector_id is not null"
        cursor = con_ob.cursor()
        try:
            cursor.execute(query)
        except:
            print("Got exception while running query to mentor-db")
            raise
        else:
            for row in cursor:
                cell_id_v_cell_name[row[0]] = row[1]
            return cell_id_v_cell_name
        finally:
            con_ob.close()

