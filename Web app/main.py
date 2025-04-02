import paho.mqtt.client as mqtt
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
Broker = "test.mosquitto.org"
client = mqtt.Client()

# Callback function to handle messages from the "fromPhone" topic
def on_message(client, userdata, msg):
    print(f"Received message from topic {msg.topic}: {msg.payload.decode()}")

# Set up the MQTT client
client.on_message = on_message
client.connect(Broker)
client.subscribe("fromPhone")
client.loop_start()  # Start the MQTT loop in a separate thread

@app.route("/room1/<string:led>")
def toggle(led):
    client.publish("inTopic", "toggle")
    return redirect(url_for('room_1'))

@app.route("/room1")
def room_1():
    return render_template("room1.html", leds=["Main led", "Secondary LED", "Third LED"])

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
