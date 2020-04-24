import redis
import paho.mqtt.client as mqtt

redis_client = redis.Redis(host='redis', port=6379, db=0)

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("events/log/#")

def on_message(client, userdata, msg):
  log = msg.payload.decode("utf-8")
  event_id = msg.topic.split('/')[2]
  redis_client.set('event:'+event_id, log)
  print(log)

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect("mosquitto", 1883, 60)
mqtt_client.loop_forever()