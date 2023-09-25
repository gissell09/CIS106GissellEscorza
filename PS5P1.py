qtyofitem = float(input("Enter the quantity of the item "))

if qtyofitem <1000:
  unitprice = 5
else:
  unitprice = 3

extprice = qtyofitem * unitprice
tax = extprice * .07
total = extprice + tax

print("Quantity of the item: ",qtyofitem)
print("Unitprice: $",unitprice)
print("Extended price: $", extprice)
print("Tax amount: $",tax)
print("Total amount: $",total)