total = 0.0
tax = 0.0

def comptotal(qty,unitprice):
  global total
  total = qty * unitprice
  global tax
  tax = total * 0.07
  return total, tax

qty = float(input("Enter quantity:"))
unitprice = float(input("Enter unit price:"))
comptotal(qty,unitprice)
print("Your total is:$",total)
print("Your tax is:$",tax)



  
  