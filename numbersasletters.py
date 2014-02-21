

ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = ["onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred", "sixhundred", "sevenhundred", "eighthundred", "ninehundred"]
thousands = ["onethousand"]
ands = "and"
onesSum = 0.0
teensSum = 0.0
tensSum = 0.0
hundredsSum = 0.0
thousandsSum = 0.0

  
#count ones place
for i in range (0,len(ones)):
  onesSum = onesSum +len(ones[i])
print onesSum

#count teens
for j in range (0,len(teens)):
  teensSum = teensSum + len(teens[i])
print teensSum

#count tens place

for k in range (0,len(tens)):
  for l in range (0, len(ones)):
    tensSum = tensSum + len(tens[k]) + len(ones[l])
print tensSum

