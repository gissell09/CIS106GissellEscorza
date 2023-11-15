def calculateaverage(gs1,gs2,gs3,handicap):
  averagescore = (gs1 + gs2 + gs3) / 3
  averagescorehandicap = (gs1 + gs2 + gs3 + handicap) / 3
  return averagescore, averagescorehandicap

lastname = input("Enter last name: ")
gs1 = float(input("Enter game score 1: "))
gs2 = float(input("Enter game score 2: "))
gs3 = float(input("Enter game score 3: "))
handicap = float(input("Enter handicap: "))
averagescore,averagescorehandicap = calculateaverage(gs1,gs2,gs3,handicap)

print("    ")
print("Last Name:", lastname)
print("Average score:",averagescore)
print("Average score with handicap:",averagescorehandicap)
