import random
import mysql.connector

# Connect to the MySQL database

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="monopoly"
)
cursor=mydb.cursor()
# def search_table():
#         # Get user input
#         id = input("Enter the ID: ")

#         # Search the "cards" table using the ID
#         cursor = mydb.cursor()
#         cursor.execute("SELECT type FROM cards WHERE id = %s", (id,))
#         result = cursor.fetchone()
#         # print(result)
#         getType=False
#         if result:
#                 table_name = result[0]
#                 # Search the retrieved table using the ID
#                 cursor.execute(f"SELECT * FROM {table_name} WHERE id = %s", (id,))
#                 result = cursor.fetchone()
#                 if result:
#                         print(f"Found in table {table_name}: {result}")
#                         getType=True
#                 else:
#                         print(f"No record found in table {table_name} for ID {id}")
#         else:
#                 print(f"No record found in the 'cards' table for ID {id}")

#         return id,table_name
def test():
        print("hi")
        cursor.execute(f"select type from currentTransaction")
        result = cursor.fetchall()
        # print(result)
        currAction=[]
        for x in result:

                currAction.append(x[0])
        print(currAction)
        
        cursor.execute("DELETE FROM currenttransaction")
        print("0hi")
        mydb.commit()
        print("hi")
        return
def conditions():
        cursor.execute(f"select type from currentTransaction")
        result = cursor.fetchall()
        # print(result)
        currAction=[]
        for x in result:

                currAction.append(x[0])
        cursor.execute("DELETE FROM currenttransaction")
        print("0hi: ", currAction)
        mydb.commit()
        scan_order=[['properties','players'],['chance','players'] ,['comm','players'],['house','properties'],['mort','properties']]
        actions = [ 'buy/rent',  'chance', 'community chest',  'property/house', 'property/mortgage']

              
        if currAction in scan_order:
                
                index = scan_order.index(currAction)
                print("HI1")
                print(index,actions[index])

                return
                if(index==0):
                        cursor.execute(f"select id from currentTransaction where type='properties'")
                        property_id = cursor.fetchone()
                        cursor.execute(f"select * from properties where id={property_id[0]}")
                        property_data = cursor.fetchone()
                        cursor.execute(f"select id from currentTransaction where type='players'")
                        player_id = cursor.fetchone()
                        cursor.execute(f"select * from teams where id={player_id[0]}")
                        team_id=cursor.fetchone()
                        cursor.execute(f"select * from players where id={team_id[0]}")
                        player_data = cursor.fetchone()
                        if(property_data[len(property_data)-2]=='NULL'):
                                if(player_data[2]>property_data[3]):
                                        cursor.execute(f"update players set cash = cash - {property_data[3]} where id = {team_id[0]}")
                                        cursor.execute(f"update properties set owner_id = {player_data[0]} where id = {property_id[0]}")
                                        # mydb.commit()
                                else:
                                        #make api for telling it failed
                                        print("Insufficient balance")
                        elif(property_data[len(property_data)-2]!=team_id[0]):
                                cursor.execute(f"select house from properties where id={property_id[0]}")
                                house = cursor.fetchone()[0]
                                cursor.execute(f"select R{house} from properties where id={property_id[0]}")
                                rent=cursor.fetchone()[0]
                                if player_data[2] >= rent:
                                        cursor.execute(f"update players set cash = cash - {rent} where id = {team_id[0]}")
                                        cursor.execute(f"update players set cash = cash + {rent} where id = {property_data[len(property_data)-2]}")
                                        # mydb.commit()
                                else:
                                        print("Insufficient balance")
                elif(index==1):
                        cursor.execute(f"select id from currentTransaction where type='players'")
                        player_id=cursor.fetchone()[0]
                        cursor.execute(f"select * from teams where id={player_id[0]}")
                        team_id=cursor.fetchone()[0]
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
                        ]
                        selected_card = random.choice(chance_cards)
                        if selected_card == "Advance to 'Go' (Collect £200)":
                                cursor.execute(f"update players set cash = cash + 200 where id = {team_id}")
                                mydb.commit()
                        elif selected_card == "Bank pays you dividend of £50":
                                cursor.execute(f"update players set cash = cash + 50 where id = {team_id}")
                                mydb.commit()
                        elif selected_card == "Pay poor tax of £15" or selected_card =="Speeding fine (£15)":
                                cursor.execute(f"update players set cash = cash - 15 where id = {team_id}")
                                mydb.commit()
                        elif selected_card =="Your building loan matures (Collect £150)":
                                cursor.execute(f"update players set cash = cash + 150 where id = {team_id}")
                                mydb.commit()
                        elif selected_card =="You have won a crossword competition (Collect £100)":
                                cursor.execute(f"update players set cash = cash + 100 where id = {team_id}")
                                mydb.commit()
                        elif selected_card =="Make general repairs on all your property (For each house pay £25, For each hotel £100)":
                                cursor.execute(f"select houses,hotel from properties where owner_id = {team_id}")
                                result=cursor.fetchall()
                                money=0
                                for x in result:
                                        money += (x[0] * 25) + (x[1] * 100)
                                if player_data[2] >= money:
                                        cursor.execute(f"update players set cash = cash - {money} where id = {team_id}")
                                        mydb.commit()
                                else:
                                        print("Insufficient balance")
                        elif selected_card =="Your building loan matures (Collect £150)":
                                cursor.execute(f"update players set cash = cash + 150 where id = {team_id}")
                                mydb.commit()
        
                elif(index==2):
                        #community chest card
                        # List of British Monopoly Community Chest cards
                        cursor.execute(f"select id from currentTransaction where type='players'")
                        player_id=cursor.fetchone()[0]
                        cursor.execute(f"select * from teams where id={player_id[0]}")
                        team_id=cursor.fetchone()[0]
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
                                cursor.execute(f"update players set cash = cash + 200 where id = {team_id}")
                        elif selected_community_card == "Bank error in your favor (Collect £200)":
                                cursor.execute(f"update players set cash = cash + 200 where id = {team_id}")
                        elif selected_community_card == "Doctor's fees (Pay £50)":
                                cursor.execute(f"update players set cash = cash - 50 where id = {team_id}")
                        elif selected_community_card == "From sale of stock you get £50":
                                cursor.execute(f"update players set cash = cash + 50 where id = {team_id}")
                        elif selected_community_card == "Get Out of Jail Free (This card may be kept until needed or traded)":
                                cursor.execute(f"update players set get_out_of_jail_free = get_out_of_jail_free + 1 where id = {team_id}")
                        elif selected_community_card == "Go to Jail (Go directly to Jail, do not pass Go, do not collect £200)":
                                cursor.execute(f"update players set in_jail = 1 where id = {team_id}")
                        elif selected_community_card == "Holiday Fund matures (Receive £100)":
                                if player_data[2] >= 100:
                                                cursor.execute(f"update players set cash = cash + 100 where id = {team_id}")
                                                mydb.commit()
                                else:
                                                print("Insufficient balance")
                                cursor.execute(f"update players set cash = cash + 100 where id = {team_id}")
                        elif selected_community_card == "Income tax refund (Collect £20)":
                                cursor.execute(f"update players set cash = cash + 20 where id = {team_id}")
                        elif selected_community_card == "It is your birthday (Collect £10 from each player)":
                                cursor.execute("select id from players")
                                all_player_ids = cursor.fetchall()
                                for pid in all_player_ids:
                                        cursor.execute(f"update players set cash = cash - 10 where id = {pid[0]}")      
                                cursor.execute(f"update players set cash = cash + {10 * len(all_player_ids)} where id = {player_id}")
                        elif selected_community_card == "Life insurance matures (Collect £100)":
                                cursor.execute(f"update players set cash = cash + 100 where id = {player_id}")
                        elif selected_community_card == "Pay hospital fees of £100":
                                cursor.execute(f"update players set cash = cash - 100 where id = {team_id}")
                        elif selected_community_card == "Pay school fees of £150":
                                cursor.execute(f"update players set cash = cash - 150 where id = {team_id}")
                        elif selected_community_card == "Receive £25 consultancy fee":
                                cursor.execute(f"update players set cash = cash + 25 where id = {team_id}")
                        elif selected_community_card == "You are assessed for street repairs (£40 per house, £115 per hotel)":
                                cursor.execute(f"select house, hotels from properties where owner_id = {team_id}")
                                result = cursor.fetchall()
                                repair_cost = 40 * sum([x[0] for x in result]) + 115 * sum([x[1] for x in result])
                                cursor.execute(f"update players set cash = cash - {repair_cost} where id = {team_id}")
                        elif selected_community_card == "You have won second prize in a beauty contest (Collect £10)":
                                cursor.execute(f"update players set cash = cash + 10 where id = {team_id}")
                        elif selected_community_card == "You inherit £100":
                                cursor.execute(f"update players set cash = cash + 100 where id = {team_id}")
                elif(index==3):
                        cursor.execute(f"select id from currentTransaction where type='properties'")
                        property_id = cursor.fetchone()
                        cursor.execute(f"select owner_id from properties where id={property_id[0]}")
                        team_id=cursor.fetchone()[0]
                        cursor.execute(f"select house from properties where id={property_id[0]}")
                        property_data = cursor.fetchone()
                        cursor.execute("select house from properties")
                        result=cursor.fetchall()
                        canbuild=True
                        for x in result:
                                sum+=x[0]
                                if sum>=32:
                                        canbuild=False
                        
                        cursor.execute(f"select color from properties where id={property_id[0]}")
                        property_color = cursor.fetchall()[0]
                        cursor.execute(f"select * from properties where color='{property_color[0]}'")
                        result=cursor.fetchall()
                        houses=[]
                        for x in result:
                                if(x[-2]!=team_id):
                                        canbuild=False        
                                        houses.append(x[4])
                                
                        if canbuild and min(houses)!=property_data[0]:
                                canbuild=False

                        if canbuild:
                                if property_data[0]<4:
                                        cursor.execute(f"update properties set house = house + 1 where id = {property_id}")
                                        cursor.execute(f"UPDATE players SET cash = cash - (SELECT houseCost FROM properties WHERE id = {property_id}) WHERE team = (SELECT owner_id FROM properties WHERE id = {property_id})")
                                elif property_data[0]==4:
                                        cursor.execute(f"update properties set hotels = hotels + 1 where id = {property_id}")
                                        cursor.execute(f"UPDATE players SET cash = cash - (SELECT houseCost FROM properties WHERE id = {property_id}) WHERE team = (SELECT owner_id FROM properties WHERE id = {property_id})")

        
                if index==4: 
                        cursor.execute(f"select id from currentTransaction where type='properties'")
                        property_id = cursor.fetchone()[0]
                        cursor.execute(f"select owner_id from properties where id={property_id[0]}")
                        team_id=cursor.fetchone()[0]
                        cursor.execute()
                        


        mydb.commit()


if __name__ == "__main__":
        
        # id,table_name = search_table()
        
        # print(f"ID: {id}, Table: {table_name}")
        # cursor.execute(f"insert into currentTransaction (id,type) values({id},'{table_name}')")
        # mydb.commit()
        # cursor.execute("SELECT type FROM cards WHERE id = %s", (id,))
        # result = cursor.fetchone()v
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
        
      