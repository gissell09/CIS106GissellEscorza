def compgrosspay(jobcode, hours):
  if jobcode == 'L':
      payrate = 25.0
  elif jobcode == 'A':
      payrate = 30.0
  elif jobcode == 'J':
      payrate = 50.0
  else:
      return 0.0
    
  if hours > 40:
    regularhours = 40
    overtimehours = hours - 40
    overtimepay = payrate * 1.5
    grosspay = (regularhours * payrate) + (overtimehours * overtimepay)
  else:
     grosspay = hours * payrate
  return grosspay
    
totalgrosspay = 0.0

r = input("Do you want to compute grosspay? (y/n) ")

while r == "y":
  lastname = input("Enter last name: ")
  jobcode = input("Enter job code: ")
  hours = float(input("Enter hours worked: "))
  grosspay = compgrosspay(jobcode, hours)
  totalgrosspay += grosspay
  print(lastname, " has a gross pay of $",grosspay)
  r = input("Do you want to compute grosspay again? (y/n) ")

print("The total grosspay amount is $",totalgrosspay)
  
  
    
  
  