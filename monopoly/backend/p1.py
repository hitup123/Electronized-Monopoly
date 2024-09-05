import random

import Constants as c

# Connect to the MySQL database

from dbConnector import dbconnect
mydb=dbconnect()
cursor=mydb.cursor()


def insertLog(count, action , team1,team2, money, msg ):
        cursor.execute(f"insert into log values ({count}, '{action}', '{team1}','{team2}', {money}, '{msg}' )")




def conditions():
        cursor.execute(f"select type from currentTransaction")
        result = cursor.fetchall()
        # print(result)
        currAction=[]
        for x in result:

                currAction.append(x[0])


        #print("0hi: ", currAction)
        #mydb.commit()
        #scan_order=[['properties','players'],['chance','players'] ,['comm','players'],['house','properties'],['mort','properties']]
        
        #actions = [ 'buy/rent',  'chance', 'community chest',  'property/house', 'property/mortgage']

              
        if currAction in c.Actions:
                
                #index = (c.Actions).index(currAction)
                #print("HI1")
                #print(index,actions[index])
                cursor.execute(f"select MAX(txn_order) from log")
                temp = cursor.fetchone()
                if(len(temp) == 0):
                        txn = 1
                else:
                        txn = temp[0] + 1

                print("This is p1.py file, value of txn is ", txn)

                # return
                if(c.PlayerOnProperty == currAction):
                        print("hi1")
                        #Fetching Data from Database                        
                        cursor.execute(f"select id from currentTransaction where type='properties'")
                        property_id = cursor.fetchone()
                        print(property_id[0])
                        cursor.execute(f"select * from properties where id ={property_id[0]}")
                        print("hi2")
                        property_data = cursor.fetchone()
                        cursor.execute(f"select id from currentTransaction where type='players'")
                        player_id = cursor.fetchone()
                        cursor.execute(f"select team from teams where id={player_id[0]}")
                        print("hi3")
                        team_id=cursor.fetchone()
                        print("teamid: ",team_id)
                        cursor.execute(f"select * from players where team={team_id[0]}")
                        print("hi5")
                        player_data = cursor.fetchone()
                        print(player_data)
                        if(property_data[-4]==None):
                                print("hi6")
                                if(player_data[0]>property_data[3]):
                                        print("hi7")
                                        cursor.execute(f"update players set cash = cash - {property_data[3]} where team = {team_id[0]}")
                                        cursor.execute(f"update properties set owner_id = {team_id[0]} where id = {property_id[0]}")
                                        #cursor.execute(f"insert into  log values ({txn}, 'team{team_id} bought {property_data[1]}') ")
                                        str1 = f"team{team_id} bought {property_data[1]}"
                                        insertLog(txn, 'buy', team_id, None, property_data[3], str1)
                                        mydb.commit()
                                else:
                                        #make api for telling it failedf
                                        print(player_data[2],property_data[3])
                                        insertLog(txn, 'buyfailed', team_id, None, 0, f'team{team_id} has insufficient funds to buy {property_data[1]}')
                                        print("Insufficient balance")
                                        
                        elif(property_data[-4]!=team_id[0]):
                                print("rent")
                                cursor.execute(f"select house from properties where id={property_id[0]}")
                                house = cursor.fetchone()[0]
                                cursor.execute(f"select R{house} from properties where id={property_id[0]}")
                                rent=cursor.fetchone()[0]
                                if player_data[0] >= rent:
                                        cursor.execute(f"update players set cash = cash - {rent} where team = {team_id[0]}")
                                        cursor.execute(f"update players set cash = cash + {rent} where team = {property_data[-4]}")
                                        # mydb.commit()
                                        #cursor.execute(f"insert into  log values ({txn}, 'team{team_id} paid rent on {property_data[1]}') ")
                                        print("Team id: ",team_id[0])
                                        insertLog(txn, 'rent', team_id, None, rent, f'team {team_id} paid rent ({rent}) on {property_data[1]}')

                                else:
                                        print("Insufficient balance ")

                elif(c.PlayerOnChance == currAction):

                        cursor.execute(f"select id from currentTransaction where type='players'")
                        player_id=cursor.fetchone()[0]
                        cursor.execute(f"select * from teams where id={player_id[0]}")
                        team_id=cursor.fetchone()[0]
                        # Draw a random Chance card
                        chance_cards = [
                                ["Advance to 'Go' (Collect £200)",'''cursor.execute(f"update players set cash = cash + 200 where team = {team_id}")'''],
                                ["Advance to Trafalgar Square", ""],
                                ["Advance to Pall Mall (If you pass Go, collect £200)", ""],
                                ["Bank pays you dividend of £50", '''cursor.execute(f"update players set cash = cash + 50 where team = {team_id}")'''],
                                ["Get out of Jail Free (This card may be kept until needed or traded)", ""],
                                ["Go back 3 spaces",""],
                                ["Go directly to Jail (Do not pass Go, do not collect £200)", ""],
                                ["Make general repairs on all your property (For each house pay £25, For each hotel £100)", '''cursor.execute(f"select houses,hotel from properties where owner_id = {team_id}")
                                 result=cursor.fetchall()
                                money=0
                                for x in result:
                                        money += (x[0] * 25) + (x[1] * 100)
                                if player_data[2] >= money:
                                        cursor.execute(f"update players set cash = cash - {money} where team = {team_id}")
                                        mydb.commit()
                                else:
                                        print("Insufficient balance")'''],
                                ["Pay poor tax of £15", '''cursor.execute(f"update players set cash = cash - 15 where team = {team_id}")'''],
                                ["Take a trip to Marylebone Station (If you pass Go, collect £200)", ""],
                                ["Advance to King's Cross Station (If you pass Go, collect £200)", ""],
                                ["Advance to Mayfair", ""],
                                ["You have been elected Chairman of the Board (Pay each player £50)", ""],
                                ["Your building loan matures (Collect £150)", '''cursor.execute(f"update players set cash = cash + 150 where team = {team_id}")'''],
                                ["You have won a crossword competition (Collect £100)", '''cursor.execute(f"update players set cash = cash + 100 where id = {team_id}")''']
                        ]
                        selected_card = random.choice(chance_cards)
                        
                        exec(selected_card[1])
                                

                                
        
                elif(c.PlayerOnCommunity == currAction):
                        #community chest card
                        # List of British Monopoly Community Chest cards
                        cursor.execute(f"select id from currentTransaction where type='players'")
                        player_id=cursor.fetchone()[0]
                        cursor.execute(f"select * from teams where team={player_id[0]}")
                        team_id=cursor.fetchone()[0]
                        
                        community_chest_cards = [
                                ["Advance to 'Go' (Collect £200)", '''cursor.execute(f"update players set cash = cash + 200 where team = {team_id}")'''],
                                ["Bank error in your favor (Collect £200)", '''cursor.execute(f"update players set cash = cash + 200 where team = {team_id}")'''],
                                ["Doctor's fees (Pay £50)", '''cursor.execute(f"update players set cash = cash - 50 where team = {team_id}")'''],
                                ["From sale of stock you get £50", '''cursor.execute(f"update players set cash = cash + 50 where team = {team_id}")'''],
                                ["Get Out of Jail Free (This card may be kept until needed or traded)", '''cursor.execute(f"update players set get_out_of_jail_free = get_out_of_jail_free + 1 where id = {team_id}")'''],
                                ["Go to Jail (Go directly to Jail, do not pass Go, do not collect £200)", '''cursor.execute(f"update players set in_jail = 1 where id = {team_id}")'''],
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
                        selected_community_card = random.choice(community_chest_cards)

                        # Execute the associated code
                        exec(selected_community_card[1])


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
                        cursor.execute(f"select id from currentTransaction where type='properties'")
                        property_id = cursor.fetchone()[0]
                        cursor.execute(f"select owner_id from properties where id={property_id[0]}")
                        team_id=cursor.fetchone()[0]
                        cursor.execute()

                mydb.commit()
        
        else:
                print("ERROR\n")
                        



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
        
      