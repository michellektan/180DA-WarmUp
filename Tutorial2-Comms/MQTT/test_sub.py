import random

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "ece180d/test"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'

# 0. define callbacks - functions that run when events happen.
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    # create mqtt client
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


 # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
def subscribe(client: mqtt_client):
    # The default message callback.
    # (you can create separate callbacks per subscribed topic)
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
