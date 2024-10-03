import sqlite3


def initiate_db():
    connection = sqlite3.connect('database_.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        prise INTEGER NOT NULL
        )
        """)
    cursor.execute("""CREATE INDEX IF NOT EXISTS title ON Products(title)""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        """)
    cursor.execute("""CREATE INDEX IF NOT EXISTS username ON Users(username)""")

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('database_.db')
    cursor = connection.cursor()
    add_products()
    cursor.execute("""SELECT * FROM Products""")
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return rows


def add_products():
    connection = sqlite3.connect('database_.db')
    cursor = connection.cursor()
    initiate_db()
    for i in range(4):
        cursor.execute("""
        INSERT INTO Products(
        title,
        description,
        prise) VALUES(?, ?, ?)
        """, (f"Продукт №{i + 1}", f"Описание {i + 1}", str((i + 1) * 100)))
    connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('database_.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users(username, "
                   "email, "
                   "age,"
                   "balance) VALUES(?, ?, ?, ?)", (f"{username}", f"{email}", f"{age}", "1000"))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('database_.db')
    cursor = connection.cursor()
    check_username = cursor.execute("SELECT * FROM Users WHERE username = ?", (f"{username}", ))
    if check_username.fetchone() is None:
        return True
    else:
        return False


get_all_products()
