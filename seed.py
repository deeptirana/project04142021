import sqlite3


connection = sqlite3.connect('db1.db', check_same_thread=False)

cursor =  connection.cursor()


cursor.execute(
    """INSERT INTO users(
        email_id,
        password
        )VALUES(
            'user1',
            'abc'
        );"""
)


cursor.execute(
    """INSERT INTO users(
        email_id,
        password
        )VALUES(
            'user2',
            'def'
        );""")


cursor.execute(
    """INSERT INTO dashboard(
        listname,
        task_name,
        task_status
        )VALUES(
            'Designing',
            'interface',
            'pending'
        );""")

cursor.execute(
    """INSERT INTO dashboard(
        listname,
        task_name,
        task_status
        )VALUES(
            'Testing',
            'Home page',
            'pending'
        );""")

cursor.execute(
    """INSERT INTO dashboard(
        listname,
        task_name,
        task_status
        )VALUES(
            'Documentation',
            'interface',
            'pending'
        );""")



connection.commit()
cursor.close()
connection.close()