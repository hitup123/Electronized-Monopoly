from dbConnector import dbconnect
mydb=dbconnect()
# [(0,0),(0,0)]
cursor=mydb.cursor()
property_id=(28,)
cursor.execute(f"select * from properties where id ={property_id[0]}")

player_id=cursor.fetchall()
print(player_id)
