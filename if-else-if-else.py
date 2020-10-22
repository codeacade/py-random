#  Short one-liner for complex if-elxse-if-else

def ii(x):
  if x < 0:
    print("D")
  else:
    if x > 0:
      print("E")
    else:
      print("N")

def jj(x):
  print("D" if x < 0 else "E" if x > 0 else "N")
