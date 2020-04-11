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
        
# Snippet to change individual XML element value
# Still need to fing a way to check if element exist
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
    
    


