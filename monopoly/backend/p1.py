import random
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
        scan_order=[['properties','players_team'],['action','properties','players_team'],['action','players_team','players_team'],['action','players_team'] ]
        actions={'buy/rent/house':1,'other':2}
        if currAction in scan_order:
                index = scan_order.index(currAction)
                # action=actions[index]
                if(index==0):
                        cursor.execute(f"select id from currentTransaction where type='properties'")
                        property_id = cursor.fetchone()
                        cursor.execute(f"select * from properties where id={property_id[0]}")
                        property_data = cursor.fetchone()
                        cursor.execute(f"select id from currentTransaction where type='players_team'")
                        player_id = cursor.fetchone()
                        cursor.execute(f"select * from players_team where id=P{player_id[0]}")
                        player_data = cursor.fetchone()
                        if(property_data[len(property_data)-2]=='NULL'):
                               
                                
                               
                                if(player_data[3]>property_data[3]):
                                        cursor.execute(f"update players_team set cash = cash - {property_data[3]} where id = {player_id[0]}")
                                        cursor.execute(f"update properties set owner_id = {player_data[0]} where id = {property_id[0]}")
                                        # mydb.commit()
                                else:
                                        print("Insufficient balance")
                        elif(property_data[len(property_data)-2]!=player_id[0]):
                                cursor.execute(f"select house from properties where id={property_id[0]}")
                                house = cursor.fetchone()[0]
                                cursor.execute(f"select R{house} from properties where id={property_id[0]}")
                                rent=cursor.fetchone()[0]
                                print(rent)
                                cursor.execute(f"update players_team set cash = cash - {rent} where id = {player_id[0]}")
                                cursor.execute(f"update players_team set cash = cash + {rent} where id = {property_data[len(property_data)-2]}")
                                # mydb.commit()
                        
                        elif(property_data[len(property_data)-2]==player_id[0]):
                                # cursor.execute(f"select color from properties where id={property_id[0]}")
                                property_color = property_data[2]
                                cursor.execute(f"select owner_id from properties where color='{property_color}' ")
                                owned_properties = cursor.fetchall()
                                if all(x == player_id for x in owned_properties):
                                        # Build house on the appropriate property

                                                # property_color='red'
                                                cursor.execute(f"select house from properties where color='{property_color}' ")
                                                for i in range(0,len(result)):
                                                        j=result.pop(i)
                                                        result.append(j[0])
                                                # cursor.execute(f"update properties set house = house + 1 where id={property_to_build[0]}")
                                                result = [(0,), (0,), (0,)]
                                                colors = [x[0] for x in result]
                                                #code to select what property to build houses on
                                        # mydb.commit()
                elif(index==1):
                        #transfer properties
                        
                        pass
                elif(index==2):
                        #transfer money
                        pass
                elif(index==3):
                        # cursor.execute( "select  ")
                        cursor.execute(f"select id from currentTransaction where type='players_team'")
                        player_id=cursor.fetchone()[0]
                        
                        # Draw a random Chance card
                        chance_cards = [
    "Advance to 'Go' (Collect £200)",
    "Advance to Trafalgar Square",
    "Advance to Pall Mall (If you pass Go, collect £200)",
    "Bank pays you dividend of £50",
    "Get out of Jail Free (This card may be kept until needed or traded)",
    "Go back 3 spaces",
    "Go directly to Jail (Do not pass Go, do not collect £200)",
    "Make general repairs on all your property (For each house pay £25, For each hotel £100)",
    "Pay poor tax of £15",
    "Take a trip to Marylebone Station (If you pass Go, collect £200)",
    "Advance to King's Cross Station (If you pass Go, collect £200)",
    "Advance to Mayfair",
    "You have been elected Chairman of the Board (Pay each player £50)",
    "Your building loan matures (Collect £150)",
    "You have won a crossword competition (Collect £100)",
    "Speeding fine (£15)"
]
                        selected_card = random.choice(chance_cards)
                        # print(f"Chance card drawn: {selected_card}")
                        # Perform actions based on the drawn card
                        if selected_card == "Advance to 'Go' (Collect £200)":
                                # Move player to Go and collect £200
                                cursor.execute(f"update players_team set cash = cash + 200 where id = {player_id}")
                                mydb.commit()
                                
                        elif selected_card == "Bank pays you dividend of £50":
                                cursor.execute(f"update players_team set cash = cash + 50 where id = {player_id}")
                                mydb.commit()
                        elif selected_card == "Pay poor tax of £15" or selected_card =="Speeding fine (£15)":
                                cursor.execute(f"update players_team set cash = cash - 15 where id = {player_id}")
                                mydb.commit()
                                # Move player to Pall Mall and collect £200 if they pass Go
                        elif selected_card =="Your building loan matures (Collect £150)":
                                cursor.execute(f"update players_team set cash = cash + 150 where id = {player_id}")
                                mydb.commit()
                        elif selected_card =="You have won a crossword competition (Collect £100)":
                                cursor.execute(f"update players_team set cash = cash + 100 where id = {player_id}")
                                mydb.commit()
                        elif selected_card =="Make general repairs on all your property (For each house pay £25, For each hotel £100)":
                                cursor.execute(f"select houses,hotel from properties where owner_id = {player_id}")
                                result=cursor.fetchall()
                                money=0
                                for x in result:
                                        money+=25*x[0]+100*x[1]
                                        
                                cursor.execute(f"update players_team set cash = cash - {money} where id = {player_id}")
                                mydb.commit()
                        elif selected_card =="Your building loan matures (Collect £150)":
                                cursor.execute(f"update players_team set cash = cash + 150 where id = {player_id}")
                                mydb.commit()
                        
                        # Add more conditions for other Chance cards
                        else:
                                # Handle other Chance cards
                                pass
                elif(index==4):
                        #community chest card
                        # List of British Monopoly Community Chest cards
                        community_chest_cards = [
    "Advance to 'Go' (Collect £200)",
    "Bank error in your favor (Collect £200)",
    "Doctor's fees (Pay £50)",
    "From sale of stock you get £50",
    "Get Out of Jail Free (This card may be kept until needed or traded)",
    "Go to Jail (Go directly to Jail, do not pass Go, do not collect £200)",
    "Holiday Fund matures (Receive £100)",
    "Income tax refund (Collect £20)",
    "It is your birthday (Collect £10 from each player)",
    "Life insurance matures (Collect £100)",
    "Pay hospital fees of £100",
    "Pay school fees of £150",
    "Receive £25 consultancy fee",
    "You are assessed for street repairs (£40 per house, £115 per hotel)",
    "You have won second prize in a beauty contest (Collect £10)",
    "You inherit £100"
]

# Randomly select a Community Chest card
                        selected_community_card = random.choice(community_chest_cards)
                        

                if selected_community_card == "Advance to 'Go' (Collect £200)":
                        # Move player to Go and collect £200
                        cursor.execute(f"update players_team set cash = cash + 200 where id = {player_id}")

                        
                elif selected_community_card == "Bank error in your favor (Collect £200)":
                        # Collect £200 due to bank error
                        pass
                elif selected_community_card == "Doctor's fees (Pay £50)":
                        # Pay £50 for doctor's fees
                        pass
                # Add more conditions for other Community Chest cards
                else:
                        # Handle other Community Chest cards
                        pass
        


        mydb.close()