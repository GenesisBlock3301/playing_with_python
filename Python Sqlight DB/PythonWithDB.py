import sqlite3


try:
    # connect with database
    sqliteConnection = sqlite3.connect('sqlightFirst.db')
    # connection with cursor for executing sqlite command.
    cursor = sqliteConnection.cursor()
    print("Database created and successfully Connected to db")

    select_query = "select sqlite_version()"
    # execute above query using cursor
    cursor.execute(select_query)
    # fetch the query using fetchall
    record = cursor.fetchall()
    print(f"Sql version is {record}")
    cursor.close()
except sqlite3.Error as error:
    print(f"Error connecting while {error} ")
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("Sql connection is already close.")
