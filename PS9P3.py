def compbatavg(miles, gallons):
  mpg = miles / gallons
  if gallons == 0:
    return 0.0
  else: 
    return miles / gallons
c = 0.0

r = input("Do you want to compute miles per gallons? (y/n)? ")

while r == "y":
  city = input("Enter destination city:  ")
  miles = float(input("Enter miles:      "))
  gallons = float(input("Enter gallons:  "))
  mpg = compbatavg(miles, gallons)
  c = c + 1
  print("   ")
  print("Destination city: ",city)
  print("Miles traveled: ", miles)
  print("Miles per gallons: ", mpg)
  r = input("Do you want to compute another set of miles per gallons? (y/n)? ")

print("Total amount of entries made:  ",c)
  
