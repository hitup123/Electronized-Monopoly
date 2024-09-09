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
                        # cursor.execute(f"select id from currentTransaction where type='properties'")
                        # property_id = cursor.fetchone()
             
                        # cursor.execute(f"select * from properties where id ={property_id[0]}")
                        # property_data = cursor.fetchone()

                        # cursor.execute(f"select id from currentTransaction where type='players'")
                        # player_id = cursor.fetchone()

                        # cursor.execute(f"select team from teams where id={player_id[0]}")
                        # team_id=cursor.fetchone()
   
                        # cursor.execute(f"select * from players where team={team_id[0]}")
                        # player_data = cursor.fetchone()

                        

                        if(property_data[-4]==None):
                                
                                logging.debug("Entered Buy Property")

                                if(PlayerData[cash]>PropertyData[cost]):

                                        cursor.execute(f"update players set cash = cash - {PropertyData[cost]} where team = {PlayerData[team]}")
                                        cursor.execute(f"update properties set owner_id = {PlayerData[team]} where id = {PropertyData[id]}")

                                        str1 = f"team {PlayerData[team]} bought {PropertyData[name]}"
                                        insertLog(txn, 'buy', PlayerData[team], None, PropertyData[cost], str1)
                                        mydb.commit()

                                        logging.debug("Property Bought Successfully")

                                else:
                                        logging.debug("Player does not have enough money to buy the property")
                                        insertLog(txn, 'buyfailed', PlayerData[team], None, 0, f'team{PlayerData[team]} has insufficient funds to buy {PropertyData[name]}')
                                        
                        elif(PropertyData[owner_id]!= PlayerData[team]):
                                
                                logging.debug("Entered  Rent Property")

                                cursor.execute(f"select house from properties where id={PropertyData[id]}")
                                house = cursor.fetchone()[0]

                                cursor.execute(f"select R{house} from properties where id={PropertyData[id]}")
                                rent=cursor.fetchone()[0]

                                if(PropertyData[id] == 8 or  PropertyData[id] == 21):  # Utiliy  Property
                                        rent = handleUtilityRent()
                                elif(PropertyData[id] == 3 or PropertyData[id] == 11 or PropertyData[id] == 18 or PropertyData[id] == 26):
                                        rent = handleRailwayRent()
                                



                                if(0 == house):
                                        cursor.execute(f"select color from properties where  id={PropertyData[id]}")
                                        color = cursor.fetchone()[0]

                                        cursor.execute(f"select owner_id, mortgage from properties where color = '{color}'")
                                        owners = cursor.fetchall()

                                        rent = 2*rent
                                        
                                        for i in owners:
                                                if(i[0] != PropertyData[owner_id] and i[1] == 0):

                                                        rent = rent / 2


                                if PlayerData[cash] >= rent:
                                        cursor.execute(f"update players set cash = cash - {rent} where team = {PlayerData[team]}")
                                        cursor.execute(f"update players set cash = cash + {rent} where team = {PropertyData[owner_id]}")
                                        
                                        insertLog(txn, 'rent', team_id, None, rent, f'team {team_id} paid rent ({rent}) on {PropertyData[name]}')

                                        logging.debug("Rent has been payed")

                                else:
                                        logging.debug("Player cannot pay rent")


                elif(c.PlayerOnChance == currAction):

                        logging.debug("Entered Player on Chance Card")

                        # cursor.execute(f"select id from currentTransaction where type='players'")
                        # player_id=cursor.fetchone()[0]

                        # cursor.execute(f"select * from teams where id={player_id[0]}")
                        # team_id=cursor.fetchone()[0]
                        team_id = PlayerData[team]

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

                        # cursor.execute(f"select id from currentTransaction where type='players'")
                        # player_id=cursor.fetchone()[0]

                        # cursor.execute(f"select * from teams where team={player_id[0]}")
                        # team_id=cursor.fetchone()[0]
                        team_id = PlayerData[team]

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

                        # cursor.execute(f"select id from currentTransaction where type='properties'")
                        # property_id = cursor.fetchone()

                        # cursor.execute(f"select owner_id from properties where id={property_id[0]}")
                        # team_id=cursor.fetchone()[0]

                        # cursor.execute(f"select house from properties where id={property_id[0]}")
                        # property_data = cursor.fetchone()

                        cursor.execute("select house from properties")
                        result=cursor.fetchall()


                        cursor.execute(f"select mortgage from properties where id={property_id[0]}")
                        mortgage = cursor.fetchone()
                        
                        canbuild=True
                        if mortgage:
                                canbuild=False
                        for x in result:
                                sum+=x[0]
                                if sum>=32:
                                        canbuild=False
                        
                        cursor.execute(f"select color from properties where id={PropertyData[id]}")
                        property_color = cursor.fetchone()[0]

                        cursor.execute(f"select * from properties where color='{property_color}'")
                        result=cursor.fetchall()

                        houses=[]
                        for x in result:
                                if(x[-2]!=team_id):
                                        canbuild=False        
                                        houses.append(x[4])
                                
                        if canbuild and min(houses)!=PropertyData[id]:
                                canbuild=False

                        if canbuild:
                                if PropertyData[id]<4:
                                        cursor.execute(f"update properties set house = house + 1 where id = {property_id}")
                                        cursor.execute(f"UPDATE players SET cash = cash - (SELECT houseCost FROM properties WHERE id = {property_id}) WHERE team = (SELECT owner_id FROM properties WHERE id = {property_id})")
                                elif PropertyData[id]==4:
                                        cursor.execute(f"update properties set hotels = hotels + 1 where id = {property_id}")
                                        cursor.execute(f"UPDATE players SET cash = cash - (SELECT houseCost FROM properties WHERE id = {property_id}) WHERE team = (SELECT owner_id FROM properties WHERE id = {property_id})")

        
                elif(c.MortgageProperty == currAction): 

                        logging.debug("Entered  Mortgage Property")                        

                        # cursor.execute(f"select id from currentTransaction where type='properties'")
                        # property_id = cursor.fetchone()[0]
                        # cursor.execute(f"select owner_id from properties where id={property_id}")
                        # team_id=cursor.fetchone()[0]

                        cost =  0.5 * (f"SELECT cost FROM properties WHERE id = {PropertyData[id]}")

                        cursor.execute(f"select mortgage  from properties where id={PropertyData[id]}")
                        mort_status = cursor.fetchone()[0]

                        if(mort_status == 0):

                                cursor.execute(f"update players set cash = cash + {cost} where team = {PlayerData[team]}")
                                cursor.execute(f"update properties set mortgage = 1 where id = {PropertyData[id]}")

                                insertLog(txn, 'mortgage',  property_id, PlayerData[team], cost, f"Property {PropertyData[id]} was Mortgaged by Team {PlayerData[team]}")

                                logging.debug(f" Property {PropertyData[id]} was mortgaged  by Team {PlayerData[team]}")
                        else:
                                cursor.execute(f"update players set cash = cash - {cost*1.1} where team = {PlayerData[team]}")
                                cursor.execute(f"update properties set mortgage = 0 where id = {property_id}")

                                insertLog(txn, 'unmortgage', PlayerData[team], None, cost*1.1,  f"Property {PropertyData[id]} was Unmortgaged by Team {PlayerData[team]}")



                mydb.commit()
        
        else:
                logging.error(" Invalid action")

        
        # Check for Bankrupt

        # cursor.execute(f"select id from currentTransaction where type='players'")
        # player_id = cursor.fetchone()

        # cursor.execute(f"select team from teams where id={player_id[0]}")
        # team_id=cursor.fetchone()

        # cursor.execute(f"select  cash from players where team={team_id}")
        # cash = cursor.fetchone()

        if(PlayerData[cash] < 0):
                logging.debug("Player is Bankrupt")
                insertLog(txn, 'bankrupt',  PlayerData[team], None, cash, f"Team {PlayerData[team]} is Bankrupt. Please sell properties/Houses to pay off debt or Retire from game")
                


        


                        



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
        
      