import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="monopoly"
)
# [(0,0),(0,0)]
cursor=mydb.cursor()
cursor.execute(f"select id from currentTransaction where type='players_team'")
player_id=cursor.fetchone()[0]
print(player_id)
