import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify
from flask_cors import CORS


# Create logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Configure the logger
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a file handler that logs debug and higher-level messages
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)

# Define the format for the handler logs
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

app = Flask(__name__)

# Allow CORS from all origins
CORS(app, resources={r"/*": {"origins": "*"}})

categories = [
    {'catid': 1, 'desc': 'meat'},
    {'catid': 2, 'desc': 'dairy'},
    {'catid': 3, 'desc': 'bakery'}
]

@app.route('/')
def home():
    return "Hello, World"

@app.route('/categories')
def get_categories():
    return jsonify(categories)

@app.route('/dis_cat/<id>')
def dis_cat(id):
    print(id)
    return "Hello, test"

@app.route('/test')
def test():
    return "Test Page"

if __name__ == '__main__':
    app.run(debug=True)