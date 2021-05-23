##  https://projecteuler.net/problem=14
############################################################
##  Longest Collatz sequence:
##  The following iterative sequence is defined for the set of positive integers:
##
##  n → n/2 (n is even)
##  n → 3n + 1 (n is odd)
##
##  Using the rule above and starting with 13, we generate the following sequence:
##  13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
##
##  It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
##
##  Which starting number, under one million, produces the longest chain?
##########################################################################
##  BRUT-FORCE SOLUTION (5 minuter os Coreduo)

def all(w):     ## calculate Collatz sequence for given number
  alist = []
  while w > 1:
    alist.append(int(w))
    w = (w/2, w*3+1)[int(w)%2]
  return alist

def main(x):      ## calling for all numbers in x range (descending)
  step = 0
  for i in range(x, 0, -1):
    if len(all(i)) > step:
      step = len(all(i))
      print("------------------------------")
      print(i, len(all(i)), all(i)) 

## >>> main(999999) => 837799 524  ## 837799 is number starting Collatz sequence, greatest 524 chain length
