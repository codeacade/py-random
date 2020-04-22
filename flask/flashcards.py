from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
  return "WELCOME TO THE WORLD OF TOMORROW"
  
cou = 0

@app.route("/counter")
def counter():
  global cou
  cou+=1
  return str(cou)
