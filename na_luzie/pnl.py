from flask import Flask, render_template
from random import random
import itertools

aa = Flask(__name__)

@aa.route("/") #######################################
def hw():
  return '<!DOCTYPE html>\n<html>\n<a href="/hello">Hello</a>\n</html>'


@aa.route("/hello") #####################################
def hello():
  names_file = open("names.txt").readlines()
  return render_template("hello.html", name=random(), names = names_file)

if __name__ == '__main__':
  aa.run(debug = True, host = '0.0.0.0')

# page 158 (133)
