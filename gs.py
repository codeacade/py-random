# Gaussian distribution

def randsteps(n):
  import random
  return sum([random.choice((-1,0,1)) for i in range(n)])
  
# Final counting with orinting. "n" for number of random steps, "m" for number of overall repiting
  
def distrib(n,m):
  allr = [randsteps(n) for i in range(m)]  #randsteps(n) from above
  for i in range(min(allr), max(allr)+1):
    print(str(i),"\t",str("|"*allr*count(i)))
