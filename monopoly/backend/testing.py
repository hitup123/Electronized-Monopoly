from dbConnector import dbconnect
mydb=dbconnect()
# [(0,0),(0,0)]
cursor=mydb.cursor()
property_id=(28,)
txn=1
# cursor.execute(f'SELECT * FROM log WHERE txn_order > {txn}')
# cursor.execute(f"select owner_id from properties where color='Utility'")
cursor.execute("select flag from flags")
player_id=cursor.fetchone()

print(player_id)
