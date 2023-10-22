f = open("data.2.txt" , "r") #this opens the file

#initialize counters to 0 
totalextprice = 0.00 
c = 0

#get first data line 
item = f.readline().rstrip('/n') 

while item !="":
  qty = float(f.readline())
  price = float(f.readline())

  #calculate total extended price
  extprice = qty * price
  totalextprice = totalextprice + extprice
  c = c + 1
  print("Item is:            ", item)
  print("Quantity is:        ", qty)
  print("Price is          $:", price)
  print("Extended price is: $", extprice)
  item = str(f.readline().rstrip('\n'))


#after the loop: final calculatons and display them 

print("Total extended price is: $", totalextprice)
print("Number of orders:         ", c)
avg = totalextprice / c 
print("Average order:           $", avg)



  


