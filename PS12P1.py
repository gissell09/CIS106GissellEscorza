def displayarrays(lname):
  for i in range (0, 10):
    print (lname[i])
  
def reversedisplay(lname):
  for i in range (9, -1, -1):
    print(lname[i])

lname = ["Smith", "Jones", "Williams", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Thomas",]

print("Last names:")
displayarrays(lname)
print("    ")
print("Last names reversed:")
reversedisplay(lname)

