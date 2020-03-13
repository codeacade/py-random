# py-random
 import random
# use random module 
 random.choice((-1,1)) 
# unload (reload) module
 reload(module_name)
# one ball distribution in "n" steps
 sum([random.choice((-1,1)) for i in range(n)])
