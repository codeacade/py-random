######################################################
##  This is tool to extract cookie partners
##  addresses from coolie plugin on nczas.com website
######################################################

fileName = input("What filename: ")
textSearch = input("What text: ")
from random import randint


def rr(fname, tsearch):
  """ text search tool """
  
  textFile = open(fname)
  textFileContent = textFile.read()
  textFile.close()
  
  newTextFile = open(fname + "_" + str(randint(1,999))reload, "w")
  
  print("size lenght: ", len(textFileContent))
  textpos = 0
  textcount = 0
  textpos = textFileContent.find(tsearch)
  
  while textpos + 1:
    textcount += 1
    textFound = textFileContent[textpos:textpos + 100]
    textFound = textFound[:textFound.find("\"")]
    print(textFound)
    newTextFile.write(textFound + "\n")
    textpos = textFileContent.find(tsearch, textpos + 1) # for NEXT while


  newTextFile.close()
  print(f"\n {textcount} instances of \"{tsearch}\" found in {fileName}.\n")

  
rr(fileName, textSearch)
