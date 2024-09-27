from dbConnector import dbconnect
mydb=dbconnect()
# [(0,0),(0,0)]
cursor=mydb.cursor()
property_id=(28,)
txn=1
# cursor.execute(f'SELECT * FROM log WHERE txn_order > {txn}')
# cursor.execute(f"select owner_id from properties where color='Utility'")
# cursor.execute("select flag from flags")
# team_id=1
# PropertyData="Strand"
# cursor.execute(f"SELECT propertiesOwned FROM players WHERE team = {team_id} ")
# result=cursor.fetchone()
# print(result)
# if(result[0]!=None):
#     s=result[0]+PropertyData
# else:
#     s=PropertyData
# cursor.execute(f"""
#     UPDATE players 
#     SET propertiesOwned ='{s}'
# """)
# player_id=cursor.fetchone()
# mydb.commit()
# print(player_id)
# cursor.execute("select name,owner_id from properties")
# print(cursor.fetchall()) 
# cursor.execute("SELECT team FROM teams")
# teams = cursor.fetchall()
# for t in teams:
#     team_id = t[0]
#     str1 = ""
#     cursor.execute("SELECT name FROM properties WHERE owner_id = %s", (team_id,))
#     result = cursor.fetchall()
#     for prop in result:
#         str1 += f"_{prop[0]}"
#     if str1 == "":
#         str1 = None
#     cursor.execute("UPDATE players SET propertiesOwned = %s WHERE team = %s", (str1, team_id))
#     mydb.commit()
cursor.execute(f"select sum(house) from properties where house <> 5") # Check if there are houses remaining for purchase
print(cursor.fetchone())
    # print("hi:",str1)