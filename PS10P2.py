r = input("Do you want to compute number of gallons needed? (yes or no) ")
while r == 'yes':
  length = float(input("Enter length: "))
  width = float(input("Enter width: "))
  height = float(input("Enter height: "))
  sqfoot = (2 * length * width) +( 2 * length * height) + (2 *width * height)
  gallons = (sqfoot / 50)
  print("You need", gallons, "gallons of paint.")
  r = input("Do you want to compute another number of gallons needed? (yes or no) ")
  
