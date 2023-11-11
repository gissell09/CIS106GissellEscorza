def assessedvaluepercent(county):
  if county == "Cook":
    return 0.90
  elif county == "DuPage":
    return 0.80
  elif county == "McHenry":
    return 0.75
  elif county == "Kane":
    return 0.60
  else: 
    return 0.70

totalmarketprice = 0
totalassessedvalue = 0

r = input("do you want to compue the assessed value? (yes or no) ")
while r == "yes":
  county = input("Enter county(capitalize): ")
  marketprice = float(input("Enter market price: "))
  assessedvalue = marketprice * assessedvaluepercent(county)
  totalassessedvalue = totalassessedvalue + assessedvalue
  totalmarketprice = totalmarketprice + marketprice
  print("Market value: $",marketprice)
  print("Assessed value: $",assessedvalue)
  r = input("Do you want to compute another assessed value? (yes or no) ")

print("The sum of all market values is: $",totalmarketprice)
print("The sum of all assessed values is: $",totalassessedvalue)