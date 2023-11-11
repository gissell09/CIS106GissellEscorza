def msrp_percentoff(make, model,evc):
  if make == 'honda' and model == 'accord':
    return 0.10
  elif make == 'toyota' and model == 'Rav4':
    return 0.15
  elif evc == 'y':
    return 0.30
  else: 
    return 0.05
totalmsrp = 0
totalfinalprice = 0

r = input("Do you want to compute the out of door price? (yes or no) ")
if r == 'yes':
  make = input("What is the make of the car? ")
  model = input("What is the model of the car? ")
  evc = input("Is the car electric? (y or n) ")
  msrp = float(input("Enter msrp: "))
  newmsrp = msrp * msrp_percentoff(make, model,evc)
  finalmsrp = msrp - newmsrp + (msrp * 0.07)
  print("The final out of door msrp is: ", finalmsrp)
  totalmsrp = totalmsrp + finalmsrp
  totalfinalprice = totalfinalprice + finalmsrp
  r = input("do you want to compute another out of door price? (yes or no) ")

print("The tota msrp of all computed is: ", totalmsrp)
print("The total final out of door price of all computed is: ", totalfinalprice)


  
  

  
