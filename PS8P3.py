f = open("data.2.txt", "r")
totalbonus  = 0
c = 0
lastname = f.readline()


while lastname != "":
  salary = f.readline()
  print()
  print("Employees last name:  ",lastname)
  print("Employee salary: $", format(float(salary), '10,.2f'))
  bonus = float(salary) * 0.10
  print("Employee bonus: $", format(bonus, '10,.2f'))
  totalbonus = totalbonus + bonus
  c = c + 1
  lastname = f.readline()

f.close()
avgbonus = totalbonus / c 
print("  ")
print ("Average bonus:  $", format(float(avgbonus), '10,.2f'))




  

  


  


