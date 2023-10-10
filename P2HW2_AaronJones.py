#Aaron Jones
#10/10/23
#Working with lists

Module1 = float(input("Enter grade for Module 1: "))
Module2 = float(input("Enter grade for Module 2: "))
Module3 = float(input("Enter grade for Module 3: "))
Module4 = float(input("Enter grade for Module 4: "))
Module5 = float(input("Enter grade for Module 5: "))
Module6 = float(input("Enter grade for Module 6: "))

module_list = [Module1, Module2, Module3, Module4, Module5, Module6]
print("Lowest Grade: ", min(module_list))
print("Highest Grade: ", max(module_list))
print("Sum of Grades: ", sum(module_list))
print(f"Average:  {sum(module_list)/len(module_list):.2f}")
