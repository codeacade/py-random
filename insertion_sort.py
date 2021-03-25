def sort(array):
  aa=[array[0]]          # first number from array is first added to result
  for i in array[1:]:    # ommit first alredy added number
    for index,ii in enumerate(aa):
      if i > ii:       # test number is there is any lower already
        aa = aa[:index] + [i] + aa[index:]
        break
      if index == len(aa) - 1:  # add number as lowest if nothing is lower
        aa = aa + [i]
  print(aa[::-1])
