import mysql.connector

# Connect to the MySQL database

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="monopoly"
)
def search_table():
        # Get user input
        id = input("Enter the ID: ")

        # Search the "cards" table using the ID
        cursor = mydb.cursor()
        cursor.execute("SELECT type FROM cards WHERE id = %s", (id,))
        result = cursor.fetchone()
        # print(result)
        getType=False
        if result:
                table_name = result[0]
                # Search the retrieved table using the ID
                cursor.execute(f"SELECT * FROM {table_name} WHERE id = %s", (id,))
                result = cursor.fetchone()
                if result:
                        print(f"Found in table {table_name}: {result}")
                        getType=True
                else:
                        print(f"No record found in table {table_name} for ID {id}")
        else:
                print(f"No record found in the 'cards' table for ID {id}")

        return id,table_name

if __name__ == "__main__":
        cursor=mydb.cursor()
        # id,table_name = search_table()
        
        # print(f"ID: {id}, Table: {table_name}")
        # cursor.execute(f"insert into currentTransaction (id,type) values({id},'{table_name}')")
        # mydb.commit()
        cursor.execute(f"select type from currentTransaction")
        result = cursor.fetchall()
        # print(result)
        currAction=[]
        for x in result:

                currAction.append(x[0])
        print(currAction) 
         
        #storing the card scanned so as to keep track of the current transaction
        # result = cursor.fetchone()
        # print(result)
        # Close the database connection
        scan_order=[['properties','players_team'],['',''] ]
        actions={'buy/rent/house':1,'other':2}
        if currAction in scan_order:
                index = scan_order.index(currAction)
                # action=actions[index]
                if(index==0):
                        cursor.execute(f"select id from currentTransaction where type='properties'")
                        result = cursor.fetchone()
                        print(result[0])

        mydb.close()