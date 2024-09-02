from backend.dbConnector import dbconnect
mydb=dbconnect()
# [(0,0),(0,0)]
cursor=mydb.cursor()
cursor.execute(f"select * from log ")
player_id=cursor.fetchall()
print(player_id)
