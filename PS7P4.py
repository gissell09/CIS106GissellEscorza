counter = 0 
totalgrosspay = 0.0
response = input("Do you want to compute your gross pay? (yes or no) ")
while response == "yes":
  counter = counter + 1
  lastname = input("Enter employees last name: ")
  hours = float(input("Enter hours worked: " ))
  rateofpay = float (input("Enter rate of pay: "))
  grosspay = hours * (rateofpay * 1.5) if hours > 40 else hours * rateofpay
  totalgrosspay = totalgrosspay + grosspay
  print("Employee",lastname,"has a gross pay of: $",grosspay)
  response = input("Do you want to compute your gross pay? (yes or no) ")

print("Amount of employees who entered in data: ",counter)
print("The total gross pay is : $",totalgrosspay)
averagepay = totalgrosspay / counter 
print("The average gross pay is: $",averagepay)