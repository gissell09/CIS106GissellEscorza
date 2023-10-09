counter = 0 
response = input("Do you want to compute your exam average? (yes or no) ")
while response == "yes":
  counter = counter + 1
  lastname = input("Enter students last name: ")
  examscore1 = float(input("Enter students exam 1 score: " ))
  examscore2 = float (input("Enter students exam 2 score: "))
  averagescore = (examscore1 + examscore2) /2
  print("Student",lastname,"has an average score of",averagescore)
  response = input("Do you want to compute your exam average? (yes or no) ")

print("Amount of students who entered in data: ",counter)
