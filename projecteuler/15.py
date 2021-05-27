##  https://projecteuler.net/problem=15
###########################################################################################################
##  Lattice Paths.
##
##  Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
##  there are exactly 6 routes to the bottom right corner.
##
##  How many such routes are there through a 20×20 grid?
###########################################################################################################
  
##  Lattice path can be solved in brut-force way using itertools module and permutations() iterator:

import itertools
def lattice(x,y):                 ## x and y are grid dimensions, for 20x20 grid x=20, y=20
  return len(set(itertools.permutations('x' * x, 'y' * y)))  ## Using "set" type removes duplicated permutations

##  lattice(6,6) >>> 924   ##  It took 1 minute to calculate on Core2 Duo 2.2 GHz
##
##  ...but..
##
##  There is mathematical way to calculate number of lattice paths for grid x*y.
##  It uses factorials to calculate routes. First of all number of steps always euals x+y (no moves back).
##
## solution is factorial of x+y devided by product of facorial of x and factorial of y
##
##  moves = (x+y)! / (x! * y!)
##  for 6x6 = (6+6)! / 6! * 6! = 12! / (6! * 6!) = 479001600 / (720*720) = 924
##  
##  Solving 20x20 grid can still be a challenge as factorial of 40 is really big number.
##  But this factorial can be reduced by factorial of 20:
##
##  40! / (20! * 20!) = (20! * product of 21 to 40) / (20! * 20!) = factorial of 21 to 40) / 20!
##
##  Lets try to reduce it further

u = list(range(20,41))                   ##  product of 21 to 40
d1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]   ## 20!
d2 = [1,2,3,2,2,5,2,3,7,2,2,2,3,3,2,5,11,2,2,3,13,2,7,3,5,2,2,2,2,17,2,3,3,19,2,2,5]  ##20! reduced to primes

def ff():
  for d in d2:
    for ind in range(21):
      print(d, u[ind], u)
      if not u[ind]%d:
        u[ind] /= d
        break
  prod = 1
  for i in u:
    prod *= i
  print(prod)
  

##  lattice(20,20) >>> 13784652882000


