##  https://projecteuler.net/problem=4
##############################################################################################
##  A palindromic number reads the same both ways.
##  The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
##  Find the largest palindrome made from the product of two 3-digit numbers.
#################################################################################

def projecteuler04():
    maxpal = 1
    for i in range(100,999):
        for j in range(100,999):
            if str(i*j)[:3] == str(i*j)[6:2:-1] and i*j > maxpal:
                maxpal = i*j 
                print(i, j, maxpal)

##  i = 913, j = 993, maxpal = 906609
