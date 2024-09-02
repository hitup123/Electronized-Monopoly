import logging


from backend.initialize import start_teams
from flask import Flask, send_from_directory, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy import inspect
app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Yash:root@localhost/monopoly'
db = SQLAlchemy(app)

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

def check_db_connection():
    with app.app_context():
        try:
            
            x = db.session.execute(text('SELECT * from players'))
            output = x.fetchall()
            x = db.session.execute(text('SELECT * from teams'))
            icon = x.fetchall()
            # logger.info("Database connection successful. OUTPUT:")
            # print(output)
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
        return output,icon
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
    player_data,icon_data =check_db_connection()

# Create JSON packet
    json_packet = {
    'team1': [],
    'team2': [],
    'team3': [],
    'team4': [],
    'team5': [],
    'team6': [],
    'team7': [],
    'log': 'I am Bankrupt'
}

# Process player_data
    for player in player_data:
        cash, in_jail, jail_free_cards, propertiesOwned, bankrupt, team = player
        team_key = f"team{team}"
        if team_key in json_packet:
        # Filter icons for the current team
            icons = [icon[2] for icon in icon_data if icon[1] == team]
            json_packet[team_key] = [
            icons,
            cash,
            'playing' if bankrupt == 0 else 'bankrupt',
            'NULL' if in_jail == 0 else 'in jail',
            propertiesOwned if propertiesOwned is not None else 'NULL'
        ]

# print(json_packet)

    # data=[dict(zip(column_names,item )) for item in converted_data]


    # data = [dict(zip(column_names, item)) for item in converted_data]
    # data = {column: value for column, value in zip(column_names, x)}

    print((json_packet))
    return jsonify(json_packet)
# @app.route('/api/update')
# def update_data():
#     column_names = get_column_names('properties')
#     # print(column_names)
#     x=check_db_connection()
#     data = {column: value for column, value in zip(column_names, x)}
#     print(jsonify(data))
#     return jsonify(data)
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
    

@app.route('/api/transfer_properties',methods=['POST'])
def transfer_properties():
    if request.method == 'POST':
        data = request.get_json()
        print((data))
        
        #transferproperties()
        return jsonify({'message': 'Data submitted successfully'})
    else:
        return jsonify({'error': 'Method not allowed'})
if __name__ == '__main__':
    
    app.run(debug=True)
