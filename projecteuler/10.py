##  https://projecteuler.net/problem=10
############################################################
##  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##  Find the sum of all the primes below two million.
############################################################
##  BRUT-FORCE SOLUTION

def e10(x):
  sumprimes = 0
  while x:
    sumprimes += x * isPrime(x)
    x -= 1         ##  NOTE: Changing step into 2 to omit even numbers reduced time only few % (?)
  return sumprimes - 1  ## 1 is not a prime number
  
def isPrime(x):
    for i in range(2, int(x // 2) + 1):
        if not x%i:
            return False
    return True

##  e10(10_000) >>> 454396535     ## 22 seconds @ Core 2 2.2GHz
##  e10(2_000_000) >>> 
