def displaystudentinfo(lname, scores):
  for i in range(len(lname)):
    print (lname[i], scores[i])
  
def reversedstudentinfo(lname, scores):
  for i in reversed(range(len(lname))):
    print(lname[i], "has a score of", scores[i])

lname = ["Smith", "Jones", "Williams", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Thomas",]
scores = [85,90,78,93,74,87,98,100,92,78]

print("Last names and scores:")
displaystudentinfo(lname, scores)
print("    ")
print("Last names and scores reversed:")
reversedstudentinfo(lname, scores)

