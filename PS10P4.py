def ticketprice (miles):
  if miles >= 30:
    return 12
  elif 20 <= miles <= 29:
    return 10
  elif 10 <= miles <= 19:
    return 8
  else:
    return 5
totalticketprice = 0

r = input("Do you want to compute train ticket price? (yes or no) ")
while r == "yes":
  lastname = input("Enter last name: ")
  miles = float(input("Enter miles: "))
  currentticketprice = ticketprice(miles)
  totalticketprice = totalticketprice + currentticketprice
  print("Ticket price: $",currentticketprice)
  r = input("Do you want to compute the price of another train ticket? (yes or no) ")

print("Total of all tickets price: $",totalticketprice)
