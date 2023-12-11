import sqlite3
import threading
import datetime


class pctime:
    def __init__(self):
        self.db = sqlite3.connect(
            "C:/코딩/Pc_time_check/Database/Pc_Time.db", check_same_thread=False
        )
        self.cursor = self.db.cursor()
        self.check_time_start()

    def read_row_num(self):
        self.cursor.execute("SELECT count(*) FROM Pc_Time")
        row_num = self.cursor.fetchone()
        return row_num

    def check_time_start(self):
        self.start_time = datetime.datetime.now()
        self.Seq = self.read_row_num()[0] + 1
        insert_query = (
            f'INSERT INTO Pc_Time VALUES("{self.Seq}","{self.start_time}", "", "")'
        )
        self.cursor.execute(insert_query)
        self.db.commit()
        self.update_time()

    def update_time(self):
        self.terminate_time = datetime.datetime.now()
        self.use_time = self.terminate_time - self.start_time
        self.cursor.execute(
            f"UPDATE Pc_Time SET End_time ='{self.terminate_time}', Use_time ='{self.use_time}' WHERE Seq=='{self.Seq}'"
        )
        self.db.commit()
        timer = threading.Timer(1, self.update_time)
        timer.start()


pcstart = pctime()
