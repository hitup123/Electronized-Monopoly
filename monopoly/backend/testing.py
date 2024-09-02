import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Grub@123",
    database="monopoly"
)
# [(0,0),(0,0)]
cursor=mydb.cursor()
cursor.execute(f"select * from PLAYERS ")
player_id=cursor.fetchall()
print(player_id)
