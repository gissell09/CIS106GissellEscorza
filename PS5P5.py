lastname = input("Enter last name ")
numofdependents = float(input("Enter number of dependents "))
grossincome = float(input("Enter gross income "))

adjgross = grossincome - numofdependents * 12000

if adjgross > 50000:
  tax = 0.20
else:
  tax = 0.10

incometax = tax * adjgross

if incometax < 0:
  incometax = 100

print("Last name:",lastname)
print("Gross income: $",grossincome)  
print("Number of dependents: ",numofdependents)
print("Adjusted gross income: $",adjgross)
print("Income tax: $",incometax)
  