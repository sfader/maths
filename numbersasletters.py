
# Sophie Fader, sosele, P.E. #17 

ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = ["onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred", "sixhundred", "sevenhundred", "eighthundred", "ninehundred"]
thousands = ["onethousand"]
totalSum = 0.0

  
#count ones place
for i in range (0,len(ones)):
  totalSum = totalSum +len(ones[i])

#count teens
for i in range (0,len(teens)):
  totalSum = totalSum + len(teens[i])

#count tens place
for i in range (0,len(tens)):
  totalSum = totalSum + len(tens[i])
  for j in range (0, len(ones)):
    totalSum = totalSum + len(tens[i]) + len(ones[j])

#count hundreds place up to 20 eg. (100, 101,...,119,...200, 201,....)
for i in range (0,len(hundreds)):
  totalSum=  totalSum + len(hundreds[i])
  for j in range (0,len(ones)):
      totalSum = totalSum + len(hundreds[i]) + len("and") + len(ones[j])
for i in range (0,len(hundreds)):
  for j in range (0,len(teens)):
      totalSum = totalSum + len(hundreds[i]) + len("and") + len(teens[j])

#count hundreds place from 20 - 99 eg. (121, 122.....221,222....)
for i in range (0,len(hundreds)):
  for j in range(0, len(tens)):
    totalSum = totalSum + len(hundreds[i]) + len("and") + len(tens[j])
    for k in range(0,len(ones)):
       totalSum = totalSum + len(hundreds[i]) + len("and") + len(tens[j]) +len(ones[k])
      
#count thousands place
for i in range (0,len(thousands)):
  totalSum = totalSum + len(thousands[i])


print totalSum


