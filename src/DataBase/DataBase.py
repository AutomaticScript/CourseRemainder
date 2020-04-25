import subprocess
import sqlite3


class DataBase:

    def __init__(self):
        self.db_dir = '/home/lida/Desktop/tool/CourseRemainder/db'
        subprocess.run(["rm", "-rf", self.db_dir])
        subprocess.run(["mkdir", self.db_dir])
        self.conn = sqlite3.connect(self.db_dir + '/rerun_index.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE rerun_index (class_name text, current_index integer)')
        self.cursor.execute("INSERT INTO rerun_index VALUES ('小班课', 0)")
        self.cursor.execute("INSERT INTO rerun_index VALUES ('定制学_有', 0)")
        self.cursor.execute("INSERT INTO rerun_index VALUES ('定制学_无', 0)")
        self.conn.commit()

    def update(self, values):
        # values = (1, '小班课')
        self.cursor.execute("UPDATE rerun_index SET current_index = ? WHERE class_name = ?", values)
        self.conn.commit()

    def query(self, values):
        # values = ('小班课',)
        self.cursor.execute('SELECT current_index FROM rerun_index WHERE class_name=?', values)
        return self.cursor.fetchone()[0]

    def close(self):
        self.conn.close()

