# Exercise 1
# Create a meaningful variable name assign the value apple to it
# print apple

myFruit = "Apple"
print(myFruit) 

# Exercise 2
# Get user input to display the age category using condition statements. Age range : 0-99

print("Welcome to Age Category System! ")
myAge = input("Please enter your age in range 0-99: ")
myAge = int(myAge)

if myAge >= 0 and myAge < 5:
    print("Your age is in Toddler's category")
elif myAge >= 5 and myAge < 13:
    print("Your age is in Kids' category")
elif myAge >= 13 and myAge < 20:
    print("Your age is in Teenager's category")
elif myAge >= 20 and myAge < 99:
    print("Your age is in Adult's category")
else:
    print("Your age is invalid.")



# Exercise 3
# Scenario: Quality control in a Manufacturing Process
# Assume You are a qulity control engineer in a manufacturing company that produces electronic component.
# Your task is to inspect the produced components and determine their quality based on certain criteria.
# The criteria for determining the quality is as follow:
    
# If the component voltage is below 3.0V, it is considered "Low Voltage"
# If the component voltage is between 3.0V and 3.6V (inclusive), it is considered "Standard Voltage"
# If the component voltage is above 3.6V, it is considered "High Voltage"
    
myVoltage = float(input("Component Voltage:   "))
if myVoltage < 3.0:
    print("The component's voltage is low.")
elif myVoltage >= 3.0 and myVoltage <= 3.6:
    print("The component's voltage is standard.")
else:
    print("The component's voltage is high.")

# Exercise 4
# Create a calculate BMI function with the return method.
    
def myCalcBMI(weight, height):
    return weight / (height * height)

print("Welcome to BMI Calculator!")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

print("Your BMI is" , round(myCalcBMI(weight, height), 2))


# Exercise 5
# Create the function for Exercise 2

def myAgeCategory(age): 
    if age >= 0 and age < 5:
        print("You are a Toddler.")
    elif age >= 5 and age < 13:
        print("You are a Kid.")
    elif age >= 13 and age < 20:
        print("You are a Teenager.")
    elif age >= 20 and age < 99:
        print("You are an Adult.")
    elif age >= 60 and age <= 99:
        print("You are a Senior Citizen.")
    else:
        print("Your age is invalid.")

myAge = int(input("Please enter your age in range 0-99: "))
myAgeCategory(myAge)

# # Exercise 6
# # Define the function to check if a number is even or odd (user input)
def myEvenOddNum(num):
    remainder = num%2
    if remainder == 1:
        print(num, "is an odd number.")
    else:
        print(num, "is an even number")

inputNum = int(input("Please insert a number: "))
myEvenOddNum(inputNum)