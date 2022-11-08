import mariadb
import sys
#run this command in linux to start the docker container with maria db
    #docker run -d -p 3306:3306 -e MYSQL_DATABASE=example -e MYSQL_ROOT_PASSWORD=password -e TZ=America/Los_Angeles --name mdb103 mariadb:10.3

    #CREATE TABLE employees (user_ID int, message_count int);

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
    show_databases()


def show_databases():
    cur.execute("SHOW DATABASES")
    for database in cur:
        print(database)


def update_message_count(user_ID):
    try:
        statement = "SELECT user_ID, message_count FROM user_message_count WHERE user_ID=%s"
        data = (user_ID,)
        cur.execute(statement, data)
        for (user_ID, message_count) in cur:
            print(f"Successfully retrieved {user_ID}, {message_count}")
    except database.Error as e:
        print(f"Error retrieving entry from database: {e}")
    try:
        statement = "INSERT INTO user_message_count (user_ID ,message_count) VALUES (%s, %s)"
        data = (user_ID, message_count + 1)
        cur.execute(statement, data)
        conn.commit()
        print("Successfully added entry to database")
    except database.Error as e:
        print(f"Error adding entry to database: {e}")