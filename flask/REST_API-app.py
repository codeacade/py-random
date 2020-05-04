# #########################################################
# https://www.pluralsight.com/courses/python-flask-rest-api
# #########################################################
# Building a REST API Using Python and Flask
# #########################################################

from flask import Flask, render_template
aa=Flask(__name__)

books = [
  {
  "name": "Green Eggs And Ham",
  "price": 7.99,
  "isbn": 12345,
  },
  {
  "name": "The Cat In The Hat",
  "price": 6.99,
  "isbn": 67890
  }
]

@aa.route("/")
def home():
  return render_template('home.html')
  
  
@aa.route("/books")
def see_books():
  return {'bb':books}


@aa.route("/books/<int:isbn>")
def see_books_by_isbn(isbn):
  for i,book in enumerate(books):
    if book["isbn"] == isbn:
      return {"bb":books[i]}
  return "ERROR "+str(book["isbn"])

# ########### Alternative books: #########
@aa.route("/bookz/<int:isbn>")
def see_bookz_by_isbn(isbn):
  for book in enumerate(books):
    if book["isbn"] == isbn:
      return_value = {
        'name': book["name"],
        'price': book["price"]
      }
    return return_value
  return "ERROR "+str(book["isbn"])


aa.run(debug=True)
