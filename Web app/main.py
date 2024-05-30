from flask import Flask, render_template, url_for
from requests import post

app = Flask(__name__)
first_room = "http://192.168.0.105"

@app.route("/room1/LED<int:led>")
def toggle(led):
    post(f"{first_room}/LED{led}")
    return room_1()

@app.route("/room1")
def room_1():
    return render_template("room1.html", leds=range(2))

@app.route("/")
def home():
    post("http://192.168.0.105/LED1")
    return render_template("home.html")

if __name__ == "__main__":
    app.run("0.0.0.0", port=80)