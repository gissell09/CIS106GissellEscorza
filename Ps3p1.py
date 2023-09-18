#input phase
exam1grade = float(input("Enter Exam 1 score "))
exam2grade = float(input("Enter Exam 2 score "))
#process phase
Exam1score = 0.6 * exam1grade
Exam2score = 0.4 * exam2grade
totalpoints = Exam1score + Exam2score
#output phase
print("Total points earned is",totalpoints)