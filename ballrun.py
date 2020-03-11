import random
#######################################
# leng - length(height) of ball paths
# run - number for random runs
# symb - graphic symboe used to show ball path (default |)
#####################################

def rran(leng,run,symb="|"):
  
  # empty two dimentional table to collect results for all runs 
  #########################################
  rtable = [[] for i in range(leng)]
  
  # loop for number or random runs
  ##################################
  for i in range(run):
  
    # ball starting from posion=0
    ################################
    bpos = 0
    # loop for length(height) of ball paths
    ###############################################
    for j in range(leng):
      if bpos not in rtable[j]:
        rtable[j].append(bpos)
      bpos += random.choice((-1,0,1))
      
  # printing results from rtable
  ###############################
  for i in rtable:
    line = ["."]*40
    for j in i:
      # as results in rtable varied from <0 to >0 add 20 to center the chart
      # symbol by default | but ccan be changed
      ###########################################
      line[j+20] = symb[0]
    print("".join(line))
  
  #end
  
