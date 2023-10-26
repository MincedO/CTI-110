#Aaron Jones
#10/26/23
#Uses if/else statements

#Get employee name for user
name =(input("Enter employee's name: "))
#Get number of hours from the user
hours = float(input("Enter number of hours worked: "))
#Get payrate per hour from user
payrate = float(input("Enter employee's pay rate: "))
#Determine if employee worked more than 40 hours
if hours > 40:
    OT_hours = hours - 40
else:
    OT_hours = 0
#Calculate regular hours worked
if hours <= 40:
    Reghours_worked = hours
else:
    Reghours_worked = 40
#Calculate pay for regular hours
RegHour_Pay = Reghours_worked * payrate
#Calculate overtime hours

#Calculate overtime pay
OT_pay = OT_hours *(payrate * 1.5)
#Display name, payrate, regular hours, overtime hours, overtime pay, and gross pay
gross_pay = OT_pay + RegHour_Pay
print("Employee name: ", name)
print("Hours Worked: ", hours)
print("Pay Rate: ", payrate)
print("OverTime: ", OT_hours)
print("OverTime Pay: ", OT_pay)
print("RegHour Pay: ", RegHour_Pay)
print("Gross Pay: ", gross_pay)
