def calculatecommission(lastname, sales):
  highsalesrate = 0.10
  lowsalesrate = 0.05
  nextyearstarget = sales * 0.05
  if sales > 100000:
    commission = sales * highsalesrate
    return commission,nextyearstarget
  else:
    commission = sales * lowsalesrate
    return commission, nextyearstarget

lastname = input("Enter last name: ")
sales = float(input("Enter sales: "))
commission, nextyearstarget = calculatecommission(lastname, sales)

print("Last name:", lastname)
print("Commission:$", commission,)
print("Next Year's Target:$", nextyearstarget)

