# import unittest
```
class TestSum(unittest.TestCase): # new class TestSum based on TestCase

    def test_sum(self):
        self.assertEqual(sum(6, 4), 10, "Should be 10")

unittest.main()
```
# assertEqual() methods:
```
Method                    What it checks
assertEqual(a, b) 	       a == b
assertNotEqual(a, b) 	    a != b
assertTrue(x) 	           bool(x) is True
assertFalse(x) 	          bool(x) is False
assertIsNone(x) 	         x is None
assertIsNotNone(x) 	      x is not None
assertGreater(a, b) 	     a > b
assertLess(a, b) 	        a < b
assertIsInstance(a, b) 	  isinstance(a, b)
assertRaises(exception, function, arguments) 	The function raises the exception when given the arguments
```

# py-random
 import random
# use random module 
 random.choice((-1,1)) 
# unload (reload) module
 reload(module_name)
# reload in Python 3
 from importlib import reload<br />
 reload(module_name)
# one ball distribution in "n" steps
 sum([random.choice((-1,1)) for i in range(n)])
# PyGame
 https://www.alicja.it/2017/02/gra-w-pythonie-pygame-hello-world-1/
# SQLite
  https://mgurg.github.io/sql/2020/04/10/SQL-podstawy.html
# Practical SQLite
  https://www.sqlitetutorial.net/sqlite-commands/
  https://www.sqlitetutorial.net/sqlite-select/
