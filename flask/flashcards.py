# 1.create virtual envoroment: $virtualenv name
# 2.activate virtual enviroment: $source bin/bin/activate
# 3.install Flask in new enviroment: $pip install -p python3 
# 4.create py file in virtual enviroment

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

# 5.create enviromental variables (Debian):
# 5.a $export FLASK_APP=flashcards.py   #no spaces next to "="
# 5.b $export FLASK_ENV=development     #for easier debuging
# 6. $flask run --host 0
