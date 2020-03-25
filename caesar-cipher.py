import random

def rans():
  arr = [i for i in "abcdefghijklmnoprstuwxyz"]
  brr = []
  print ("".join(arr)).upper()
  while arr:
    aa = random.choice(arr)
    brr.append(aa)
    arr.remove(aa)
  print ("".join(brr)).upper() 
