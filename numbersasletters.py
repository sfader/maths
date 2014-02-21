

ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = ["onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred", "sixhundred", "sevenhundred", "eighthundred", "ninehundred"]
thousands = ["onethousand"]
onesSum = 0.0
teensSum = 0.0
tensSum = 0.0
hundredsSum = 0.0
thousandsSum = 0.0
totalSum = 0.0

  
#count ones place
for i in range (0,len(ones)):
  onesSum = onesSum +len(ones[i])
  #print ones[i]
#print onesSum

#count teens
for i in range (0,len(teens)):
  teensSum = teensSum + len(teens[i])
 # print teens[i]
#print teensSum

#count tens place
for i in range (0,len(tens)):
  tensSum = tensSum + len(tens[i])
  #print tens[i]
  for j in range (0, len(ones)):
    tensSum = tensSum + len(tens[i]) + len(ones[j])
  #  print tens[i] + ones[j]
#print tensSum

#count hundreds place up to 20 eg. (101, 102, 102,... 201,202,203,....)
for i in range (0,len(hundreds)):
  hundredsSum=  hundredsSum + len(hundreds[i])
  for j in range (0,len(ones)):
      hundredsSum = hundredsSum + len(hundreds[i]) + len("and") + len(ones[j])
      print hundreds[i] + "and" + ones[j]
for i in range (0,len(hundreds)):
  for j in range (0,len(teens)):
      hundredsSum = hundredsSum + len(hundreds[i]) + len("and") + len(teens[j])
      print hundreds[i] + "and" + teens[j]

#count hundreds place from 20 - 99 eg. (121, 122.....221,222....)
for i in range (0,len(hundreds)):
  for j in range(0, len(tens)):
    hundredsSum = hundredsSum + len(hundreds[i]) + len("and") + len(tens[j])
    print str(hundreds[i]) + "and" +  str(tens[j])
    for k in range(0,len(ones)):
       hundredsSum = hundredsSum + len(hundreds[i]) + len("and") + len(tens[j]) +len(ones[k])
       print str(hundreds[i]) + "and" + str(tens[j]) + str(ones[k])

#count thousands place
for i in range (0,len(thousands)):
  thousandsSum = thousandsSum + len(thousands[i])
  print thousandsSum
totalSum = thousandsSum + hundredsSum + tensSum + teensSum + onesSum
 
print totalSum


