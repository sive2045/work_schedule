import datetime
import sqlite3
 
def what_day_is_today():
    now = datetime.datetime.now()
    t = ['Monday', 'Tuseday', 'Wednseday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    r = datetime.datetime.today().weekday()
    day = str(now.year) + '-' + str(now.month).rjust(2, '0') + '-' + str(now.day).rjust(2, '0') + '\n' + t[r]
    return day

def cal_achievement_rate(total_time, goal_time) -> float:
    total_time_to_hour = total_time / 60
    ach_time = '{:.2f}'.format(total_time_to_hour * 100 /goal_time) + ' %'
    return ach_time


def sub_time(start_time, end_time) -> float:
    """
    문자열 시간 차이를 시간축 기준으로 반환

    15:15:30 - 12:00:00 = 3.25 (H)
    """
    _start_time = list(map(int, start_time.split(':')))
    start_hour = _start_time[0]
    start_min = _start_time[1]
    start_sec = _start_time[2]

    _end_time = list(map(int, end_time.split(':')))
    end_hour = _end_time[0]
    end_min = _end_time[1]
    end_sec = _end_time[2]

    time_duration = (end_hour - start_hour) + (end_min - start_min) / 60 + (end_sec - start_sec) / 60*60
    return '{:.2f}'.format(time_duration)


def db_insert_work_start_time(memo, goal_time ,work_date, work_star_time) -> int:
    connect_db = sqlite3.connect("db/test.db")
    
    cur = connect_db.cursor()

    cur.executemany(
        "INSERT INTO work_time_data(Memo, GoalTime, WorkDate, StartTime) VALUES (?, ?, ?, ?)",
        [(memo, goal_time, work_date, work_star_time)]
    )

    cur.execute('SELECT id from work_time_data ORDER BY ROWID DESC LIMIT 1') # 가장 나중에 추가한 row data의 id 추출
    id = cur.fetchall()[0][0] # 작업한 데이터 unique id

    connect_db.commit()
    connect_db.close()

    return id

def db_insert_work_end_time() -> None:
    pass

if __name__ == "__main__":
    day = what_day_is_today()
    print(day)