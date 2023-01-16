import datetime
import sqlite3


dir_local_db = "db/test.db"


def what_day_is_today()  -> str:
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


def db_insert_work_start_time(goal_time, work_star_time) -> int:
    connect_db = sqlite3.connect(dir_local_db)
    
    cur = connect_db.cursor()

    cur.executemany(
        "INSERT INTO work_time_data(GoalTime, StartTime) VALUES (?, ?)",
        [(goal_time, work_star_time)]
    )

    cur.execute('SELECT id from work_time_data ORDER BY ROWID DESC LIMIT 1') # 가장 나중에 추가한 row data의 id 추출
    id = cur.fetchall()[0][0] # 작업한 데이터 unique id

    connect_db.commit()
    connect_db.close()

    return id

def db_insert_work_end_time(id, memo, work_end_time, duration_time) -> None:
    connect_db = sqlite3.connect(dir_local_db)
    
    cur = connect_db.cursor()

    cur.execute(
        "update work_time_data set EndTime = :end_time WHERE id = :id",
        {"end_time": work_end_time, "id": id}
    )

    cur.execute(
        "update work_time_data set Memo = :memo WHERE id = :id",
        {"memo": memo, "id": id}
    )

    cur.execute(
        "update work_time_data set DurationWokrTime = :duration_time WHERE id = :id",
        {"duration_time": duration_time, "id": id}
    )

    connect_db.commit()
    connect_db.close()

def db_insert_todo(todo, todo_date) -> int:
    connect_db = sqlite3.connect(dir_local_db)
    
    cur = connect_db.cursor()

    cur.executemany(
        "INSERT INTO todo_data(Todo, TodoDate, isDone) VALUES (?, ?, ?)",
        [(todo, todo_date, 'FALSE')]
    )

    cur.execute('SELECT id from todo_data ORDER BY ROWID DESC LIMIT 1') # 가장 나중에 추가한 row data의 id 추출
    id = cur.fetchall()[0][0] # 작업한 데이터 unique id

    connect_db.commit()
    connect_db.close()

    return id

def db_update_todo(id, todo) -> None:
    connect_db = sqlite3.connect(dir_local_db)
    
    cur = connect_db.cursor()

    cur.execute(
        "update todo_data set Todo = :todo WHERE id = :id",
        {"todo": todo, "id": id}
    )

    connect_db.commit()
    connect_db.close()

def db_delete_todo(id) -> None:
    connect_db = sqlite3.connect(dir_local_db)
    
    cur = connect_db.cursor()

    cur.execute(
        "delete from todo_data WHERE id = :id",
        {"id": id}
    )

    connect_db.commit()
    connect_db.close()

def db_is_done_todo(id, done) -> None:
    connect_db = sqlite3.connect(dir_local_db)
    
    cur = connect_db.cursor()

    cur.execute(
        "update todo_data set isDone = :done WHERE id = :id",
        {"done": done, "id": id}
    )

    connect_db.commit()
    connect_db.close()

def db_find_todo_id(todo_data, todo) -> int:
    for _, data in enumerate(todo_data):
        if data['todo'] == todo:
            return data['id']            

def update_todo_list(todo_data, id, updated_todo) -> None:
    for i, data in enumerate(todo_data):
        if data['id'] == id:
            todo_data[i]['todo'] = updated_todo

if __name__ == "__main__":
    day = what_day_is_today()
    print(day)