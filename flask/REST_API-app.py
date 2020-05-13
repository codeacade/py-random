# #########################################################
# https://www.pluralsight.com/courses/python-flask-rest-api
# #########################################################
# Building a REST API Using Python and Flask
# #########################################################

from flask import Flask, render_template, jsonify, request, Response
import json
aa=Flask(__name__)

books = json.load(open('static/books_db.json'))

@aa.route("/") # ##################### HOME
def home():
  return render_template('home.html', jtitle="Homepage")
  
@aa.route("/form/", methods=["POST", "GET"]) # FORM-TEST
def form():
  return render_template('form.html', jtitle="Form Page")
    
@aa.route("/books/") # ############### SEE BOOKS by GET
def see_books():
  return jsonify({'bb':books})


def validBookObject(bookObject): # ###### INPUT VALIDATION
  try:
    if(isinstance(bookObject, dict) and "name" in bookObject and "price" in bookObject and "isbn" in bookObject):
      return True
    else:
      return False
  except:
    return False
      
      
@aa.route("/books/", methods=["POST"]) # ##### ADD BOOKS
def add_book():    
  request_data = request.get_json()
  if(validBookObject(request_data)):
    new_book = {
        "name": request_data["name"],
        "price": request_data["price"],
        "isbn": request_data["isbn"]
    } # ################################ DATA FILTERED
    
    books.insert(0, new_book)
    respon = Response("", 201, mimetype='application/json')
    respon.headers["Location"] = "/books/" + str(new_book['isbn'])
    return respon
    
  else:  # ### THIS DO IF NOT VALID REQUEST SENT
    invBookError = {
      "error":"OMG Invalid book!",
      "helpMsg":"Seriusly, try again!"
    }
    respon = Response(json.dumps(invBookError), status=400, mimetype="applicatoni/json")
    return respon

@aa.route("/books/<isbn>") # ####### BOOKS ISBN
def see_books_by_isbn(isbn):
  for i,book in enumerate(books):
    if book["isbn"] == isbn:
      return {"bb":books[i]} ## shorter version
  return "ERROR. Serial Number " + str(book["isbn"] == isbn)
  
  
@aa.route("/books/<isbn>", methods=["PUT"])  # ####### UPDATE BOOK INFO
def replace_book(isbn):
  return request.get_json()

aa.run(debug=True)
