# Exercise 1
# 1. User input(Ask birthday date) 
# 2. then calculate the age of user
# 3. Save the information to the file
# Main Method: Date and Time function and File Handling

import datetime

# user input
name = input("Welcome to Age Calculator.\nEnter your name: ")
birthdate = input("Enter your birthday (DD/MM/YYYY): ")

# Calculate age
today = datetime.date.today()
birthdate = datetime.datetime.strptime(birthdate, '%d/%m/%Y').date()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Save information to file
with open("user_Age.txt", "a") as file:
    file.write("Name: {}\n".format(name))
    file.write("Birthday: {}\n".format(birthdate.strftime('%d/%m/%Y')))
    file.write("Age: {}\n".format(age))
    file.write("=" * 30 + "\n")

print("Hello {}, your age is {}".format(name, age))
print("Your information has been saved to 'user_Age.txt'.")
