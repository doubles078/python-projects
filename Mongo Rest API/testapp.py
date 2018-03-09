from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'lfd_mongo'


mongo = PyMongo(app)

print("Success!")


@app.route('/')
def home_page():
    online_users = mongo.db.gym.find({'Location': 'Decatur, Alabama'})
    print(online_users)

    return online_users[0]


if __name__ == '__main__':
    app.run(debug=True)
