#Aaron Jones
#9/26/23
#Calculates travel expenses

budget = int(input("Enter Budget: "))

dest = input("Where Ya Headin: ")

gas = int(input("Enter Gas Budget: "))

hotel = int(input("Enter Hotel Budget: "))

food = int(input("Enter Food Budget: "))

expenses = gas+food+hotel

print("---------Travel Expenses---------")
print("Location: ", dest)
print("Initial Budget", budget)
print()
print("Fuel", gas)
print("Hotel", hotel)
print("Food", food)
print()
print("Remaining Balance: ", budget-expenses)
