## Paper, rock, scissors game algortim

import random
ll = ['paper', 'rock', 'scissors'
     ]
for i in range(10):
  player1 = random.randint(0,2)
  player2 = random.randint(0,2)
  print(ll[player1],"=><"[(player1 - player2 + 3) % 3], ll[player2])
