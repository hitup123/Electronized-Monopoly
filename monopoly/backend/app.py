import logging
from  initialize import start_teams
from flask import Flask, send_from_directory, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy import inspect
app = Flask(__name__, static_folder='static')
# from  p1 import bp 
# app.register_blueprint(bp)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Yash:root@localhost/monopoly'
db = SQLAlchemy(app)

txn=0
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_column_names(table_name):
    inspector = inspect(db.engine)
    columns = inspector.get_columns(table_name)
    return [column['name'] for column in columns]
def convert_bytes(value):
    if isinstance(value, bytes):
        return int.from_bytes(value, byteorder='big')
    return value
# Example usage:
def insertflag(data):
    with app.app_context():
        try:
            # print(data)
            flagData=data['value']
            print(flagData)
            db.session.execute(text(f"insert into flags values ('{flagData}')"))
            db.session.commit()
        except Exception as e:
            logger.error(f"Database operation failed: {e}")
            db.session.rollback()
# from sqlalchemy import text
def insertLog(count, action , team1,team2, money, msg ):
            print("log")
            db.session.execute(text(f"insert into log values ({count}, '{action}', '{team1}','{team2}', {money}, '{msg}' )"))
            db.session.commit()

def tempfunc(data):
    with app.app_context():
        try:
            # print(data)
            
            # If message is not None
            if data['message'] is not None:
                # Deleting from 'flags' table
                db.session.execute(text("DELETE FROM flags"))
                db.session.commit()

                spaces = data['message']
                # print(int(spaces))

                # Getting max transaction order from 'log'
                result = db.session.execute(text("SELECT MAX(txn_order) FROM log"))
                temp = result.fetchone()
                # print(temp)
                # Determining transaction number
                if temp == None or len(temp) == 0 or temp[0]==None:
                    txn = 1
                else:
                    txn=temp[0] + 1
                # print("passes txn")
                # Fetching player_id from 'currentTransaction' where type is 'players'
                result = db.session.execute(text("SELECT id FROM currentTransaction WHERE type='players'"))
                player_id = result.fetchone()
                # print("playerid:",player_id)

                # Fetching team_id from 'teams' where id matches player_id
                result = db.session.execute(text(f"SELECT team FROM teams WHERE id = {player_id[0]}"))
                team_id = result.fetchone()
                # print(team_id)

                # Fetching player data from 'players' where team matches team_id
                result = db.session.execute(text(f"SELECT * FROM players WHERE team = {team_id[0]}"))
                PlayerData = result.fetchone()
                # print(PlayerData)

                # Fetching property_id from 'currentTransaction' where type is 'properties'
                result = db.session.execute(text("SELECT id FROM currentTransaction WHERE type='properties'"))
                property_id = result.fetchone()

                # Fetching property data from 'properties' where id matches property_id
                result = db.session.execute(text(f"SELECT * FROM properties WHERE id = {property_id[0]}"))
                PropertyData = result.fetchone()

                # Fetching owners of properties where color is 'Utility'
                result = db.session.execute(text("SELECT owner_id FROM properties WHERE color='Utility'"))
                owners = result.fetchall()

                # Calculating rent
                rent = 0
                if owners[0][0] == owners[1][0]:
                    rent = 10 * int(spaces)
                else:
                    rent = 4 * int(spaces)
                # print(rent)

                # Checking if player has enough cash to pay rent
                if PlayerData[0] >= rent:
                    # print("inside")

                    # Updating player's cash after paying rent
                    db.session.execute(text(f"UPDATE players SET cash = cash - {rent} WHERE team = {PlayerData[5]}"))
                    db.session.execute(text(f"UPDATE players SET cash = cash + {rent} WHERE team = {PropertyData[11]}"))
                    db.session.commit()
                    #   Insert log entry
                    # print("did tran")
                    insertLog(txn, 'rent', team_id, None, rent, f"team {team_id[0]} paid rent ({rent}) on {PropertyData[1]}")
                    logging.debug("Rent has been paid")
                else:
                    logging.debug("Player cannot pay rent")

                # Committing the changes to the database
                db.session.commit()

        except Exception as e:
            logger.error(f"Database operation failed: {e}")
            db.session.rollback()

def check_db_connection():
    with app.app_context():
        try:
            
            x = db.session.execute(text('SELECT * from players'))
            output = x.fetchall()
            x = db.session.execute(text('SELECT * from teams'))
            icon = x.fetchall()
            x=db.session.execute(text('SELECT flag from flags'))
            y=x.fetchone()
            flag=True
            
            # logger.info("Database connection successful. OUTPUT:")
            # print(output)
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
        return y,output,icon
def Logs():
    with app.app_context():
        try:
            y=db.session.execute(text('SELECT txn_order FROM LOG '))
            z=y.fetchall()
            print(z)
            # print("last txn_order value ", z[-1][0])
            # print("txn value ", txn)


            # x = db.session.execute(text(f'SELECT * FROM log WHERE txn_order = (SELECT MAX(txn_order) FROM log)'))
            if(z[-1][0]>txn):
                x = db.session.execute(text(f'SELECT * FROM log WHERE txn_order > {txn}'))
                
                output = x.fetchall()
                # print("OUTPUT: ",f'SELECT * FROM log WHERE txn_order > {txn}')
                return output
            else:
                print("No new Log")
                return ()
            # logger.info("Database connection successful. OUTPUT:")
            #print(output)
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
        
    
@app.route('/Landing')
def index():
    return send_from_directory(app.static_folder, 'index.html')
@app.route('/Teams')
def landing():
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/data')
def get_data():
    
    # 
    column_names=get_column_names('players')
    # print(column_names)
   # Data from the tables
    flag,player_data,icon_data =check_db_connection()

