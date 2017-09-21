from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
@app.route("/")
def ninja():
    if "gold" not in session:
        session["gold"]=0
    if "log" not in session:
        session["log"]=[]
    return render_template("index.html")
@app.route("/process_money", methods=["POST"])
def process():
    timestring=datetime.strftime(datetime.today(), "(%Y/%m/%d %I:%M %p)")
    location=request.form["building"]
    if location == "farm":
        delta=random.randint(10, 20)
    if location == "cave":
        delta=random.randint(5, 10)
    if location == "house":
        delta=random.randint(2, 5)
    if location == "casino":
        delta=random.randint(-50,50)
        if session["gold"] <= -delta:
            session["log"].insert(0, ["Entered a casino and lost all your gold... Ouch... "+timestring, "red"])
        elif delta >= 0:
            session["log"].insert(0, ["Entered a casino and earned "+str(delta)+" golds! "+timestring, "green"])
        else:
            session["log"].insert(0, ["Entered a casino and lost "+str(-delta)+" golds... Ouch... "+timestring, "red"])
    else:
        session["log"].insert(0, ["Earned "+str(delta)+" golds from the "+location+"! "+timestring, "green"])
    session["gold"]+=delta
    if session["gold"]<0:
        session["gold"]=0
    return redirect("/")
@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")
app.run(debug=True)