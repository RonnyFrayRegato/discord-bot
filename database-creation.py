import mariadb
import sys
#run this command in linux to start the docker container with maria db
    #docker run -d -p 3306:3306 -e MYSQL_DATABASE=example -e MYSQL_ROOT_PASSWORD=password -e TZ=America/Los_Angeles --name mdb103 mariadb:10.3


global curr


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
    cur = conn.cursor()
    show_databases(cur)


def show_databases(cur):
    cur.execute("SHOW DATABASES")
    for database in cur:
        print(database)
