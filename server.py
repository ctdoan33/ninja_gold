from flask import Flask, render_template, request, redirect, session
import random
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
    location=request.form["building"]
    if location == "farm":
        delta=random.randint(10, 20)
        session["gold"]+=delta
        session["log"].insert(0, "Earned "+str(delta)+" golds from the farm!")
    if location == "cave":
        delta=random.randint(5, 10)
        session["gold"]+=delta
        session["log"].insert(0, "Earned "+str(delta)+" golds from the cave!")
    if location == "house":
        delta=random.randint(2, 5)
        session["gold"]+=delta
        session["log"].insert(0, "Earned "+str(delta)+" golds from the house!")
    if location == "casino":
        delta=random.randint(-50,50)
        session["gold"]+=delta
        if delta >= 0:
            session["log"].insert(0, "Entered a casino and earned "+str(delta)+" golds!")
        else:
            session["log"].insert(0, "Entered a casino and lost "+str(-delta)+" golds... Ouch..")
    return redirect("/")
@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")
app.run(debug=True)