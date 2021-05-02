##  https://projecteuler.net/problem=3
####################################################################
##  The prime factors of 13195 are 5, 7, 13 and 29.
##  What is the largest prime factor of the number 600851475143 ?
##
##  /hint - start with smalest factors to find bigger prime division result/ 
###############################################################################

def isPrime(x):
    for i in range(2, int(x // 2) + 1):
        if not x%i:
            return False
    return True

def topPrime(y):
    for i in range(2, y):
        if not y%i and isPrime(y / i):
            print("Largest prime factor = ", y / i)
            break

##  topPrime(600851475143): >> 6857
##  topPrime(600851475141): >> 16716787
