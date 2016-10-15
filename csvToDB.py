import sys
import csv
import sqlite3

# creates db if one does not exist
# conn = sqlite3.connect('some.db')
class CSVTool(object):
    
    def __init__(self, path=None):
        self.path = None
        self.csv_name = None
        self.db = None
        
    def dump_to_db(self, csv_path):
        # store connection
        self.db = sqlite3.connect('csi.db')
        # get cursor object
        cur = self.db.cursor()
        # sql staement to create a tbale with only ID field
        sqlst = 'CREATE TABLE csi(ID int PRIMARY KEY NOT NULL)'
        # preform the above statement
        cur.execute(sqlst)
        with open(csv_path) as csv_file:
            read_csv = csv.DictReader(csv_file)
            import pdb; pdb.set_trace()
            for row in read_csv:
                sqlst = """
                    
                """
                cur.execute(sqlst.format(int(read_csv.line_num)))
            self.db.commit()
            self.db.close()
if __name__ == '__main__':
    ct = CSVTool()
    ct.dump_to_db('csi.csv')
    
