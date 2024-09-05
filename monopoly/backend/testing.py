from dbConnector import dbconnect
mydb=dbconnect()
# [(0,0),(0,0)]
cursor=mydb.cursor()
property_id=(28,)
txn=1
cursor.execute(f'SELECT * FROM log WHERE txn_order > {txn}')

player_id=cursor.fetchall()
print(player_id)
