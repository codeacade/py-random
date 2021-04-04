# more exercices from szkopul.edu.pl
# also mateuszrus.pl/matura-rozszerzona-z-informatyki/
# count a number of letters in random string

def lettercount(rstring):
 return {i:rsting.count(i) for i in rstring}  # returns dictionary from string / count number of each character

# "Divide and conquer"exercise for random number of "1" and "0":

#!/usr/bin/env pythoon

import random as rr  # to create random number like: "111111110000"

def st(n=10):             # size of random number (default 10)
  r1 = int(rr.random()*n)
  print(r1)
  stt = "1"*r1 + "0"*(n-r1)
  print(stt)              # shows random number like: "111111110000000"
  # nn is starting point from where we search left and right for "1" or "0"
  nn = 0
  # nnn is a step of how far we go for next search, half of what left
  nnn = int(n/2)
  while abs(nnn) > 0:
    if stt[nn + nnn] == "1":
      print((nn + nnn), " - this is 1")
      nn += nnn
      nnn = int(abs(nnn)/2)
    else:
      print((nn + nnn), " - this is 0")
      nn += nnn
      nnn = int(abs(nnn)/2)*(-1)
  nn+=int(stt[nn])
  return nn,"-",stt[nn]




# 3-level XML file parser using ElementTree:

def xmlparse(xmlfile):
  import xml.etree.ElementTree as et # ElemtTree required library
  
  rr = et.parse(xmlfile).getroot()
  
  for i in rr:
    print(i.tag + " - " + i.text)
    if len(i):    
      for j in i:
        print("-" + j.tag + " - " + j.text)
        if len(j):
         for k in j:
           print("--" + k.tag + " - " + k.text)
        
# Snippet to change individual XML element value
# Still need to find a way to check if element exist
# @inprogress

def newgg(file1, file2, element1, value1):
  import xml.etree.ElementTree as et
  
  try:  # in case missing file1
    source_tree = et.parse(file1)
  except:
    return "NO SUCH FILE: " + str(file1)
  source_root = source_tree.getroot()
  
  try:  # in case missing elemnt1 in file1
    print("Old value: " + source_root.find(element1).text)
  except:
    return "NO SUCH ELEMENT: " + str(element1) + " IN FILE " + str(file1)
  
  source_root.find(element1).text = value1
  print("New value: " + str(value1))
  print("Saved to new file: " + str(file2))
  source_tree.write(file2)
  
# end
    
    


