# Imports 
import random
import Constants as c
# from  dbConnector import getFromDB, FetchTypes
from dbConnector import dbconnect
import logging

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Logging Config
logging.basicConfig(filename='SessionLog.log', level=logging.DEBUG, format='%(asctime)s - (%(levelname)s) :   %(message)s', datefmt='%H : %M : %S')


# Connect to the MySQL database
# from dbConnector import dbconnect
import asyncio
mydb=dbconnect()
cursor=mydb.cursor()
idk=0
from flask import Blueprint, jsonify, request
import time
# bp = Blueprint('p1', __name__)
# @bp.route('/api/input', methods=['POST'])
# def input():
#         data=request.json
#         global idk
#         idk=data
#         print("input data: ",data)

#         tempfunc(data)
#         return jsonify({"received_data": data, "message": "POST request received!"})
async def handleUtilityRent():
        data = await asyncio.wait_for(input(), timeout=10000)
        return (data)
def insertLog(count, action , team1,team2, money, msg ):
        cursor.execute(f"insert into log values ({count}, '{action}', '{team1}','{team2}', {money}, '{msg}' )")

def handleRailwayRent(owner_id):

        cursor.execute(f"select owner_id from properties where color='Railroad'")
        owners = cursor.fetchall()#[(4,),(4,),(None,),(None,)]
        print(owners)
        mul = 0.5
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
houseCost = 12
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


def test():
        print("gi")

