

ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = ["one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
thousands = ["one thousand"]

lSum = 0.0

for i in range (0,9):
  lSum = lSum +len(ones[0])
  print lSum
