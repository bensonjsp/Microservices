from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import os
import sys

app = Flask(__name__)
import os
hotel_db_url = os.environ.get('HOTEL_DB_URL')
# hotel_db_url = "mysql+mysqlconnector://root@localhost:3306/hotel_db"

if hotel_db_url is None:
    raise ValueError("Missing HOTEL_DB_URL environment variable")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = hotel_db_url

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_recycle": 299}

db = SQLAlchemy(app)

CORS(app)

class Hotel(db.Model):
    __tablename__ = "hotel"

    hotel_id = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(255), nullable=False)
    hotel_location = db.Column(db.String(255), nullable=False)


    def __init__(self, hotel_id, hotel_name, hotel_location):
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.hotel_location = hotel_location

    def json(self):
        return {
            "hotel_id": self.hotel_id,
            "hotel_name": self.hotel_name,
            "hotel_location": self.hotel_location,
        }

# Retrieve list of hotels

@app.route("/gethotel", methods=['GET'])
def get_hotel():
    hotellist = db.session.scalars(db.select(Hotel)).all()

    if len(hotellist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "hotels": [hotel.json() for hotel in hotellist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no hotels."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
