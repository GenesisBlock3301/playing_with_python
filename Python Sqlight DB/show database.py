import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='mydatabase'
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255),address VARCHAR (255))")
mycursor.execute("""SHOW TABLES""")
print(type(mycursor))
# show database
for i in mycursor:
    print(i)
print("TABLE CREATED")
