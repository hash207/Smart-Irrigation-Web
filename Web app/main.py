import paho.mqtt.client as mqtt
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
Broker = "broker.emqx.io"
client = mqtt.Client()

# Callback function to handle messages from the "fromPhone" topic
def on_message(client, userdata, msg):
    data = msg.payload.decode()
    topic = msg.topic
    print(f"Received message from topic {topic}: {data}")

# Set up the MQTT client
client.on_message = on_message
client.connect(Broker, 1883)
client.subscribe("HashLAP")
client.loop_start()  # Start the MQTT loop in a separate thread

@app.route("/room1/<string:led>")
def toggle(led):
    client.publish("HashESP1", f"{led}")
    return redirect(url_for('room_1'))

@app.route("/room1")
def room_1():
    return render_template("room1.html", leds=["Main led", "Secondary LED", "Third LED"])

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
