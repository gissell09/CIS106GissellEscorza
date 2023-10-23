def comptuition(districtcode, credits):
  if districtcode == "I":
    tuition = 250 * credits
  elif districtcode == "O":
    tuition = 550 * credits
  else:
    return 0.0
  return tuition
totaltuition = 0.0

r = input("Do you want to compute tuition owed? (y/n) ")

while r == "y":
  lastname = input("Enter last name:  ")
  districtcode = input("Enter district code (use capitals): ")
  credits = float(input("Enter credits: "))
  tuition = comptuition(districtcode, credits)
  print("Student ",lastname, "owes a tuition amount of", tuition, "dollars")
  r = input("Do you want to compute tuition owed again? (y/n) ")
  totaltuition += tuition

print("Total tuition owed is", totaltuition, "dollars")


    
  
  