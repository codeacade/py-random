#!/usr/bin/env pythoon

import random as rr

def sfile(fname):
  num = open(fname,"w")
  num.write(",".join([str(int(rr.random() * 10000)) for i in range(100)]))
  num.close()

# Save and read list of numbers from the file
# Calculate how often specific digits appear in all numbers

# Sample list of random numbers (as strings):

www = ['5200', '7472', '3353', '9087', '533', '6738', '6196', '3306', '9404', '7799', '9037', '587', '3341', '1756', '7238', '4826', '1012', '8498', '8974', '1873', '7490', '761', '6415', '507', '4046', '3549', '655', '8149', '3270', '8041', '2402', '7960', '4608', '142', '4503', '8424', '1384', '507', '4989', '5431', '1509', '5276', '2532', '6884', '9261', '1422', '9243', '6212', '9136', '149', '3898', '1031', '3895', '6931', '4728', '8770', '4390', '8737', '3629', '8901', '9528', '1434', '9823', '225', '3342', '3499', '7243', '9007', '1179', '3852', '4633', '4292', '1578', '9053', '8350', '2053', '9550', '876', '906', '7705', '2027', '3729', '5714', '4', '9622', '6926', '3295', '9519', '3544', '5683', '7046', '5581', '9410', '8999', '4143', '7200', '2827', '6686', '1089', '2357']  

#  Produce lll file with number of digits in each string above:

lll = []
for numb in www:
  lll.append({i:numb.count(i) for i in numb})  #  Use hash to remove duplicated digits

#  reading a pre-counted file with primes
#  ensure 100k.txt and 10k.txt in same locaton

file100 = open("100k.txt")
data100 = file100.read().split("\n")
file100.close()


ww2 = []
def ww2do(inp):
  for i in inp:
    for l in i:
      if i.count(l) == 2:
        ww2.append(i)
        break

same = []
def find(inp): # use data100 from line 23
  for i in inp[:90000]:
    for l in i:
      if i.count(l) > 1:
        same.append(i.replace(l,"*"))
        break

sams = {}
def fins(inp): # use data100 from line 23
  for i in inp[:2000]:
    for l in i:
      if i.count(l) > 1:
        sams[i] = (i.replace(l,"*"))
        break

def fond():
  for i in range(70000):
    if same.count(same[i]) > 5:
      print(i, " - ", same[i], " - ", same.count(same[i]))








