# SELECT * FROM users
# INSERT INTO users (email, password) VALUES ('lev@mail.ru', 'qwerty')

import sqlite3


def get_all_users():
    conn = sqlite3.connect('psw_and_emails.db')
    cur = conn.cursor()
    res = cur.execute('SELECT email FROM users')
    #  [(8.2,), (7.5,)]
    data = [i[0] for i in res.fetchall()]
    conn.close()
    return data


def insert_new_user(email, password):
    conn = sqlite3.connect('psw_and_emails.db')
    cur = conn.cursor()
    cur.execute(
        f"INSERT INTO users (email, password) VALUES ('{email}', '{password}')")
    conn.commit()
    conn.close()
