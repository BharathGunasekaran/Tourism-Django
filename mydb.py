import mysql.connector
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'bharath',
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE tour")

print("Successfully created the DataBase")