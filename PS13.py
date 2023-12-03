#main
def dil (mylist):
  n = int(input("Enter the number of items in the list: "))
  for n in range (0,n,1):
    s =int(input("Enter an integer: "))
    mylist.append(s)
  return mylist
def displaylist(mylist):
  for item in mylist:
    print(item)
mylist = []
mylist = dil(mylist)
displaylist(mylist)
print(mylist)

#d2
mylist.insert(0,99)
print(mylist)

#d3
mylist[0] = 100
print(mylist)

#d4
mylist2 = [500, 600, 700, 800, 900]
print(mylist2)
mylist.extend(mylist2)
print(mylist)

#d5
mylist.remove(800)
print(mylist)

#d6
del mylist[2]
print(mylist)

#d7
mylist3 = ["A","A","B","D","C"]

#d8
print("Count of A's in list: ", mylist3.count("A"))

#d9
print("Index of B in the list: ", mylist3.index("B"))

#d10
mylist3 = ["A","A","B","D","C"]
if 'F' not in mylist3:
  print("F is not in 'mylist3'")

#d11
mylist2 = [500, 600, 700, 800, 900]
mylist2.clear()
print(mylist2)

#d12
mylist2 = [500, 600, 700, 800, 900]
del mylist2
print(mylist2) #this causes the error along the whole program so just put a hashtag in 
               # front of the print statement to continue the rest of the code

#d13
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

#d14
players.sort()
print(players)

#d15
players2 = players.copy()
print(players2)

#d16
players.reverse()
print("Original: ",players)
print("Copy: ",players2)



  

