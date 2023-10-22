f = open("data.2.txt", "r")

c = 0 
totaltuition = 0.0

#get first part of the data

lastname = f.readline()

while lastname !="":
  dcode = f.readline()
  credits = float(f.readline())
  costpercredit = 250.0 if dcode == "I" else 500.0
  
  tuition = costpercredit * credits
  c = c + 1
  totaltuition = totaltuition + tuition
  print("Student:   ", lastname)
  print("Credits taken:   ",credits)
  print("tuition owed:   $",tuition)
  
  lastname = f.readline()

f.close()
print("Number of students:  ",c)
print("Total tuition owed:  $",totaltuition)