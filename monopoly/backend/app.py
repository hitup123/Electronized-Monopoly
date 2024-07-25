import logging
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

# Example usage:

def check_db_connection():
    with app.app_context():
        try:
            
            x = db.session.execute(text('SELECT * from properties;'))
            output = x.fetchone()
            logger.info("Database connection successful. OUTPUT:")
            print(output)
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
        return output
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/data')
def get_data():
    column_names = get_column_names('properties')
    # print(column_names)
    x=check_db_connection()
    data = {column: value for column, value in zip(column_names, x)}
    print(jsonify(data))
    return jsonify(data)

@app.route('/api/submit', methods=['POST'])
def submit_data():
    if request.method == 'POST':
        data = request.get_json()
        # Process the data received from the frontend
        # ...
        return jsonify({'message': 'Data submitted successfully'})
    else:
        return jsonify({'error': 'Method not allowed'})
if __name__ == '__main__':
    
    app.run(debug=True)
