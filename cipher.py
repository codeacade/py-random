import random

def rans():
  arr = list("abcdefghijklmnoprstuvwxyz")
  
  random.shuffle(arr)
  ff = open("shuffle.txt","w")
  ff.write("".join(arr))
  ff.close()
  
    
def reds():
  arr = list("abcdefghijklmnoprstuvwxyz")
  hrr = {}
  ff = open("shuffle.txt")
  srr = ff.read()
  ff.close()
  for i in range(25):
    print(arr[i] + "..." + srr[i])
    hrr[arr[i]] = srr[i]
  print(hrr)
    
 # end
