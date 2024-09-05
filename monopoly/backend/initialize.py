import json
import mysql.connector
from backend.dbConnector import dbconnect
mydb=dbconnect()
cursor=mydb.cursor()
# mydb.autocommit()

def start_teams(data):
  #check for number of teams;
    characters = data['Characters']
    print(f"data -- {data}")
    print(f"char -- {characters}")
    # Initialize dictionary to store team members
    teams = {}

    prev_id = -1

    # Categorize items by team
    for item in characters:
         if item['isPressed']:  # Only include characters where isPressed is True
            team = item['team']
            name = item['name']
            if team not in teams:
                teams[team] = []
            teams[team].append(name)
        
    print(teams)
    # Count number of teams
    number_of_teams = len(teams)
    # {'team1': ['Cannon', 'Car'], 'team2': ['Dog', 'Dustbin'], 'team3': ['Hat', 'Horse'], 'team4': ['Wheelbarrow', 'Ship']}
    # Print the results
    print(f"Number of teams: {number_of_teams}")
    cursor.execute("DROP TABLE IF EXISTS teams")
    cursor.execute("""
    CREATE TABLE teams (
        id int primary key,
        team int,
        icon varchar(20)
    )
    """)
    for x in teams:
        for y in teams[x]:
            cursor.execute(f"""
    INSERT INTO monopoly.teams (id, team, icon) 
    SELECT id, '{x[-1]}', icon 
    FROM monopolymaster.master_teams 
    WHERE icon = '{y}'
""")

        mydb.commit()
    for team, members in teams.items():
        print(f"{team}: {members}")
    cursor.execute("TRUNCATE TABLE currentTransaction")
    cursor.execute("TRUNCATE TABLE log ")
    #insertLog(txn, 'buyfailed', team_id, None, 0, 'team{team_id} has insufficient funds to buy {property_data[1]}')
    cursor.execute("insert into log values (0, 'StartGame', 'None', 'None', 0, 'A new Game has started')")


    mydb.commit()
    cursor.execute("drop table if exists players")
    cursor.execute("drop table if exists properties")
    cursor.execute("create table properties as select * from monopolymaster.masterproperties")
    cursor.execute("create table players as select * from monopolymaster.master_players where 1=2")
    # print("items:" ,item)
#     for item in characters:
#         if item['isPressed']: 
#             #adding players to current game table
#             # cursor.execute(f"insert into players as select * from monopolymaster.master_players where icon='{item['name']}' ")
#             cursor.execute(f"""
#     INSERT INTO players 
#     SELECT * 
#     FROM monopolymaster.master_players 
#     WHERE team = (SELECT team FROM teams WHERE icon = '{item['name']}')
# """)
    for x in range(0,number_of_teams):
            cursor.execute(f"INSERT INTO players (cash, in_jail, jail_free_cards, propertiesOwned, bankrupt, team) SELECT cash, in_jail, jail_free_cards, propertiesOwned, bankrupt, {x + 1} FROM monopolymaster.master_players")
            mydb.commit()
            cursor.execute(f"select COUNT(*) from teams where team={x+1}")
            team_size=cursor.fetchone()[0]
            cursor.execute(f"update players set cash={team_size*1500} where team={x+1}")
    mydb.commit()
    # for x in teams:
    #     print(x)
    #     for y in  teams[x]:
    #         #setting correct cash amount
    #         cursor.execute(f"update players set cash = {len(x)*1500} where team = (SELECT team FROM teams WHERE icon = '{y}')")
    #         cursor.execute(f"update players set team = {int(x[4])} where team = (SELECT team FROM teams WHERE icon = '{y}')")
    #         mydb.commit()
def start_idv():
    pass