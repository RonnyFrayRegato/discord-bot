import mariadb
import sys

# run this command in linux to start the docker container with maria db
# docker run -d -p 3306:3306 -e MYSQL_DATABASE=example -e MYSQL_ROOT_PASSWORD=password -e TZ=America/Los_Angeles --name mdb103 mariadb:10.3


global cur
global conn


def connect_to_db():
    try:
        global conn
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


# print users message count
def show_user_msg_count(user_ID):
    cur.execute("SELECT msg_count FROM user_activity WHERE ID=?", (user_ID,))

    for msg_count in cur:
        msg_count_string = f"{msg_count}"
        return msg_count_string


# create the table
def init_table():
    cur.execute("CREATE TABLE IF NOT EXISTS user_activity(ID varchar(50), msg_count int)")
    conn.commit()


# update statement
def increase_user_msg_count(user_ID):
    cur.execute("UPDATE user_activity SET msg_count = msg_count + 1 WHERE ID=?", (user_ID,))
    query = f"SELECT * FROM user_activity"

    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)
    conn.commit()


# insert new data
def init_user_for_msg_count(user_ID):
    cur.execute("INSERT INTO user_activity (ID, msg_count) VALUES (?, ?)", (user_ID, 0))
    conn.commit()


# insert new data
def delete_user_from_msg_count(user_ID):
    cur.execute("DELETE FROM user_activity WHERE ID=?", (user_ID,))
    conn.commit()