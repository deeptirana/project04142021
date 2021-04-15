import sqlite3

def show_color(email_id):
    connection = sqlite3.connect('db1.db',check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT pk FROM users where email_id = '{}';""".format(email_id))
    id_1 = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    message = '{email_id}\'s id in the database is {id_1}.'.format(email_id=email_id, id_1 = id_1)
    return message

def check_pw(email_id):
    connection = sqlite3.connect('db1.db',check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT password FROM users where email_id = '{}';""".format(email_id))
    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    return password    

def check_users():
    connection = sqlite3.connect('db1.db',check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT email_id FROM users ORDER BY pk DESC;""")
    db_users = cursor.fetchall()
    users = []

    for i in range(len(db_users)):
        person = db_users[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()

    return users      


def signup(email_id, password):
    connection = sqlite3.connect('db1.db',check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT password FROM users where email_id = '{}';""".format(email_id))
    exist = cursor.fetchone()
    if exist is None:
        cursor.execute(""" INSERT INTO users(email_id,password) VALUES ({},{});""".format(email_id,password))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        return ('user already existed!!')   

    message = 'You have successfully signed up!'     

    return password     

NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'    

def add_to_list(listname,task_name):
    connection = sqlite3.connect('db1.db',check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""insert into dashboard(listname, task_name,task_status) VALUES({},{});""".format(listname, task_name,task_status))
    connection.commit()
    cursor.close()
    connection.close()
    return password      

def getalltask():
    print("here")
    connection = sqlite3.connect('db1.db',check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT task_name from dashboard;""")
    alltask = cursor.fetchall()

    for t in alltask:
        print(t)

    connection.commit()
    cursor.close()
    connection.close()
    return alltask         
