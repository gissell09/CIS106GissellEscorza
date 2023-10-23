def CompExtPrice(qty, unitprice):
  extprice = qty*unitprice
  
  extprice * 0.1 if extprice > 10000.0 else 0.0
  
  return extprice

totalextprice = 0.0
r = input("Do you want to compute extended price? (y/n)? ")

while r == "y":
  qty = float(input("Enter quantity: "))
  unitprice = float(input("Enter unit price: "))
  extprice = CompExtPrice(qty, unitprice)
  totalextprice = totalextprice + extprice
  print("Extended Price is:   $", extprice)
  r = input("Do you want to compute extended price? (y/n)? ")

print("total extended price is:  $", totalextprice)
  
 
