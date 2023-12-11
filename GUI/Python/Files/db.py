import sqlite3
import datetime


def check_seq_list():
    db = sqlite3.connect(f"../../../Database/Pc_Time.db", check_same_thread=False)
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM Pc_Time")
    count = cursor.fetchone()[0]
    return int(count)


def get_list(sort, desc):
    db = sqlite3.connect(f"../../../Database/Pc_Time.db", check_same_thread=False)
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM Pc_Time")
    count_lists = cursor.fetchone()[0]
    get_list = []
    if int(desc) == 0:
        cursor.execute(f'SELECT * FROM Pc_Time Order By "{sort}"')
    else:
        cursor.execute(f'SELECT * FROM Pc_Time Order By "{sort}" DESC')

    for i in range(count_lists):
        li = cursor.fetchone()[1:]
        get_list.append(li)
    return get_list


def get_recent_data():
    db = sqlite3.connect(f"../../../Database/Pc_Time.db", check_same_thread=False)
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Pc_Time ORDER BY Seq DESC")
    return cursor.fetchone()


def cal_week():
    to = str(datetime.datetime.now())[:10]
    to1 = str(datetime.datetime.now() - datetime.timedelta(days=1))[:10]
    to2 = str(datetime.datetime.now() - datetime.timedelta(days=2))[:10]
    to3 = str(datetime.datetime.now() - datetime.timedelta(days=3))[:10]
    to4 = str(datetime.datetime.now() - datetime.timedelta(days=4))[:10]
    to5 = str(datetime.datetime.now() - datetime.timedelta(days=5))[:10]
    to6 = str(datetime.datetime.now() - datetime.timedelta(days=6))[:10]
    db = sqlite3.connect(f"../../../Database/Pc_Time.db", check_same_thread=False)
    cursor = db.cursor()
    cursor.execute(
        f"SELECT Use_time FROM Pc_Time Where Start_time like '{to}%' OR Start_time like '{to1}%' OR Start_time like '{to2}%' OR Start_time like '{to3}%' OR Start_time like  '{to4}%' OR Start_time like '{to5}%' OR Start_time like '{to6}%'"
    )
    return len(cursor.fetchall())
