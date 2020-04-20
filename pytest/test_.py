# this is testing file for PYTEST
# filename must start with "test_"
# PYTEST module must be added to python environment

# Testing functions from er.py file

def test_er():
  import er
  assert er.fib(9) == [2, 3, 5, 8, 13, 21, 34, 55, 89]
  assert er.fibmax(4) == [2, 3]
  assert er.fiblast(4) == 8
