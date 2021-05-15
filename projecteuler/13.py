##  https://projecteuler.net/problem=13
############################################################
##  Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
##  3710728753390210279879799822083759024651013574025... etc
############################################################
##  BRUT-FORCE SOLUTION (SUM OF ALL CALCULATED)

with open("digits.txt") as f:  # text file with one-hundred 50-digit numbers
  ff = f.readlines()
print(sum(list(map(int, ff))))

## >>> 5537376230390876637302048746832985971773659831892672
