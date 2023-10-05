#Aaron Jones
#10/5/23
#Introduction to dictionaries
#Inputing new user
name = input("Enter your name: ")
hair = input("Hair color: ")
eye_color = input("Eye color: ")
height = float(input("Enter height as a decimal: "))
age = int(input("Age: "))
favorite_food = input("Favorite food: ")

#Create a new dictionary
my_dic = {"Name": name, "Hair_Color": hair, "Eye_Color": eye_color, "Height": height, "Age": age, "Favorite_Food": favorite_food}

#Get values using the key
print(f"{my_dic['Name']} is a {my_dic['Height']} tall student with {my_dic['Hair_Color']} hair and {my_dic['Eye_Color']} eyes. They are {my_dic['Age']} years \
old and  their favorite food is {my_dic['Favorite_Food']}.")
