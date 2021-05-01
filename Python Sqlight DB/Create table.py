import sqlite3

try:
    # connect with database
    sqliteConnection = sqlite3.connect('sqlightFirst.db')
    # connection with cursor for executing sqlite command.
    cursor = sqliteConnection.cursor()
    print("Database created and successfully Connected to db")

    create_table = """CREATE TABLE contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
); """
    # execute above query using cursor
    cursor.execute(create_table)
    sqliteConnection.commit()
    print("Sqlite table is created.")
    cursor.close()
except sqlite3.Error as error:
    print(f"Error connecting while {error} ")
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("Sql connection is already close.")
