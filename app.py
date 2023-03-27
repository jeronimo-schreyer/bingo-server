from datetime import datetime
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://mongo:27017/')
db = client.myapp

@app.route('/')
def home():
    return 'Hello, World!'

@app.before_request
def get_game_info():
    game_id = get_query_param('gameId')
    if game_id == False:
        app.logger.info('No game selected')
    else:
        registry = db.registries.find_one({'_id': game_id[0]})
        if registry:
            app.logger.info(f'Resuming game {game_id[0]} {registry}')
        else:
            app.logger.info(f'No game with id {game_id[0]}. Creating a new one')

            data = {
                '_id': game_id[0],
                'name': 'John Doe',
                'email': 'johndoe@example.com',
                'created_at': datetime.now(),
            }
            result = db.registries.insert_one(data)
            app.logger.info(f'Game created with id {result.inserted_id}')


def get_query_param(key):
    for k in request.args.keys():
        if k == key:
            return request.args.getlist(key)
    return False


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
