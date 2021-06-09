
##  https://projecteuler.net/problem=9
################################################################################################
##  A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a2 + b2 = c2
##  For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
##  There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##  Find the product abc.
############################################################################
##  BRUT-FORCE SOLUTION

for i in range(500):
    for j in range(500):
        if i**2 + j**2 == (1000-i-j)**2:
            print(i,j)

##  >>> 200 375
