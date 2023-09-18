#input phase
Purchaseprice = float(input("Enter the purchase price per share "))
Currentstockprice = float(input("Enter current stock price "))
Qtyofstock = float(input("Enter quantity of stock "))
#process phase
newvalueofstock = (Currentstockprice - Purchaseprice) * Qtyofstock
#output phase
print("The new value of the stock is ",newvalueofstock)