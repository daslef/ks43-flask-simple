import sqlite3
import datetime

def init_tables():

    connection = sqlite3.connect('app.db')
    cursor = connection.cursor()

    cursor.execute(f'''CREATE TABLE IF NOT EXISTS users (
        id integer primary key,
        username varchar(20) unique not null,
        password varchar(50) not null,
        email varchar(40) unique not null
        )''')

    cursor.execute(f'''CREATE TABLE IF NOT EXISTS tasks (
        id integer primary key,
        user_id integer not null,
        title varchar(40) unique not null,
        content text,
        start_date date not null default CURRENT_DATE,
        end_date date,
        status boolean default 0
        )''')

    connection.close()

def add_user(username, email, password):
    connection = sqlite3.connect('app.db')
    cursor = connection.cursor()
    cursor.execute('''insert into users (username, password, email) 
                   values (?, ?, ?)''', [username, password, email])
    cursor.execute('select * from users')
    print(cursor.fetchall())
    connection.commit()
    connection.close()

def login(email, password):
    connection = sqlite3.connect('app.db')
    cursor = connection.cursor()
    cursor.execute('select username from users where email = ? and password = ?',
                                                        [email, password])
    user = cursor.fetchone()
    print(user)
    connection.close()
    return user

def add_task(user_id, title, content="", end_date=""):
    connection = sqlite3.connect('app.db')
    cursor = connection.cursor()
    cursor.execute('''insert into tasks (user_id, title, content, end_date) 
                   values (?, ?, ?, ?)''', [user_id, title, content, end_date])
    cursor.execute('select * from tasks')
    print(cursor.fetchall())
    connection.commit()
    connection.close()

def get_user(name):
    connection = sqlite3.connect('app.db')
    cursor = connection.cursor()
    cursor.execute('select id from users where username = ?', [name])
    user = cursor.fetchone()
    print(user)
    connection.close()
    return user[0]

def get_tasks(name):
    connection = sqlite3.connect('app.db')
    cursor = connection.cursor()
    user_id = get_user(name)
    cursor.execute('select * from tasks where user_id = ?', [user_id])
    tasks = cursor.fetchall()
    print(tasks)
    connection.close()
    return tasks    

# init_tables()