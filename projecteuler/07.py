##  https://projecteuler.net/problem=7
########################################################################################################
##  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
##  What is the 10001st prime number?
#############################################################################################
##  BRUT-FORCE SOLUTION

def e07(x,y=1,z=0,last=1, ma=0):
    ## x: number of all primes, y: starting to test, last: previous prime, ma: max difference between primes
    while z+1<x:
        if isPrime(y):
            z+=1
            print(y, z, ma, '='*(y-last))   ## "=" element to visualise difference between primes
            if y-last > ma:
                ma = y-last
            last = y
        y+=2 
    print(y, z+1, ma, '='*(y-last))       

def isPrime(x):
    for i in range(2, int(x // 2) + 1):
        if not x%i:
            return False
    return True

##  e07(6) >>> 13
##  e07(10001) >>> 104745
