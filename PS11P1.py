def compdiscount (qty,price,discountrate):
  discountamt = qty * price * discountrate
  discountedprice = qty * price - discountamt
  return discountamt, discountedprice

qty = float(input("Enter quantity: "))
price = float(input("Enter price: "))
discountrate = float(input("Enter discount rate: "))

discountamt, discountedprice = compdiscount(qty,price,discountrate)

print("    ")
print("Quantity:",qty)
print("Price:$",price)
print("Discount amount:$",discountamt)
print("Discounted price:$",discountedprice)