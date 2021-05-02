##  https://projecteuler.net/problem=2
########################################################################################################
##  Each new term in the Fibonacci sequence is generated by adding the previous two terms.
##  By starting with 1 and 2, the first 10 terms will be:
##
##  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
##
##  By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
######################################################################################################################################

def projecteuler02(x):
    f1, f2 = 0, 2
    su = []
    while f2 < x:
        f1, f2 = f2, f2 * 4 + f1
        ##  Next Fibonacci even number is equal quadruple of last one (f2) plus previous one (f1)
        ##  It works with other recurrence sequences like Lucas numbers for example (2,1,3,4,7,11,18,29,47...)
        su.append(f1)
    return(sum(su))

##  projecteuler01(1000) >> 798
##  projecteuler01(1000000) >> 1089154
##  projecteuler01(4000000) >> 4613732
##  projecteuler01(100000) >> 2333316668
