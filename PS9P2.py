def compbatavg(hits, atbats):
  batavg = hits / atbats 
  if atbats ==0:
    return 0.00
  else:
    return hits / atbats
(c) = 0.0 

r = input("Do you want to compute a batting average? (y/n)? ")

while r == "y":
  lastname = input("Enter last name: ")
  hits = float(input("Enter number of hits: "))
  atbats = float(input("Enter number of at bats: "))
  batavg = compbatavg(hits, atbats)
  c = 1 + c
  
  print(lastname, "has a batting average of", batavg)
  r = input("Do you want to compute another batting average? (y/n)? ")

print("Total amount of players entered: ", c)
    
 
