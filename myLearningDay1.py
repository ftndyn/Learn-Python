# Testing Python Comment
"""
print("Hello")
print("Hello")
print("Hello")
"""

# # INDENTATIONS
# if 10 > 2:
#     print("10 is greater than 2") 

# # VARIABLES
# x = 5
# y = "John"
# z = "Hi"
# print(x, y, z)

# # Casting purpose
# a = "John"
# b = 5
# x = str(5)
# y = int(5)
# z = float(5)
# print(x, y, z)
# print(type(a)) # check the type of variables
# print(type(y))

# # Variable names 
# a = "John"
# X = 5       # case sensitive
# x = str(5)
# y = int(5)
# z = float(5)
# print(x, X)

# myvar = 'Alex'
# myVar = 'Alex'
# myVar2 = 'Alex'
# my_var = 'Alex'
# _my_var = 'Alex'
# MYVAR = 'Alex'

# print(myvar, myVar, myVar2, my_var, _my_var, MYVAR)

# # Cannot start with:
# 2myVar = 'Alex' (number)
# my-var = 'Alex' (dash)
# my var = 'Alex' (space)
# print(2myVar, my-var, my var)            # Invalid syntax

# x, y, z = "Alex", "John", "James"
# print(x, y, z)

# x = y = z = "Alex"
# print(x, y, z)

# x = "My name "
# y = "is "
# z = "Fatin Diyana."
# print(x + y + z)

# X = 10
# Y = 5
# print(X+Y)

# # print(x + X) # syntax error because different type 
# print(x, X) # separate with a comma for different type of variable

# x = ["apple", "banana", "cherry"]
# print(type(x))

# # Convert data type
# Y = 5
# a = float(5)
# print(Y, a)
# print(type(Y))
# print(type(a))

# # Print random number and specify the range
# import random
# print(random.randrange(1,10))

# # Specify variable type
# x = int(1)
# y = int(2.8)
# z = int("5")

# print(x, y, z)
# print(type(x))
# print(type(y))
# print(type(z))

# x = float(1)
# y = float(2.8)
# z = float("5")

# print(x, y, z)
# print(type(x))
# print(type(y))
# print(type(z))

# x = str(1)
# y = str(2.8)
# z = str("5")

# print(x, y, z)
# print(type(x))
# print(type(y))
# print(type(z))

# # OPERATORS
# # Arithmetic Operators
# print((30 + 2) - (6 * 2))
# print(5%2)
# print(2**3)
# print(10//3)

# a = 5
# print(a)

# a += 3
# print(a)

# a = a + 3
# print(a)

# b = 5
# print(b)

# b -= 3
# print(b)

# # Comparison Operators
# print(1 == 10) # False
# print(1 != 10) # True
# print(1 > 10) # False
# print(1 >= 10) # False
# print(1 < 10) # True
# print(1 <= 10) # True

# # Logical Operators
# x = 10
# print(x>3 and x<20) # True
# x = 30
# print(x>3 and x<20) # False
# x = 30
# print(x>3 or x<20) #True
# x = 30
# print(not(x>3 or x<20)) #False

# # CONDITION STATEMENTS
# if 1 > 10:
#     print("This is true")
# elif 10 == 10:
#     print("This is true")
# else:
#     print("This is false")

# print("Always execute")

# Nested If
x = 30

if x > 10:
    print("Above 10")
    if x > 20:
        print("Also above 20")
    else:
        print("but not above 20")
else:
    print("Less than 10")

# x = 5

# if x > 10 and x < 20:
#     print("Greater than 10 but less than 20")
# else:
#     print("It is false")

# # This method susah nak faham dan nak tambah statements
# print("Greater than 10 but less than 20") if x > 10 and x < 20 else print("It is false")
 
# name = "Alexx"

# if name == "John":
#     print("My name is John")
# elif name == "Alex":
#     print("My name is Alex")
# else:
#     # print("My name is Alexx")
#     pass

# # INPUT F
# print("What is your name: ")
# print("Hello " + username)

# username = input("What is your name: ")
# if username.isalnum(): # accept string only
#     print("Hello " + username)
# else:
#     print("Invalid")
    
# The Python isalpha() method returns true if a string only contains letters. Python isnumeric() returns true if all characters in a string are numbers. Python isalnum() only returns true if a string contains alphanumeric characters, without symbols

# # FUNCTION
# # Without Input, without arguments
# def myFirstFunction():
#     print("Hi, I am a newbie ^^")

# myFirstFunction()

# # Number Arguments
# def myFirstFunction(fname, lname):
#     print(fname + " " + lname)

# myFirstFunction("James", "Kelvin")
# myFirstFunction("Joe", "Alex")

# # Arbitrary Arguments (if the number of Arguments is unknown)
# def myFirstFunction(*fname):
#     print("The winner is " + fname[2])

# myFirstFunction("James", "Kevin", "John", "Alvin")

# # Keyword Arguments (key = value syntax)
# def myFirstFunction(fname, mname, lname):
#     print("I like this name: " + lname)

# myFirstFunction(fname = "James", mname = "Kevin", lname = "John")

# # Arbitrary Keyword Arguments (if the arguments number is unknown, use ** to receive dictionary arguments)
# def myFirstFunction(**people):
#     print("The winner last name's is " + people["lname"])

# myFirstFunction(fname = "James", mname = "Kevin", lname = "John")

# # default parameter value
# def myFirstFunction(country = "Malaysia"):
#     print("I come from " + country)

# myFirstFunction("Indonesia")
# myFirstFunction()
# myFirstFunction("Singapore")

# # return function
# def myReturnFunc(x):
#     return 10 * x

# print(myReturnFunc(9))
# myReturnFunc(3) # tak print return value 
# print(myReturnFunc(2))

# Global variable used in function example
# x = "newbie"

# def myFirstFunction():
#     print("Hi, I am a " + x)

# myFirstFunction()