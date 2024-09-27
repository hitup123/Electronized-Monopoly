import json
import time
from  dbConnector import dbconnect
mydb=dbconnect()
cursor=mydb.cursor()
def transferproperties(x):
    
    cursor.execute(f"select id from currentTransaction where type='properties'")
    property_id = cursor.fetchone()#property being bought
    cursor.execute(f"select * from properties where id={property_id[0]}")
    property_data = cursor.fetchone()
    cursor.execute(f"select id from currentTransaction where type='players'")
    player_id = cursor.fetchone()#person buying the property
    cursor.execute(f"select team from teams where id={player_id[0]}")
    team_id = cursor.fetchone()#id of the team buying
    print(team_id) 
    cursor.execute(f"update players set cash = cash - {x} where team = {team_id[0]}")
    cursor.execute(f"update players set cash = cash + {x} where team = {property_data[len(property_data)-2]}")
    cursor.execute(f"update properties set owner_id = {team_id[0]} where id = {property_id[0]}")
    cursor.execute("SELECT team FROM teams")
    teams = cursor.fetchall()
    for t in teams:
        team_id = t[0]
        str1 = ""
        cursor.execute("SELECT name FROM properties WHERE owner_id = %s", (team_id,))
        result = cursor.fetchall()
        for prop in result:
            str1 += f"_{prop[0]}"
        if str1 == "":
            str1 = None
        cursor.execute("UPDATE players SET propertiesOwned = %s WHERE team = %s", (str1, team_id))
        mydb.commit()
    #update properties owned according to this thanks
    mydb.commit()