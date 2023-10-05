#Aaron Jones
#10/5/23
#Formatting floats

#Get float input from user

num1 = float(input("your_value: "))
num2 = float(input("your_value: "))
num3 = float(input("your_value: "))
num4 = float(input("your_value: "))

#Display values with f-string
#Display product and average with 0 decimal places

print(f'{num1*num2*num3*num4:.0f} {(num1+num2+num3+num4)/4:.0f}')

#Display the product and average with 3 decimal places

print(f'{num1*num2*num3*num4:.3f} {(num1+num2+num3+num4)/4:.3f}')



