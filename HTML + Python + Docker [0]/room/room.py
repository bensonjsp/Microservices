from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import os
import sys
import requests

app = Flask(__name__)
import os
room_db_url = os.environ.get('ROOM_DB_URL')
# room_db_url = "mysql+mysqlconnector://root@localhost:3306/room_db"

if room_db_url is None:
    raise ValueError("Missing ROOM_DB_URL environment variable")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = room_db_url

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_recycle": 299}

db = SQLAlchemy(app)

CORS(app)

class Room(db.Model):
    __tablename__ = "room"

    room_id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, nullable=False)
    hotel_name = db.Column(db.String(255), nullable=False)
    room_number = db.Column(db.Integer, nullable=False)
    room_size = db.Column(db.Integer, nullable=False)
    room_vacancy = db.Column(db.String(20), nullable=False)

    def __init__(self, room_id, hotel_id, hotel_name, room_number, room_size, room_vacancy):
        self.room_id = room_id
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.room_number = room_number
        self.room_size = room_size
        self.room_vacancy = room_vacancy

    def json(self):
        return {
            "room_id": self.room_id,
            "hotel_id": self.hotel_id,
            "hotel_name": self.hotel_name,
            "room_number": self.room_number,
            "room_size": self.room_size,
            "room_vacancy": self.room_vacancy,
        }

# Retrieve list of rooms

@app.route("/getroom", methods=['GET'])
def get_room():
    roomlist = db.session.scalars(db.select(Room)).all()

    if len(roomlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "rooms": [room.json() for room in roomlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no rooms."
        }
    ), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
