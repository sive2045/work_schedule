import sqlite3

connect_db = sqlite3.connect("test.db")

cur = connect_db.cursor()

connect_db.execute('CREATE TABLE work_time_data(id INTEGER PRIMARY KEY, Memo TEXT, GoalTime INTGER, WorkDate DATE, StartTime DATETIME, EndTime DATETIME, DurationWokrTime TIME)')
connect_db.execute('CREATE TABLE todo_data(id INTEGER PRIMARY KEY, Todo TEXT, TodoDate DATE, isDone BOOLEAN)')

cur.executemany(
    'INSERT INTO work_time_data VALUES (?, ?, ?, ?, ?, ?, ?)',
    [(1, 'memo1', 5, '2023-01-06', '2023-01-16:12:00:00', '2023-01-17:02:15:12', '03:55:12'),
    ]
)

cur.executemany(
    "INSERT INTO work_time_data(Memo, GoalTime, StartTime) VALUES (?, ?, ?)",
    [('memo42', 5, '2023-01-16:12:00:00')]
)

cur.executemany(
    'INSERT INTO todo_data VALUES (?, ?, ?, ?)',
    [(1, '논문읽기', '2023-01-14', 'FALSE'),
     (2, '논문뽑기', '2023-01-14', 'TRUE'),
    ]
)

cur.executemany(
    "INSERT INTO todo_data(Todo, TodoDate, isDone) VALUES (?, ?, ?)",
    [('ppt', '2023-01-14', 'TRUE'),]
)

connect_db.commit()
connect_db.close()