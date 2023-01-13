import sqlite3

connect_db = sqlite3.connect("test.db")

cur = connect_db.cursor()

connect_db.execute('CREATE TABLE work_time_data(id INTEGER PRIMARY KEY, Memo TEXT, GoalTime INTGER, WorkDate DATE, StartTime TIME, EndTime TIME)')

cur.executemany(
    'INSERT INTO work_time_data VALUES (?, ?, ?, ?, ?, ?)',
    [(1, 'memo1', 5, '2023-01-14', '12:00:00', '15:15:12'),
     (2, 'memo2', 5, '2023-01-14', '12:00:00', '15:15:12'),
    ]
)

cur.executemany(
    "INSERT INTO work_time_data(Memo, GoalTime, WorkDate, StartTime, EndTime) VALUES (?, ?, ?, ?, ?)",
    [('memo3', 5, '2023-01-14', '12:00:00', '15:15:12')]
)

connect_db.commit()
connect_db.close()