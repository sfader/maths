# sum of fifth power digits


# any number that can be written as the sum of its digits to the 5th power

# for loop through numbers, hold current number, make a list of current number digits, raise each digit to the 5th power, test equivalence
# make a list of successes 

succ = []
curr =0
total = 0


for i in range (2, 531441):
  curr = str(i)
  digsum = 0
  for k in range(0, len(curr)):
      digsum = digsum + pow(int(curr[k]),5)
  if i==digsum:
    succ.append(digsum)
for j in range (0, len(succ)):
  total = total + succ[j]

print total