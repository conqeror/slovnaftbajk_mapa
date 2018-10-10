from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
import pymongo
from bson.json_util import dumps

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/slovnaftbajk"
mongo = PyMongo(app)

@app.route("/status", methods=["GET"])
def status():
    last_status = mongo.db.status.find().limit(1).sort('$natural', pymongo.DESCENDING)
    return dumps(last_status[0]['stations'])

if __name__ == '__main__':
    app.run(debug=True)
