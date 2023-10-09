totaldiscountamt = 0
response = input("Do you want to compute the final price? (yes or no) ")
while response == "yes":
  qty = float(input("Enter quantity: "))
  priceofitem = float(input("Enter price of the item: $"))
  extprice = qty * priceofitem
  discount = 0.25 if extprice > 10000 else 0.10
  discountamt = discount * extprice
  totaldiscountamt = totaldiscountamt + discountamt
  total = extprice - discountamt
  print("Extended price: $",extprice)
  print("Discount amount: $",discountamt)
  print("Total amount: $",total)
  response = input("Do you want to compute the final price? (yes or no) ")
  
print("Sum of all discounts: $",totaldiscountamt)