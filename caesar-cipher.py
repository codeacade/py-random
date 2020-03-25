import random

# Random monoaplhabetic cipher generator
# Randomly change order of 26 letters (arr[] -> brr[])
def rans():
  arr = [i for i in "abcdefghijklmnoprstuwxyz"]
  brr = []
  print ("".join(arr)).upper()
  
  # ----------------------------program:
  while arr:                  # as long as arr[] is not empty...
    aa = random.choice(arr)   # select radon element of arr[]...
    brr.append(aa)            # add it to brr[]...
    arr.remove(aa)            # and remove it from arr[]
  print ("".join(brr)).upper() 
# how to use it?...
