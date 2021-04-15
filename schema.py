import sqlite3


connection = sqlite3.connect('db1.db', check_same_thread = False)
cursor = connection.cursor()


cursor.execute(
    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        email_id VARCHAR(16),
        password VARCHAR(32)
    );"""
)

cursor.execute(
    """CREATE TABLE dashboard(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        listname VARCHAR(16),
        task_name VARCHAR(16),
        task_status VARCHAR(32)
    );"""
)


connection.commit()
cursor.close()
connection.close()