## Load it with command: import rand
## Run functions(methods) with command: rand.function_name(function_paramaters)
## In case rand.py changed, use command: reload(rand)
## To reload in Python3 first run "from importlib import reload"

import random
def trun(n):
  b = [1,2,3,4,5]
  for i in range(n):
    b[random.choice(range(5))]+=1
  return(b)

def grun(n, ico="H"):
  b = trun(n)
  for i in range(5):
    print(ico*b[i])

def walk2d(n):
  result = 0
  for i in range(n):
    result+=random.choice((1,-1))
  return result

def xtree():
  print(" "*(9-i) + "/" + "|"*i*2 + "\\")
  ## MERRY XMASS ##
  
