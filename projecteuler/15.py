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
