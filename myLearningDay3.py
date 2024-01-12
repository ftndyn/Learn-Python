# # String are Arrays
# # Can identify column in data science

# example1 = "Python is good for everyone."
# print(example1[5]) # n
# print(example1[3:6]) # hon
# print(example1[3:8]) # hon i
# print(example1[:8]) # Python i
# print(example1[3:]) # hon is good for everyone
# print(example1[:]) # Python is good for everyone.
# print(example1[:-2]) # Python is good for everyon     (-) search from the back
# print(example1[-5:-2]) # yon

# # Converting a string
# example2 = "python is the best."
# print(example2.upper()) # PYTHON IS THE BEST.
# print(example2.lower()) # python is the best.
# print(example2.title()) # Python Is The Best.
# print(example2.capitalize()) # Python is the best.

# # How to remove white space
# example2 = " Python is the best. "
# print(example2)
# print(example2.strip().title())

# Find in a string
# print(example2.find('p'))
# print(example2.find('q')) # display -1 kalau tak wujud
# print(example2.find('t'))
# print(example2.find('the'))
# print(example2.find('e', 13, 16)) # find e that is between 13 and 16
# print(example2.index('h'))
# # print(example2.index('q')) # display error kalau tak wujud

# # Replace in a string
# print(example2.replace("Python is", "Anaconda is")) # must use exact word and case
# print(example2.replace("t", "a"))

# # Check existing in a string
# print("Python" in example2)
# print("Wakanda" in example2)

# age = 33
# exp3 = f"My age is {age}"
# print(exp3)

# print("My age is", age)

# print(f"My age is {age}")

# exp2 = "My age is {}"
# print(exp2.format(age))

# # Tuple
# fatherAge = 33
# myAge = 22
# sisterAge = 13
# exp4 = "My age is {0}. My father age is \b{2} and \tmy sister \age \\ is {1}." # My age is 22. My father age is33 and    my sister ge \ is 13.
# print(exp4.format(myAge, sisterAge, fatherAge))

# # DATE AND TIME FUNCTION
# import datetime as dt # shortcut

# curDateTime = dt.datetime.now()
# curDateTime2 = dt.datetime.today()
# print(curDateTime)
# print(curDateTime2)
# print(curDateTime.year)
# print(curDateTime.month)
# print(curDateTime.day)
# print(curDateTime.weekday())
# print(curDateTime.isoweekday())
# print(curDateTime.isocalendar())

# print(curDateTime.strftime("%A"))
# print(curDateTime.strftime("%a"))

# dd/mm/YY
from datetime import date
today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("d1 = ", d1)



