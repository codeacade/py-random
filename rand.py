## Load it with command: import rand
## Run functions(methods) with command: rand.function_name(function_paramaters)
## In case rand.py changed, use command: reload(rand)

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
  
