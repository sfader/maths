# Sophie Fader project euler 30
# any number that can be written as the sum of its digits to the 5th power

succ = []
curr =0
total = 0

for i in range (2, 531441):
  curr = str(i)
  digsum = 0
  for k in range(0, len(curr)):
      digsum = digsum + (int(curr[k])**5)
  if i==digsum:
    total = total + digsum
print total