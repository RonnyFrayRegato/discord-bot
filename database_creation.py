import mariadb
import sys

global cur


def connect_to_db():
    try:
        conn = mariadb.connect(
            user="root",
            password="password",
            host="127.0.0.1",
            port=3306,
            database="example"
        )
        print("connected")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    global cur
    cur = conn.cursor()
    show_databases()


def show_databases():
    cur.execute("SHOW DATABASES")
    for database in cur:
        print(database)
