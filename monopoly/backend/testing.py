from dbConnector import dbconnect
mydb=dbconnect()
# [(0,0),(0,0)]
cursor=mydb.cursor()
property_id=(28,)
txn=1
# cursor.execute(f'SELECT * FROM log WHERE txn_order > {txn}')
# cursor.execute(f"select owner_id from properties where color='Utility'")
# cursor.execute("select flag from flags")
team_id=1
PropertyData="Strand"
cursor.execute(f"SELECT propertiesOwned FROM players WHERE team = {team_id} ")
result=cursor.fetchone()
print(result)
if(result[0]!=None):
    s=result[0]+PropertyData
else:
    s=PropertyData
cursor.execute(f"""
    UPDATE players 
    SET propertiesOwned ='{s}'
""")
player_id=cursor.fetchone()
mydb.commit()
print(player_id)
