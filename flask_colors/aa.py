from flask import Flask, render_template

aa = Flask(__name__)

@aa.route("/")
def route_01():
  return ("<p>THIS IS ROUTE 01</p>")

@aa.route("/card/<x>")  ## https://localhost/card/red black blue
def route_card(x):
  return render_template("card.html", str01 = x.split())

aa.run(debug=True)
