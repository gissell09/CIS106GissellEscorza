#input phase
fixedcosts = float(input("Enter the fixed costs "))
priceperunit = float(input("Enter the price per unit "))
costperunit = float(input("Enter the costs per unit "))
#process phase
breakevenpoint = fixedcosts / (priceperunit - costperunit)
#output phase
print("Your break even point is",breakevenpoint)