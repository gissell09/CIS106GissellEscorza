#input phase
priceformeal = float(input("Enter price of the meal "))
#process phase
tip15alone = priceformeal * 0.15
tip18alone = priceformeal * 0.18
tip20alone = priceformeal * 0.2
tip15total = priceformeal + tip15alone
tip18total = priceformeal + tip18alone
tip20total = priceformeal + tip20alone
#output phase 
print("                                         ")
print("With a 15% tip your total for the meal alone would be $",priceformeal)
print("Your tip amount would be $",tip15alone)
print("Your total for the meal and tip would be $",tip15total)
print("                                        ")
print("With a 18% tip your total for the meal alone would be $",priceformeal)
print("Your tip amount would be $",tip18alone)
print("Your total for the meal and tip would be $",tip18total)
print("                                         ")
print("With a 20% tip your total for the meal alone would be $",priceformeal)
print("Your tip amount would be $",tip20alone)
print("Your total for the meal and tip would be $",tip20total)
