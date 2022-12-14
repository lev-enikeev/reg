# SELECT * FROM users
# INSERT INTO users (email, password) VALUES ('lev@mail.ru', 'qwerty')

import sqlite3


def db_connect(func):
    def inlt(*args, **kwargs):
        conn = sqlite3.connect('psw_and_emails.db')
        cur = conn.cursor()
        data = func(cur, conn, *args, **kwargs)
        conn.close()
        return data
    return inlt


@db_connect
def get_all_users(cur, conn):
    res = cur.execute('SELECT email FROM users')
    #  [(8.2,), (7.5,)]
    data = [i[0] for i in res.fetchall()]
    return data


@db_connect
def insert_new_user(cur, conn, email, password):
    cur.execute(
        f"INSERT INTO users (email, password, confirmed) VALUES ('{email}', '{password}', 0)")
    conn.commit()

@db_connect
def update_email(cur, conn, email):
    cur.execute(f"UPDATE users SET confirmed = 1 where email = '{email}' ")
    conn.commit()
