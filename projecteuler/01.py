##  https://projecteuler.net/problem=1
########################################################################################################
##  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
##  The sum of these multiples is 23.
##  Find the sum of all the multiples of 3 or 5 below 1000.
##############################################################

def projecteuler01(x):
  return sum(i for i in range(x) if not i%3 or not i%5)

##  projecteuler01(100) > 2318
##  projecteuler01(1000) > 233168
##  projecteuler01(10000) > 23331668
##  projecteuler01(100000) > 2333316668
