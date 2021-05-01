import sqlite3


try:
    # connect with database
    sqliteConnection = sqlite3.connect('sqlightFirst.db')
    # connection with cursor for executing sqlite command.
    cursor = sqliteConnection.cursor()
    with open('sqlite.sql','r') as sqlite_file:
        sql_scripts = sqlite_file.read()

    # execute scripts
    cursor.executescript(sql_scripts)
    print("Scripts execute successfully")
    cursor.close()

except sqlite3.Error as error:
    print(f"Error connecting while {error} ")
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("Sql connection is already close.")
