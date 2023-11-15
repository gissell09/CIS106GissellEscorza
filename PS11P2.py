def compscore(ex1,ex2,ex3):
  totalpoints = ex1 + ex2 + ex3 
  averagescore = totalpoints / 3
  return averagescore, totalpoints

lastname = input("Enter students last name: ")
ex1 = float(input("Enter students exam one score: "))
ex2 = float(input("Enter students exam two score: "))
ex3 = float(input("Enter students exam three score: "))
averagescore, totalpoints = compscore(ex1,ex2,ex3)

print("   ")
print("Students last name:",lastname)
print("Students total points:",totalpoints)
print("Students average score:",averagescore)
  
  
