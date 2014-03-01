# sum of fifth power digits


# five digit numers 10000 >= x <= 99999

# for loop through numbers with five digits, hold current number, make a list of current number digits, raise each digit to the 5th power, test equivalence
# make a list of successes 

succ = []
curr =0

for i in range (10000, 10500):
  curr = str(i)
  digsum = pow(int(curr[0]),5) + pow(int(curr[1]),5) + pow(int(curr[2]),5) + pow(int(curr[3]),5) + pow(int(curr[4]),5)
  #print i, digsum
  if i==digsum:
    succ.append(digsum)
print succ