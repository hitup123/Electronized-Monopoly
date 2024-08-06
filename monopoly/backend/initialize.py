import json
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="monopoly"
)
cursor=mydb.cursor()

def start_teams(data):
    #check for number of teams;
    characters = data['Characters']


    # Initialize dictionary to store team members
    teams = {}

    # Categorize items by team
    for item in characters:
         if item['isPressed']:  # Only include characters where isPressed is True
            team = item['team']
            name = item['name']
            if team not in teams:
                teams[team] = []
            teams[team].append(name)
        

    # Count number of teams
    number_of_teams = len(teams)

    # Print the results
    print(f"Number of teams: {number_of_teams}")
    # cursor.execute("DROP TABLE IF EXISTS teams")
    # cursor.execute("""
    # CREATE TABLE teams (
    #     id int primary key,
    #     team int
    # )
    # """)
    # for x in teams:
    #     for y in teams[x]:
    #         cursor.execute(f"insert into monopoly.teams (id, team) values (select id from monopolymaster.teams where icon={y},'{x}'")
    #     mydb.commit()
    # for team, members in teams.items():
        # print(f"{team}: {members}")
    cursor.execute("TRUNCATE TABLE currentTransaction")
    cursor.execute("TRUNCATE TABLE log ")

    mydb.commit()
    cursor.execute("drop table if exists players")
    cursor.execute("drop table if exists properties")
    cursor.execute("create table properties as select * from monopolymasterproperties")
    cursor.execute("create table players as select * from monopolymaster.master_teams where 1=2")
    for item  in characters:
        if item['isPressed']: 
            #adding players to current game table
            cursor.execute(f"insert into players as select * from monopolymaster.master_team where icon={item['name']} ")
    for x in team:
        for y in  team[x]:
            #setting correct cash amount
            cursor.execute(f"update table players set cash = {len(x)*1500} where icon={y}")
            cursor.execute(f"update table players set team = {int(x[4])} where icon= {y}")
            mydb.commit()
def start_idv():
    pass