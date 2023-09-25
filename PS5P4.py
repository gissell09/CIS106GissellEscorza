name = input("Enter name of appliance ")
cost = float(input("Enter cost of appliance "))

if cost > 1000:
  warrantee = cost * 0.10
else:
  warrantee = cost * 0.05

total = float(cost) + float(warrantee)

print("Name of appliance: ",name)
print("Cost of appliance: $",cost)
print("Cost of warrantee: $",warrantee)
print("Total cost: $",total)
