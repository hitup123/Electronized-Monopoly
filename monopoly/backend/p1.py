# Imports 
import random
import Constants as c
from dbConnector import getFromDB, FetchTypes
import logging

# Logging Config
logging.basicConfig(filename='SessionLog.log', level=logging.DEBUG, format='%(asctime)s - (%(levelname)s) :   %(message)s', datefmt='%H : %M : %S')


# Connect to the MySQL database
from dbConnector import dbconnect
mydb=dbconnect()
cursor=mydb.cursor()

# Function to Insert Log into Log Table 
def insertLog(count, action , team1,team2, money, msg ):
        cursor.execute(f"insert into log values ({count}, '{action}', '{team1}','{team2}', {money}, '{msg}' )")

def handleUtilityRent():
        # Need to have an API to get number of spaces moved from frontend
        return 100

def handleRailwayRent(owner_id):

        cursor.execute(f"select owner_id from properties where color='Railroad'")
        owners = cursor.fetchall()

        mul = 1
        for i in  owners:
                if(i[0] == owner_id):
                        mul = mul*2
        
        rent  = 25 * mul

        return rent
        
##### Defining Columns for Properties ######
id = 0
name = 1
color = 2
cost = 3
house = 4
R0 = 5
R1 = 6
R2 = 7
R3 = 8
R4 = 9
R5 = 10
owner_id = 11
houses = 12
hotels = 13
mortgaged = 14
###############################################



#### Defining Columns for  Players ######
cash = 0
in_jail = 1
jail_free_cards = 2
propertiesOwned = 3
bankrupt = 4
team = 5
################################################




