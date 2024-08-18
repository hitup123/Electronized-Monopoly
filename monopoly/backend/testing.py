import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="monopoly"
)
# [(0,0),(0,0)]
cursor=mydb.cursor()
cursor.execute(f"select owner_id from properties where color='red'")
player_id=cursor.fetchall()
print(player_id[0][0])
