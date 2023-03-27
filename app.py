from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://mongo:27017/')
db = client.myapp

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