def conditions():
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
        houseCost = 12
        hotels = 13
        mortgaged = 14

        cash = 0
        in_jail = 1
        jail_free_cards = 2
        propertiesOwned = 3
        bankrupt = 4
        team = 5
        # logging.info("  This is p1.py File LOG  ")
        print("hi")
        cursor.execute(f"select type from currentTransaction")
        result = cursor.fetchall()

        # result = getFromDB(f"select type from currentTransaction")
        cursor.execute(f"select type from currentTransaction")
        result = cursor.fetchall()
        currAction=[]
        
        for x in result:
                currAction.append(x[0])


        print("hi out")
        print(currAction)
        if currAction in c.Actions:
                print("hi in actions")
                cursor.execute(f"select MAX(txn_order) from log")
                temp = cursor.fetchone()
                print(temp)
                if(len(temp) == 0 or temp[0]==None):
                        txn = 1
                else:
                        txn = temp[0] + 1
                # print("passed")
                cursor.execute(f"select type  from currentTransaction")
                types  = cursor.fetchall()
                type_values = [t[0] for t in types]
                print(type_values)
                PropertyData = ()
                PlayerData = ()

                if 'properties' in  type_values:
                        cursor.execute(f"select id from currentTransaction where type='properties'")
                        property_id = cursor.fetchone()
                        cursor.execute(f"select * from properties where id ={property_id[0]}")

                        PropertyData = cursor.fetchone()
                print("passes properties")
                if 'players' in  type_values:
                        cursor.execute(f"select id from currentTransaction where type='players'")
                        player_id = cursor.fetchone()
                        cursor.execute(f"select team from teams where id ={player_id[0]}")
                        team_id= cursor.fetchone()
                        print(team_id)
                        cursor.execute(f"select * from players where team ={team_id[0]}")
                        PlayerData = cursor.fetchone()

                print("passes players",PlayerData)
                
                print("x")




                if(c.PlayerOnProperty == currAction):
                        logging.debug("Entered  PlayerOnProperty")
                        print("player on property")
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

                        

                        if(PropertyData[owner_id]==None):
                                print("buy property")
                                
                                logging.debug("Entered Buy Property")
                                print(cost)
                                if(PlayerData[cash]>PropertyData[cost]):

                                        cursor.execute(f"update players set cash = cash - {PropertyData[cost]} where team = {PlayerData[team]}")
                                        cursor.execute(f"update properties set owner_id = {PlayerData[team]} where id = {PropertyData[id]}")

                                        str1 = f"team {PlayerData[team]} bought {PropertyData[name]}"
                                        insertLog(txn, 'buy', PlayerData[team], None, PropertyData[cost], str1)
                                        mydb.commit()
                                        cursor.execute(f"SELECT propertiesOwned FROM players WHERE team = {PlayerData[team]} ")
                                        result=cursor.fetchone()
                                        print("Properties Owned: ",result)
                                        if(result[0]!=None):
                                                s=result[0]+"_"+PropertyData[name]
                                        else:
                                                s=PropertyData[name]
                                        cursor.execute(f"""
                                        UPDATE players 
                                        SET propertiesOwned ='{s}'
                                        WHERE team = {PlayerData[team]}
                                        """)
                                        # cursor.execute(f"update players set propertiesOwned='(select propertiesOwned from players where team={team_id})|| \' \' ||{PropertyData[name]}' where team={team_id} )")
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
                                # rent=1
                                if(PropertyData[id] == 8 or  PropertyData[id] == 21):  # Utiliy  Property
                                        cursor.execute(f"insert into flags values('util')")
                                        mydb.commit()
                                        print("flag planted")
                                        time.sleep(100)
                                        return
                                        # print(idk)
                                        # spaces=0
                                        # spaces = await handleUtilityRent()
                                        # cursor.execute(f"select owner_id from properties where color='Utility'")
                                        # owners = cursor.fetchall()
                                        # if owners[0][0]==owners[1][0]:
                                        #         rent = 10*spaces
                                        # else:
                                        #         rent = 4 * spaces
                                        rent=idk
                                        if(rent==0):
                                                print("rent is 0")
                                        
                                elif(PropertyData[id] == 3 or PropertyData[id] == 11 or PropertyData[id] == 18 or PropertyData[id] == 26):
                                        rent = handleRailwayRent(PropertyData[owner_id])


                                if(0 == house):
                                        cursor.execute(f"select color from properties where  id={PropertyData[id]}")
                                        color = cursor.fetchone()[0]

                                        cursor.execute(f"select owner_id, mortgage from properties where color = '{color}'")
                                        owners = cursor.fetchall()

                                        rent = 2*rent
                                        
                                        for i in owners:
                                                if(i[0] != PropertyData[owner_id] and i[1] == 0):
                                                        print("not all props owned ", rent)
                                                        rent = rent / 2
                                                        break

                                if PlayerData[cash] >= rent:
                                        cursor.execute(f"update players set cash = cash - {rent} where team = {PlayerData[team]}")
                                        cursor.execute(f"update players set cash = cash + {rent} where team = {PropertyData[owner_id]}")
                                        
                                        insertLog(txn, 'rent', team_id, None, rent, f'team {team_id} paid rent ({rent}) on {PropertyData[name]}')

                                        logging.debug("Rent has been payed")

                                else:
                                        logging.debug("Player cannot pay rent")


                elif(c.PlayerOnChance == currAction):

                        logging.debug("Entered Player on Chance Card")
                        print("ENtered")
                        # cursor.execute(f"select id from currentTransaction where type='players'")
                        # player_id=cursor.fetchone()[0]

                        # cursor.execute(f"select * from teams where id={player_id[0]}")
                        # team_id=cursor.fetchone()[0]
                        cursor.execute("select count(*) from teams")
                        num_teams=cursor.fetchone()[0]
                        team_id = PlayerData[team]
                        print(team_id)
                        cursor.execute(f"select cash from players where team = {team_id}")
                        # print(moneys)
                        moneys =  cursor.fetchone()[0]  
                        print(moneys)
                        # chance_cards = [
                        #         ["Advance to 'Go' (Collect £200)",'''cursor.execute(f"update players set cash = cash + 200 where team = {team_id}")'''],

                        #         ["Advance to Trafalgar Square", ""],

                        #         ["Advance to Pall Mall (If you pass Go, collect £200)", ""],

                        #         ["Bank pays you dividend of £50", '''cursor.execute(f"update players set cash = cash + 50 where team = {team_id}")'''],

                        #         ["Get out of Jail Free (This card may be kept until needed or traded)", '''cursor.execute(f"update players set jail_free_cards = jail_free_cards + 1 where team = {team_id}")'''],

                        #         ["Go back 3 spaces",""],
                                
                        #         ["Go directly to Jail (Do not pass Go, do not collect £200)", '''cursor.execute(f"update players set in_jail = b'1' where team = {team_id}")'''],

                        #         ["Make general repairs on all your property (For each house pay £25, For each hotel £100)", '''cursor.execute(f"select houses,hotel from properties where owner_id = {team_id}")
                        #         result=cursor.fetchall()
                        #         money=0
                        #         for x in result:
                        #                 money += (x[0] * 25) + (x[1] * 100)
                        #         if player_data[2] >= money:
                        #                 cursor.execute(f"update players set cash = cash - {money} where team = {team_id}")
                        #                 mydb.commit()'''],

                        #         ["Pay poor tax of £15", '''cursor.execute(f"update players set cash = cash - 15 where team = {team_id}")'''],

                        #         ["Take a trip to Marylebone Station (If you pass Go, collect £200)", ""],

                        #         ["Advance to King's Cross Station (If you pass Go, collect £200)", ""],

                        #         ["Advance to Mayfair", ""],

                        #         ["You have been elected Chairman of the Board (Pay each player £50)", '''cursor.execute(f"update players set cash = cash - 50*{num_teams} where team = {team_id}")
                        #          cursor.execute(f"update players set cash = cash + 50 where team <> {team_id}") '''],

                        #         ["Your building loan matures (Collect £150)", '''cursor.execute(f"update players set cash = cash + 150 where team = {team_id}")'''],

                        #         ["You have won a crossword competition (Collect £100)", '''cursor.execute(f"update players set cash = cash + 100 where id = {team_id}")''']
                        # ]
                        # selected_card = random.choice(chance_cards)
                        # print("before exec",selected_card[1])
                        # exec(selected_card[1])
                        # print("after exec")

                        choice = random.randint(1, 15)

                        chance_msg = ""

                        if choice == 1:
                                chance_msg = "Advance to 'Go' (Collect £200)"
                                cursor.execute(f"update players set cash = cash + 200 where team = {team_id}")

                        elif choice == 2:
                                chance_msg = "Advance to Trafalgar Square"

                        elif choice == 3:
                                chance_msg = "Advance to Pall Mall (If you pass Go, collect £200)"

                        elif choice == 4:
                                chance_msg = "Bank pays you dividend of £50"
                                cursor.execute(f"update players set cash = cash + 50 where team = {team_id}")

                        elif choice == 5:
                                chance_msg = "Get out of Jail Free (This card may be kept until needed or traded)"
                                cursor.execute(f"update players set jail_free_cards = jail_free_cards + 1 where team = {team_id}")

                        elif choice == 6:
                                chance_msg = "Go back 3 spaces"

                        elif choice == 7:
                                chance_msg = "Go directly to Jail (Do not pass Go, do not collect £200)"
                                cursor.execute(f"update players set in_jail = 1 where team = {team_id}")

                        elif choice == 8:
                                chance_msg = "Make general repairs on all your property (For each house pay £25, For each hotel £100)"
                                cursor.execute(f"select houses, hotel from properties where owner_id = {team_id}")
                                result = cursor.fetchall()
                                money = 0
                                for x in result:
                                        money += (x[0] * 25) + (x[1] * 100)
                                cursor.execute(f"update players set cash = cash - {money} where team = {team_id}")
                                mydb.commit()

                        elif choice == 9:
                                chance_msg = "Pay poor tax of £15"
                                cursor.execute(f"update players set cash = cash - 15 where team = {team_id}")

                        elif choice == 10:
                                chance_msg = "Take a trip to Marylebone Station (If you pass Go, collect £200)"

                        elif choice == 11:
                                chance_msg = "Advance to King's Cross Station (If you pass Go, collect £200)"

                        elif choice == 12:
                                chance_msg = "Advance to Mayfair"

                        elif choice == 13:
                                chance_msg = "You have been elected Chairman of the Board (Pay each player £50)"
                                cursor.execute(f"update players set cash = cash - 50 * {num_teams} where team = {team_id}")
                                cursor.execute(f"update players set cash = cash + 50 where team <> {team_id}")

                        elif choice == 14:
                                chance_msg = "Your building loan matures (Collect £150)"
                                cursor.execute(f"update players set cash = cash + 150 where team = {team_id}")

                        elif choice == 15:
                                chance_msg = "You have won a crossword competition (Collect £100)"
                                cursor.execute(f"update players set cash = cash + 100 where team = {team_id}")

                        cursor.execute(f"select cash from players where team = {team_id}")
                        res=cursor.fetchone()[0]
                        moneys=moneys-res
                        insertLog(txn, 'chance', team_id, None, moneys, chance_msg)

                        logging.debug("Chance Card \" %s \" was executed,\n Code: %s ",  chance_msg,  chance_msg)





                elif(c.PlayerOnCommunity == currAction):
                        
                        logging.debug("Entered Player on Community Chest Card")

                        # cursor.execute(f"select id from currentTransaction where type='players'")
                        # player_id=cursor.fetchone()[0]

                        # cursor.execute(f"select * from teams where team={player_id[0]}")
                        # team_id=cursor.fetchone()[0]
                        team_id = PlayerData[team]

                        cursor.execute(f"select cash from players where team = {team_id}")
                        moneys = cursor.fetchone()[0]
                        
                        # community_chest_cards = [
                        #         ["Advance to 'Go' (Collect £200)", ""],

                        #         ["Bank error in your favor (Collect £200)", '''cursor.execute(f"update players set cash = cash + 200 where team = {team_id}")'''],

                        #         ["Doctor's fees (Pay £50)", '''cursor.execute(f"update players set cash = cash - 50 where team = {team_id}")'''],

                        #         ["From sale of stock you get £50", '''cursor.execute(f"update players set cash = cash + 50 where team = {team_id}")'''],

                        #         ["Get Out of Jail Free (This card may be kept until needed or traded)", '''cursor.execute(f"update players set jail_free_cards = jail_free_cards + 1 where id = {team_id}")'''],

                        #         ["Go to Jail (Go directly to Jail, do not pass Go, do not collect £200)", '''cursor.execute(f"update players set in_jail = b'1' where id = {team_id}")'''],

                        #         ["Holiday Fund matures (Receive £100)", '''cursor.execute(f"update players set cash = cash + 100 where team = {team_id}")'''],

                        #         ["Income tax refund (Collect £20)", '''cursor.execute(f"update players set cash = cash + 20 where team = {team_id}")'''],

                        #         ["It is your birthday (Collect £10 from each player)", '''cursor.execute("select team from players")
                        #             all_player_ids = cursor.fetchall()
                        #             for pid in all_player_ids:
                        #                 cursor.execute(f"update players set cash = cash - 10 where team = {pid[0]}")
                        #             cursor.execute(f"update players set cash = cash + {10 * len(all_player_ids)} where team = {team_id}")'''],

                        #         ["Life insurance matures (Collect £100)", '''cursor.execute(f"update players set cash = cash + 100 where team = {team_id}")'''],

                        #         ["Pay hospital fees of £100", '''cursor.execute(f"update players set cash = cash - 100 where team = {team_id}")'''],

                        #         ["Pay school fees of £150", '''cursor.execute(f"update players set cash = cash - 150 where team = {team_id}")'''],

                        #         ["Receive £25 consultancy fee", '''cursor.execute(f"update players set cash = cash + 25 where team = {team_id}")'''],

                        #         ["You are assessed for street repairs (£40 per house, £115 per hotel)", '''cursor.execute(f"select house, hotels from properties where owner_id = {team_id}")
                        #             result = cursor.fetchall()
                        #             repair_cost = 40 * sum([x[0] for x in result]) + 115 * sum([x[1] for x in result])
                        #             cursor.execute(f"update players set cash = cash - {repair_cost} where team = {team_id}")'''],

                        #         ["You have won second prize in a beauty contest (Collect £10)", '''cursor.execute(f"update players set cash = cash + 10 where team = {team_id}")'''],

                        #         ["You inherit £100", '''cursor.execute(f"update players set cash = cash + 100 where team = {team_id}")''']
                        # ]

                        # Randomly select a Community Chest card
                        # selected_card = random.choice(community_chest_cards)

                        # print("Comm Card ",  selected_card[0])
                        # print("exec: ",selected_card[1])

                        choice = random.randint(1, 16)

                        print("Community started ", choice)

                        comm_msg = ""

                        if choice == 1:
                                comm_msg = "Advance to 'Go' (Collect £200)"
                                cursor.execute(f"update players set cash = cash + 200 where team = {team_id}")

                        elif choice == 2:
                                comm_msg = "Bank error in your favor (Collect £200)"
                                cursor.execute(f"update players set cash = cash + 200 where team = {team_id}")

                        elif choice == 3:
                                comm_msg = "Doctor's fees (Pay £50)"
                                cursor.execute(f"update players set cash = cash - 50 where team = {team_id}")

                        elif choice == 4:
                                comm_msg = "From sale of stock you get £50"
                                cursor.execute(f"update players set cash = cash + 50 where team = {team_id}")

                        elif choice == 5:
                                comm_msg = "Get Out of Jail Free (This card may be kept until needed or traded)"
                                cursor.execute(f"update players set jail_free_cards = jail_free_cards + 1 where team = {team_id}")

                        elif choice == 6:
                                comm_msg = "Go to Jail (Go directly to Jail, do not pass Go, do not collect £200)"
                                cursor.execute(f"update players set in_jail = 1 where team = {team_id}")

                        elif choice == 7:
                                comm_msg = "Holiday Fund matures (Receive £100)"
                                cursor.execute(f"update players set cash = cash + 100 where team = {team_id}")

                        elif choice == 8:
                                comm_msg = "Income tax refund (Collect £20)"
                                cursor.execute(f"update players set cash = cash + 20 where team = {team_id}")

                        elif choice == 9:
                                comm_msg = "It is your birthday (Collect £10 from each player)"
                                cursor.execute("select team from players")
                                all_player_ids = cursor.fetchall()
                                for pid in all_player_ids:
                                        cursor.execute(f"update players set cash = cash - 10 where team = {pid[0]}")
                                cursor.execute(f"update players set cash = cash + {10 * len(all_player_ids)} where team = {team_id}")

                        elif choice == 10:
                                comm_msg = "Life insurance matures (Collect £100)"
                                cursor.execute(f"update players set cash = cash + 100 where team = {team_id}")

                        elif choice == 11:
                                comm_msg = "Pay hospital fees of £100"
                                cursor.execute(f"update players set cash = cash - 100 where team = {team_id}")

                        elif choice == 12:
                                comm_msg = "Pay school fees of £150"
                                cursor.execute(f"update players set cash = cash - 150 where team = {team_id}")

                        elif choice == 13:
                                comm_msg = "Receive £25 consultancy fee"
                                cursor.execute(f"update players set cash = cash + 25 where team = {team_id}")

                        elif choice == 14:
                                comm_msg = "You are assessed for street repairs (£40 per house, £115 per hotel)"
                                cursor.execute(f"select house, hotels from properties where owner_id = {team_id}")
                                result = cursor.fetchall()
                                repair_cost = 40 * sum([x[0] for x in result]) + 115 * sum([x[1] for x in result])
                                cursor.execute(f"update players set cash = cash - {repair_cost} where team = {team_id}")

                        elif choice == 15:
                                comm_msg = "You have won second prize in a beauty contest (Collect £10)"
                                cursor.execute(f"update players set cash = cash + 10 where team = {team_id}")

                        elif choice == 16:
                                comm_msg = "You inherit £100"
                                cursor.execute(f"update players set cash = cash + 100 where team = {team_id}")

                        print(comm_msg)


                        cursor.execute(f"select cash from players where team = {team_id}")
                        resul = cursor.fetchone()[0]
                        moneys=moneys-resul
                        insertLog(txn, 'community', team_id, None, moneys, comm_msg)

                        logging.debug("Community Card \" %s \" was executed,\n Code: %s ",  comm_msg,  comm_msg)   


                elif(c.HouseOnProperty == currAction):

                        # cursor.execute(f"select id from currentTransaction where type='properties'")
                        # property_id = cursor.fetchone()

                        # cursor.execute(f"select owner_id from properties where id={property_id[0]}")
                        # team_id=cursor.fetchone()[0]

                        # cursor.execute(f"select house from properties where id={property_id[0]}")
                        # property_data = cursor.fetchone()

                        # cursor.execute("select house from properties")
                        # result=cursor.fetchall()


                        cursor.execute(f"select mortgage from properties where id={PropertyData[id]}")
                        mortgage = cursor.fetchone()
                        print(mortgage)
                        canbuild=True

                        if mortgage[0]:    # Check if  the property is mortgaged
                                canbuild=False
                                insertLog(txn, 'build', 0, None, PropertyData[houseCost], "Cannot Build Houses,  Property is Mortgaged")

                        print(canbuild)

                        # if(PropertyData[hotels]): # Check if Property already has a Hotel on it
                        #         canbuild=False

                        cursor.execute(f"select sum(house) from properties where house <> 5") # Check if there are houses remaining for purchase

                        total_houses_used=cursor.fetchall()[0]
                        print(total_houses_used[0])
                        if(total_houses_used[0] >=  32):
                                canbuild = False
                                insertLog(txn, 'build', 0, None, PropertyData[houseCost], "No Houses left")
                        print(canbuild)
                        
                        # cursor.execute(f"select color from properties where id={PropertyData[id]}")
                        # property_color = cursor.fetchone()[0]

                        # cursor.execute(f"select * from properties where color='{property_color}'")
                        # result=cursor.fetchall()

                        cursor.execute(f"select * from properties where color = (select color from properties where id = {PropertyData[id]})")
                        sameColorHouses = cursor.fetchall()     # Check if all houses of same colour are owned by same Team 
                        housesBuilt=[]
                        print(sameColorHouses)
                        for prop in sameColorHouses:
                                housesBuilt.append(prop[house])
                                if(prop[owner_id]!=PropertyData[owner_id]):
                                        canbuild=False   
                                        insertLog(txn, 'build', 0, None, PropertyData[houseCost], "Player does not own all Properties of the same color")  
                                        # houses.append(prop[4]
                        
                        print("passes same color check",canbuild)    
                        if canbuild and min(housesBuilt)!=PropertyData[house]:
                                insertLog(txn, 'build', 0, None, PropertyData[houseCost], "Please build houses on the lowest house number")  
                                canbuild=False
                        print("Canbuild ",canbuild)
                        if canbuild:
                                # cursor.execute(f"SELECT houseCost FROM properties WHERE id = {PropertyData[id]}")
                                # r=cursor.fetchone()
                                # print(PlayerData)
                                cursor.execute(f"UPDATE players SET cash = cash - {PropertyData[houseCost]} WHERE team = {PropertyData[owner_id]}")
                                mydb.commit()
                                print(PropertyData[house])
                                if PropertyData[house]<4:
                                        print("less then 4 houses")
                                        cursor.execute(f"update properties set house = house + 1 where id = {PropertyData[id]}")
                                        insertLog(txn, 'build', 0, None, PropertyData[houseCost], f"House Built on Property {PropertyData[name]}") 
                                elif PropertyData[house]==4:
                                        cursor.execute(f"update properties set house = house + 1 where id = {PropertyData[id]}")
                                        cursor.execute(f"update properties set hotels = 1 where id = {PropertyData[id]}")
                                        insertLog(txn, 'build', 0, None, PropertyData[houseCost], f"Hotel Built on Property {PropertyData[name]}")
                        
                        print("House building done")

        
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
                
                elif(c.SellProperty == currAction):
                        logging.debug("Entered Sell Property")
                        
                        if(PropertyData[house] > 0):
                                # Give money  to the player who sold the property
                                # cursor.execute(f"SELECT houseCost FROM properties WHERE id =  {PropertyData[id]}")
                                # hcost = cursor.fetchone()[0]



                                # cursor.execute(f"select team from teams where id = {PropertyData[owner_id]}")
                                # owner_team = cursor.fetchone()[0]
                                owner_team=PropertyData[owner_id]
                                hcost = PropertyData[houseCost] * 0.5
                                
                                cursor.execute(f"select hotels from properties where id = {PropertyData[id]}")
                                has_hotels = cursor.fetchone()[0]

                                
                                if(1 == has_hotels):
  
                                        cursor.execute(f"select sum(house) from properties where house <> 5")
                                        total = cursor.fetchone()[0]
                                        remaining = 32 - total
                                        if(remaining<4):
                                                # hcost=5*PropertyData[houseCost]
                                                insertLog(txn, 'sell', PlayerData[team], None, hcost,  f"Hotel on Property {PropertyData[id]} cannot be sold due to insufficient houses")
                                                return

                                                

                                        cursor.execute(f"update properties set house = 4 where id = {PropertyData[id]}")

                                        cursor.execute(f"update properties set hotels = 0 where owner_id = {PropertyData[id]}")

                                else:
                                        cursor.execute(f"update properties set house = house - 1 where id = {PropertyData[id]}")

                                cursor.execute(f"update players set cash = cash + {hcost} WHERE team = {owner_team}")

                                # Making property as unsold
                                # cursor.execute(f"update properties set owner_id = NULL where id = {PropertyData[id]}")

                                insertLog(txn, 'sell', PlayerData[team], None, hcost,  f"House/Hotel on Property {PropertyData[id]} was sold by Team {owner_team}")
                        else:
                                insertLog(txn, 'sell', PlayerData[team], None, hcost,  f"Property {PropertyData[id]} does not have any houses/hotels to be sold")
                                

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
        if 'players' in  type_values:
                if(PlayerData[cash] < 0 ):
                        logging.debug("Player is Bankrupt")
                        insertLog(txn, 'bankrupt',  PlayerData[team], None, cash, f"Team {PlayerData[team]} is Bankrupt. Please sell properties/Houses to pay off debt or Retire from game")
                


        


                        



if __name__ == "__main__":
        
        # cursor.execute(f"select type from currentTransaction")
        # result = cursor.fetchall()
        # print(result)
        currAction=[]
        # for x in result:

        #         currAction.append(x[0])
        # print(currAction) 

        # asyncio.run(conditions())
         
        # Close the database connection
        
      