item = input("Enter Item ")
qty = float(input("Enter quantity "))

if item == 'a':
  unitprice = 10
else:
  unitprice = 20

extprice = qty * unitprice

print("Item: ",item)
print("Unit price: ",unitprice)
print("Extended price:", extprice)