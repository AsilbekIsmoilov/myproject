import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password123'
)


cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE list_db')
