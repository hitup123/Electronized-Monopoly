import mysql.connector
def dbconnect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="monopoly"
    )  
    return mydb

mydb = dbconnect()
cursor = mydb.cursor()