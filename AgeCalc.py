# Exercise 1
# 1. User input(Ask birthday date) 
# 2. then calculate the age of user
# 3. Save the information to the file
# Main Method: Date and Time function and File Handling

import datetime

def calculate_age(birthdate):
    today = datetime.datetime.today()
    birthdate = datetime.datetime.strptime(birthdate, '%d/%m/%Y').date()
    age = today.year - birthdate.year 
    return age

def save_to_file(name, birthdate, age):
    with open('user_Age.txt', 'a') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Birthday: {birthdate}\n")
        file.write(f"Age: {age}\n")
        file.write("=" * 30 + "\n")

def main():
    # User input
    name = input("Welcome to Age Calculator.\nEnter your name: ")
    birthdate = input("Enter your birthday (DD/MM/YYYY): ")

    # Calculate age
    age = calculate_age(birthdate)

    # Save information to file
    save_to_file(name, birthdate, age)

    print(f"\nHello {name}! You are {age} years old.")
    print("Your information has been saved to 'user_info.txt'.")

if __name__ == "__main__":
    main()
