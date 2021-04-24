##  https://projecteuler.net/problem=5
########################################################################################################
##  2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
##  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
########################################################################################################
  
def isPrime(x):                           ##  used in primesP() function below
    for i in range(2, int(x // 2) + 1):
        if not x%i:
            return False
    return True

def primesP(x):               ##  use this to calculate product of all primes in range (20 for example)
    product = 1
    for i in range(1,x):
        if isPrime(i):        ##  isPrime() function from above
            product *= i
    return product

def smallest(x):          ##  x is a range to calculate the smallest number divisible by all its elements
    step = primesP(x)     ##  because smalest number is multiplication of product of all primes in range
    s = 0
    while True:
        s += step
        for i in range(2,x):
            if s%i:
                break
            if i==(x-1):
                return s, s/step 

##  smallest(10) >>> (2520, 12.0)             ## this is example range from problem description
##  smallest(20) >>> (232792560, 24.0)        ##  this is problem solution (range 20)
##  smallest(30) >>> (2329089562800, 360.0)
##  smallest(40) >>> (5342931457063200, 720.0)
