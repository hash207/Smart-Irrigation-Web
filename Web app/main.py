from flask import Flask, render_template
from requests import post

app = Flask(__name__)
first_room = "http://192.168.0.105"

@app.route("/room1/<string:led>")
def toggle(led):
    post(f"{first_room}/{led}")
    return room_1()

@app.route("/room1")
def room_1():
    return render_template("room1.html", leds=["main_led", "secindary_led"])

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run("0.0.0.0", port=80)