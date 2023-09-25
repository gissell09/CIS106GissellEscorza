numberofbooks = float(input("Enter number of books"))
costperbook = float(input("Enter cost per book"))

ordertotal = numberofbooks * costperbook

if ordertotal > 50:
  shipping = 0 
else:
  shipping = 25

print("The order total is $",ordertotal)
print("The shipping amount is $",shipping)