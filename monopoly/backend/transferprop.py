import json
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="monopoly"
)
cursor=mydb.cursor()
def transferproperties(x):
    cursor.execute(f"select id from currentTransaction where type='properties'")
    property_id = cursor.fetchone()#property being bought
    cursor.execute(f"select * from properties where id={property_id[0]}")
    property_data = cursor.fetchone()
    cursor.execute(f"select id from currentTransaction where type='players'")
    player_id = cursor.fetchone()#person buying the property
    cursor.execute(f"select * from players where id=P{player_id[0]}")
    player_data = cursor.fetchone()
    cursor.execute(f"update players cash = cash - {x} where id = {player_id[0]}")
    cursor.execute(f"update players cash = cash + {x} where id = {property_data[len(property_data)-2]}")
    cursor.execute(f"update properties set owner_id = {player_data[0]} where id = {property_id[0]}")
    mydb.commit()