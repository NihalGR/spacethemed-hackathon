from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/explore")
def get_started():
    return render_template("getstartedpage.html")

@app.route("/explore/solarsystem")
def solar_system():
    return render_template("solarsystem.html")

@app.route("/explore/blackhole")
def black_hole():
    return render_template("blackhole.html")

app.run(debug=True)