# Create JSON packet
    json_packet = {
    'team1': [],
    'team2': [],
    'team3': [],
    'team4': [],
    'team5': [],
    'team6': [],
    'team7': [],
    'log': '',
    'flag': ''
}
    print(flag)
    if flag!=None and flag[0]=='util':
        json_packet['flag']='util'

# Process player_data
    for player in player_data:
        cash, in_jail, jail_free_cards, propertiesOwned, bankrupt, team = player
        team_key = f"team{team}"
        # print(bankrupt)
        if team_key in json_packet:
        # Filter icons for the current team
            icons = [icon[2] for icon in icon_data if icon[1] == team]
            json_packet[team_key] = [
            icons,
            cash,
            'playing' if bankrupt == b'\x00' else 'bankrupt',
            'NULL' if in_jail == 0 else 'in jail',
            propertiesOwned if propertiesOwned is not None else 'NULL'
        ]

    return jsonify(json_packet)

@app.route('/api/input', methods=['POST'])
def input():
        data=request.json  
        # print("input data: ",data)
        tempfunc(data)
        return jsonify({"received_data": data, "message": "POST request received!"})

@app.route('/api/submit', methods=['POST'])
def submit_data():
    if request.method == 'POST':
        data = request.get_json()
        print((data))
        if data['GameMode']==1:
            # pass
            start_teams(data) #initialize
        else:
            pass
            # start_idv(data)
       
        #initialize
        return jsonify({'message': 'Data submitted successfully'})
    else:
        return jsonify({'error': 'Method not allowed'})
    
@app.route('/api/logs')
def get_logs():    
    data = tuple(Logs())
    jsondata = {}
    print("data",data)
    global txn

    if(data != ()):
        txn = data[-1][0]
        print("TXN : ",txn)
        jsondata = {
            'txn_order': data[0][0],
            'action':  data[0][1],
            'team1': data[0][2],
            'team2': data[0][3],
            'money': data[0][4],
            'msg':  data[0][5],
            "pre": 1
            
        }
        print("Sending a LOG")
        return jsonify(jsondata)
    else:
        print("Sending empty LOG")
        return jsonify({
            "pre": 0
        })

@app.route('/api/transfer_properties',methods=['POST'])
def transfer_properties():
    if request.method == 'POST':
        data = request.get_json()
        print((data))
        insertflag(data)
        #transferproperties()
        return jsonify({'message': 'Data submitted successfully'})
    else:
        return jsonify({'error': 'Method not allowed'})
    
@app.route('/api/get_tax',methods=['POST'])
def get_tax():
    if request.method == 'POST':
        data = request.get_json()
        # print("TAX !!!!!:  ",(data['team']))

        team = data['team']
        amt = data['amount']

        db.session.execute(text(f"update players set cash = cash - {amt}  where team = {team}"))
        db.session.commit()
        
        #transferproperties()
        return jsonify({'message': 'Data submitted successfully'})
    else:
        return jsonify({'error': 'Method not allowed'})
    

@app.route('/api/admin_addmoney',methods=['POST'])
def admin_addmoney():
    if request.method == 'POST':
        data = request.get_json()
        # print("TAX !!!!!:  ",(data['team']))

        team = data['team']
        amt = data['amount']

        db.session.execute(text(f"update players set cash = cash + {amt}  where team = {team}"))
        db.session.commit()
        
        #transferproperties()
        return jsonify({'message': 'Data submitted successfully'})
    else:
        return jsonify({'error': 'Method not allowed'})
    
@app.route('/api/admin_submoney',methods=['POST'])
def admin_submoney():
    if request.method == 'POST':
        data = request.get_json()
        print("ADD !!!!!:  ",(data['amount']))

        team = data['team']
        amt = data['amount']

        db.session.execute(text(f"update players set cash = cash - {amt}  where team = {team}"))
        db.session.commit()
        
        #transferproperties()
        return jsonify({'message': 'Data submitted successfully'})
    else:
        return jsonify({'error': 'Method not allowed'})

from dbConnector import cursor, mydb

@app.route('/api/go_jail' ,methods=['POST'])
def go_jail():
    if request.method == 'POST':
        data = request.get_json()

        print("JAIL: ",data['value'])

        team = data['value']

        cursor.execute(f"select in_jail from players where team = {team}")
        jailstats = cursor.fetchone()[0]

        if( 1 == jailstats):

            cursor.execute(f"select jail_free_cards from players where team = {team}")
            jailfree = cursor.fetchone()[0]

            if(jailfree > 0):
                cursor.execute(f"update players set jail_free_cards = jail_free_cards - 1 where team = {team}")
                mydb.commit()
            else:
                cursor.execute(f"update players set cash = cash - 50 where team = {team}")
                mydb.commit()
                
            cursor.execute(f"update players set in_jail = 0 where team = {team}")
            mydb.commit()

        else:
            cursor.execute(f"update players set in_jail = 1 where team = {team}")
            mydb.commit()
    
    return jsonify({'message': 'Jail toggled successfully'})

@app.route('/api/forfeit' ,methods=['POST'])
def forfeit():
    if request.method == 'POST':
        data = request.get_json()

        team = data['value']

        cursor.execute(f"update properties set 
                       house = 0,
                       owner_id = NULL,
                       hotels = 0,
                       mortgage = 0
                       
                       where team = {team}")
        mydb.commit()

        cursor.execute(f"update players set 
                       cash = 0,
                       in_jail = 0,
                       propertiesOwned = NULL,
                       bankrupt = 1,
                    
                       where team = {team}")
        
        mydb.commit()


        

if __name__ == '__main__':
    
    app.run(debug=True)
