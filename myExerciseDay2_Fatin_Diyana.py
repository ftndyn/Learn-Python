# Exercise 1
# Add the loop and iteration for Day 1 Exercise 5, and stop when don't want to ask the age.

# def myAgeCategory(age): 
#     if age >= 0 and age < 5:
#         print("You are a Toddler.")
#     elif age >= 5 and age < 13:
#         print("You are a Kid.")
#     elif age >= 13 and age < 20:
#         print("You are a Teenager.")
#     elif age >= 20 and age < 60:
#         print("You are an Adult.")
#     elif age >= 60 and age <= 99:
#         print("You are a Senior Citizen.")
#     else:
#         print("Your age is invalid.")

# while True:
#     myAge = int(input("Please enter your age in range 0-99. Enter -1 to stop: "))
#     if myAge == -1:
#         break
#     myAgeCategory(myAge)


# Exercise 2
# Print the multiplication table for the number from 1 to 10 with int input

# num = int(input("Enter a number:"))
    
# for i in range(1,11):
#     print(num * i)
    

# Exercise 3
# Write a small program about the Order Food Menu.

# define function to calculate the price after discount
def discPrice(price):
    discountPrice = round((price * 0.90), 2)
    return discountPrice

# define function for menu
title = "MENU"
charLength, leftJust, rightJust = 34, 24, 8
foodMenu = ["Spaghetti Bolognese", "Spaghetti Carbonara", "Chicken Chop", "Lamb Chop", "Ice Blended Chocolate", "Ice Blended Vanilla", "Lemon Juice", "Watermelon Juice"]
foodPrice = [8.90, 8.90, 8.00, 17.00, 3.50, 3.50, 2.50, 2.50]
def menu():    
    print(title.center(charLength, "="))
    i = 0
    for menu in foodMenu:
        if i < len(foodPrice):
            print(str(i + 1) + "." + menu.ljust(leftJust, ".") + "RM", '%.2f' % foodPrice[i])
            i += 1

print("")
print("\nWelcome to Pok Mak Westeng!\n")
print("We have a New Year promotion of 10% discount if you spend MORE than RM25.00!!")
print("")

# Call function menu
menu()

# new list for ordered food input by user
foodOrder = []
foodCost =[]
foodQuantity =[]

# Get order input
nextOrder = True
totalPrice, counter = 0, 0
while nextOrder == True:
    numOrder = input("\nPlease select your order using number on the menu list (1-8). \n->Press c to checkout, \n->press m to display menu : ")
    if numOrder.isdigit() and int(numOrder) >=1 and int(numOrder) <=8:
        quantity = int(input(f"How many portions of {foodMenu[int(numOrder)-1]} would you like to order?"))
        foodOrder.append(foodMenu[int(numOrder)-1])
        foodCost.append(foodPrice[int(numOrder)-1])
        foodQuantity.append(quantity)
        totalPrice += (foodPrice[int(numOrder)-1]) * quantity
        counter += 1
    elif numOrder.lower() == 'c':
        nextOrder = False
    elif numOrder.lower() == 'm':
        menu()
    else:
        print("Invalid input. Please select a valid menu item.")
        continue

print(" ")
print("ORDER SUMMARY".center(charLength, "="))
k = 0
while k < counter:
    print(f"Item: {foodOrder[k]} \nQuantity: {foodQuantity[k]} \nCost: RM {'%.2f' % foodCost[k]}")
    k += 1

print("Total price is: RM", '%.2f' % totalPrice)
if totalPrice > 25.01:
    print("Price after discount is: ", '%.2f' % discPrice(totalPrice))