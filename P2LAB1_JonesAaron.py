#Aaron Jones
#10/03/23
#Use Floats and Expressions to calculate gas costs

#Create input variables
mpg = float(input("Enter the car's mpg: "))
cost_per_gallon = float(input("How much a gal cost: "))

#Calculate gas costs based off gallons needed and price per gallon
#Calculate for 20 miles, 75 miles, 500 miles

cost_20 = (20/mpg) * cost_per_gallon
cost_75 = (75/mpg) * cost_per_gallon
cost_500 = (500/mpg) * cost_per_gallon
#Output values using f-string and format floats
print(f"{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}")
