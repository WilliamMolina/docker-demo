import json
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
import paho.mqtt.client as mqtt

app = Flask(__name__)
api = Api(app)
CORS(app)
client = mqtt.Client()
client.connect("mosquitto", 1883, 60)

class Endpoint(Resource):
    def post(self):
        event = request.json
        print(event)
        client.loop_start()
        client.publish("events/log/"+event.get('id'),event.get('data'))
        client.loop_stop()
        return event,200

api.add_resource(Endpoint,'/events/log')

if __name__ == '__main__':
    app.run(host="0.0.0.0")