def conditions():

        logging.info("  This is p1.py File LOG  ")

        cursor.execute(f"select type from currentTransaction")
        result = cursor.fetchall()

        result = getFromDB(f"select type from currentTransaction")
        currAction=[]
        for x in result:
                currAction.append(x[0])



              
        if currAction in c.Actions:
                
                cursor.execute(f"select MAX(txn_order) from log")
                temp = cursor.fetchone()

                if(len(temp) == 0):
                        txn = 1
                else:
                        txn = temp[0] + 1

                cursor.execute(f"select type  from currentTransaction")
                types  = cursor.fetchall()
                type_values = [t[0] for t in types]

                PropertyData = ()
                PlayerData = ()

                if 'properties' in  type_values:
                        cursor.execute(f"select id from currentTransaction where type='properties'")
                        property_id = cursor.fetchone()
                        cursor.execute(f"select * from properties where id ={property_id[0]}")

                        PropertyData = cursor.fetchone()
                
                if 'players' in  type_values:
                        cursor.execute(f"select id from currentTransaction where type='players'")
                        player_id = cursor.fetchone()
                        cursor.execute(f"select * from players where id ={player_id[0]}")

                        PlayerData = cursor.fetchone()





                if(c.PlayerOnProperty == currAction):
                        logging.debug("Entered  PlayerOnProperty")

                        #Fetching Data from Database                        
                        cursor.execute(f"select id from currentTransaction where type='properties'")
                        property_id = cursor.fetchone()
             
                        cursor.execute(f"select * from properties where id ={property_id[0]}")
                        property_data = cursor.fetchone()

                        cursor.execute(f"select id from currentTransaction where type='players'")
                        player_id = cursor.fetchone()

                        cursor.execute(f"select team from teams where id={player_id[0]}")
                        team_id=cursor.fetchone()
   
                        cursor.execute(f"select * from players where team={team_id[0]}")
                        player_data = cursor.fetchone()

                        

                        if(property_data[-4]==None):
                                
                                logging.debug("Entered Buy Property")

                                if(player_data[0]>property_data[3]):

                                        cursor.execute(f"update players set cash = cash - {property_data[3]} where team = {team_id[0]}")
                                        cursor.execute(f"update properties set owner_id = {team_id[0]} where id = {property_id[0]}")

                                        str1 = f"team{team_id} bought {property_data[1]}"
                                        insertLog(txn, 'buy', team_id, None, property_data[3], str1)
                                        mydb.commit()

                                        logging.debug("Property Bought Successfully")

                                else:
                                        logging.debug("Player does not have enough money to buy the property")
                                        insertLog(txn, 'buyfailed', team_id, None, 0, f'team{team_id} has insufficient funds to buy {property_data[1]}')
                                        
                        elif(property_data[-4]!=team_id[0]):
                                
                                logging.debug("Entered  Rent Property")

                                cursor.execute(f"select house from properties where id={property_id[0]}")
                                house = cursor.fetchone()[0]

                                cursor.execute(f"select R{house} from properties where id={property_id[0]}")
                                rent=cursor.fetchone()[0]

                                if(property_id[0] == 8 or  property_id[0] == 21):  # Utiliy  Property
                                        rent = handleUtilityRent()
                                elif(property_id[0] == 3 or property_id[0] == 11 or property_id[0] == 18 or property_id[0] == 26):
                                        rent = handleRailwayRent()
                                



                                if(0 == house):
                                        cursor.execute(f"select color from properties where  id={property_id[0]}")
                                        color = cursor.fetchone()[0]

                                        cursor.execute(f"select owner_id, mortgage from properties where color = '{color}'")
                                        owners = cursor.fetchall()

                                        rent = 2*rent
                                        
                                        for i in owners:
                                                if(i[0] != property_data[-4] and i[1] == 0):

                                                        rent = rent / 2


                                if player_data[0] >= rent:
                                        cursor.execute(f"update players set cash = cash - {rent} where team = {team_id[0]}")
                                        cursor.execute(f"update players set cash = cash + {rent} where team = {property_data[-4]}")
                                        
                                        insertLog(txn, 'rent', team_id, None, rent, f'team {team_id} paid rent ({rent}) on {property_data[1]}')

                                        logging.debug("Rent has been payed")

                                else:
                                        logging.debug("Player cannot pay rent")


                elif(c.PlayerOnChance == currAction):

                        logging.debug("Entered Player on Chance Card")

                        cursor.execute(f"select id from currentTransaction where type='players'")
                        player_id=cursor.fetchone()[0]

                        cursor.execute(f"select * from teams where id={player_id[0]}")
                        team_id=cursor.fetchone()[0]

                        moneys =  cursor.execute(f"select cash from players where team = {team_id}")

                             
                        chance_cards = [
                                ["Advance to 'Go' (Collect £200)",'''cursor.execute(f"update players set cash = cash + 200 where team = {team_id}")'''],

                                ["Advance to Trafalgar Square", ""],

                                ["Advance to Pall Mall (If you pass Go, collect £200)", ""],

                                ["Bank pays you dividend of £50", '''cursor.execute(f"update players set cash = cash + 50 where team = {team_id}")'''],

                                ["Get out of Jail Free (This card may be kept until needed or traded)", '''cursor.execute(f"update players set jail_free_cards = jail_free_cards + 1 where team = {team_id}")'''],

                                ["Go back 3 spaces",""],
                                
                                ["Go directly to Jail (Do not pass Go, do not collect £200)", '''cursor.execute(f"update players set in_jail = b'1' where team = {team_id}")'''],

                                ["Make general repairs on all your property (For each house pay £25, For each hotel £100)", '''cursor.execute(f"select houses,hotel from properties where owner_id = {team_id}")
                                result=cursor.fetchall()
                                money=0
                                for x in result:
                                        money += (x[0] * 25) + (x[1] * 100)
                                if player_data[2] >= money:
                                        cursor.execute(f"update players set cash = cash - {money} where team = {team_id}")
                                        mydb.commit()'''],

                                ["Pay poor tax of £15", '''cursor.execute(f"update players set cash = cash - 15 where team = {team_id}")'''],

                                ["Take a trip to Marylebone Station (If you pass Go, collect £200)", ""],

                                ["Advance to King's Cross Station (If you pass Go, collect £200)", ""],

                                ["Advance to Mayfair", ""],

                                ["You have been elected Chairman of the Board (Pay each player £50)", '''cursor.execute(f"update players set cash = cash - 50 where team = {team_id}")
                                 cursor.execute(f"update players set cash = cash + 50 where team <> {team_id}") '''],

                                ["Your building loan matures (Collect £150)", '''cursor.execute(f"update players set cash = cash + 150 where team = {team_id}")'''],

                                ["You have won a crossword competition (Collect £100)", '''cursor.execute(f"update players set cash = cash + 100 where id = {team_id}")''']
                        ]
                        selected_card = random.choice(chance_cards)

                        exec(selected_card[1])

                        moneys = moneys - cursor.execute(f"select cash from players where team = {team_id}")

                        insertLog(txn, 'chance', team_id, None, moneys, selected_card[0])

                        logging.debug("Chance Card \" %s \" was executed,\n Code: %s ",  selected_card[0],  selected_card[1])





                elif(c.PlayerOnCommunity == currAction):
                        
                        logging.debug("Entered Player on Community Chest Card")

                        cursor.execute(f"select id from currentTransaction where type='players'")
                        player_id=cursor.fetchone()[0]

                        cursor.execute(f"select * from teams where team={player_id[0]}")
                        team_id=cursor.fetchone()[0]

                        moneys = cursor.execute(f"select cash from players where team = {team_id}")
                        
                        community_chest_cards = [
                                ["Advance to 'Go' (Collect £200)", ""],

                                ["Bank error in your favor (Collect £200)", '''cursor.execute(f"update players set cash = cash + 200 where team = {team_id}")'''],

                                ["Doctor's fees (Pay £50)", '''cursor.execute(f"update players set cash = cash - 50 where team = {team_id}")'''],

                                ["From sale of stock you get £50", '''cursor.execute(f"update players set cash = cash + 50 where team = {team_id}")'''],

                                ["Get Out of Jail Free (This card may be kept until needed or traded)", '''cursor.execute(f"update players set jail_free_cards = jail_free_cards + 1 where id = {team_id}")'''],

                                ["Go to Jail (Go directly to Jail, do not pass Go, do not collect £200)", '''cursor.execute(f"update players set in_jail = b'1' where id = {team_id}")'''],

                                ["Holiday Fund matures (Receive £100)", '''cursor.execute(f"update players set cash = cash + 100 where team = {team_id}")'''],

                                ["Income tax refund (Collect £20)", '''cursor.execute(f"update players set cash = cash + 20 where team = {team_id}")'''],

                                ["It is your birthday (Collect £10 from each player)", '''cursor.execute("select team from players")
                                    all_player_ids = cursor.fetchall()
                                    for pid in all_player_ids:
                                        cursor.execute(f"update players set cash = cash - 10 where team = {pid[0]}")
                                    cursor.execute(f"update players set cash = cash + {10 * len(all_player_ids)} where team = {team_id}")'''],

                                ["Life insurance matures (Collect £100)", '''cursor.execute(f"update players set cash = cash + 100 where team = {team_id}")'''],

                                ["Pay hospital fees of £100", '''cursor.execute(f"update players set cash = cash - 100 where team = {team_id}")'''],

                                ["Pay school fees of £150", '''cursor.execute(f"update players set cash = cash - 150 where team = {team_id}")'''],

                                ["Receive £25 consultancy fee", '''cursor.execute(f"update players set cash = cash + 25 where team = {team_id}")'''],

                                ["You are assessed for street repairs (£40 per house, £115 per hotel)", '''cursor.execute(f"select house, hotels from properties where owner_id = {team_id}")
                                    result = cursor.fetchall()
                                    repair_cost = 40 * sum([x[0] for x in result]) + 115 * sum([x[1] for x in result])
                                    cursor.execute(f"update players set cash = cash - {repair_cost} where team = {team_id}")'''],

                                ["You have won second prize in a beauty contest (Collect £10)", '''cursor.execute(f"update players set cash = cash + 10 where team = {team_id}")'''],

                                ["You inherit £100", '''cursor.execute(f"update players set cash = cash + 100 where team = {team_id}")''']
                        ]

                        # Randomly select a Community Chest card
                        selected_card = random.choice(community_chest_cards)

                        exec(selected_card[1])

                        moneys = moneys - cursor.execute(f"select cash from players where team = {team_id}")

                        insertLog(txn, 'community', team_id, None, moneys, selected_card[0])

                        logging.debug("Community Card \" %s \" was executed,\n Code: %s ",  selected_card[0],  selected_card[1])


                elif(c.HouseOnProperty == currAction):

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

        
                elif(c.MortgageProperty == currAction): 

                        logging.debug("Entered  Mortgage Property")                        

                        cursor.execute(f"select id from currentTransaction where type='properties'")
                        property_id = cursor.fetchone()[0]
                        cursor.execute(f"select owner_id from properties where id={property_id}")
                        team_id=cursor.fetchone()[0]

                        cost =  0.5 * (f"SELECT cost FROM properties WHERE id = {property_id}")

                        cursor.execute(f"select mortgage  from properties where id={property_id}")
                        mort_status = cursor.fetchone()[0]

                        if(mort_status == 0):

                                cursor.execute(f"update players set cash = cash + {cost} where team = {team_id}")
                                cursor.execute(f"update properties set mortgage = 1 where id = {property_id}")

                                insertLog(txn, 'mortgage',  property_id, team_id, cost, f"Property {property_id} was Mortgaged by Team {team_id}")

                                logging.debug(f" Property {property_id} was mortgaged  by Team {team_id}")
                        else:
                                cursor.execute(f"update players set cash = cash - {cost*1.1} where team = {team_id}")
                                cursor.execute(f"update properties set mortgage = 0 where id = {property_id}")

                                insertLog(txn, 'unmortgage', team_id, None, cost*1.1,  f"Property {property_id} was Unmortgaged by Team {team_id}")



                mydb.commit()
        
        else:
                logging.error(" Invalid action")

        
        # Check for Bankrupt
        cursor.execute(f"select id from currentTransaction where type='players'")
        player_id = cursor.fetchone()

        cursor.execute(f"select team from teams where id={player_id[0]}")
        team_id=cursor.fetchone()

        cursor.execute(f"select  cash from players where team={team_id}")
        cash = cursor.fetchone()

        if(cash < 0):
                logging.debug("Player is Bankrupt")
                insertLog(txn, 'bankrupt',  player_id, team_id, cash, f"Team {team_id} is Bankrupt. Please sell properties/Houses to pay off debt or Retire from game")
                


        


                        



if __name__ == "__main__":
        
        cursor.execute(f"select type from currentTransaction")
        result = cursor.fetchall()
        # print(result)
        currAction=[]
        for x in result:

                currAction.append(x[0])
        print(currAction) 

        # conditions()
         
        # Close the database connection
        
      