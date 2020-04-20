# Three test functions for error testing

def fib(x):
 result=[1,2]
 for i in range(1,x):
  result.append(result[i]+result[i-1])
 return result[1:]

def fiblast(x):
  return fib(x)[-1]

def fibmax(y):
 i=2
 while fiblast(i) < y:
   i+=1
 return fib(i)[:-1]
