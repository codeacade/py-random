# more exercices from szkopul.edu.pl
# count a number of letters in random string

def lettercount(rstring):
 return {i:rsting.count(i) for i in rstring}  # iterate over the string and count number of each character


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
        
    
    


