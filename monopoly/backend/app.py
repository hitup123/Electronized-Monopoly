import logging
# from initialize import start_teams
from flask import Flask, send_from_directory, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy import inspect
app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/monopoly'
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
            # logger.info("Database connection successful. OUTPUT:")
            # print(output)
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
        return output
@app.route('/Landing')
def index():
    return send_from_directory(app.static_folder, 'index.html')
@app.route('/')
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
    x=check_db_connection()
    # print(x)
    json_packet = {
    'team1': [],
    'team2': [],
    'team3': [],
    'team4': [],
    'team5': [],
    'team6': [],
    'team7': [],
    'log': 'I am Bankrupt',
}
    for row in x:
        data = dict(zip(column_names, [convert_bytes(item) for item in row]))
        team_key = f"team{data['team']}"
        if team_key in json_packet and isinstance(json_packet[team_key], list) and len(json_packet[team_key]) == 0:
            json_packet[team_key] = [[data['icon']], data['cash'], 'playing' if data['bankrupt'] == 0 else 'bankrupt', 'NULL' if data['in_jail']==0 else 'in jail',data['propertiesOwned'] if data['propertiesOwned']!=None else 'NULL']
        elif team_key in json_packet:
            json_packet[team_key][0].append(data['icon'])
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
        # start_teams(data)
        # Process the data received from the frontend
        # ...
        # Insert the data into the database
        #initialize
        return jsonify({'message': 'Data submitted successfully'})
    else:
        return jsonify({'error': 'Method not allowed'})
if __name__ == '__main__':
    
    app.run(debug=True)
