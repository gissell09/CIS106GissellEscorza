p = float(input("Enter Principle "))
r = float(input("Enter rate "))
totalint = 0 


print("Year   Beginning balance   end balance")

for x in range(1, 6, 1):
  i = p * r 
  totalint = totalint + i
  endbal = p + i
  print(x, "        ", p, "       ",endbal)
  p = endbal

print("total interest earned:  ",totalint)
