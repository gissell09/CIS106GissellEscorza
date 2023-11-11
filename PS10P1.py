def forcastpercent(month):
  if month == "January" or month == "Febuary" or month == "March":
    return 0.10
  elif month == "April" or month == "May" or month == "June":
    return 0.15
  elif month == "July" or month == "August" or month == "September":
    return  0.20
  elif month == "October" or month == "November" or month == "December":
    return 0.25
  else:
    return 0

r = input("Do you want to compute next months sales? (yes or no) ")

while r == "yes":
  lastname = input("Enter last name: ")
  month = input("Enter month (capitalize month): ")
  sales = float(input("Enter sales: "))
  nextmonthsales = sales * (1 + forcastpercent(month))
  print(lastname, "'s next months sales will be ",nextmonthsales)
  r = input("Do you want to run the program again? (yes or no) ")