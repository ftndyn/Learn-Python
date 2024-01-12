# ============== DATE AND TIME FUNCTION ===================
# import datetime as dt # shortcut

# curDateTime = dt.datetime.now()
# curDateTime2 = dt.datetime.today()
# curDateTime3 = dt.datetime.now().strftime("%d-%m-%y")
# print(curDateTime)
# print(curDateTime2)
# print(curDateTime3)

# import datetime as dt
# curDateTime = dt.datetime.now()
# curDateTime2 = dt.datetime.today()
# curDateTime3 = dt.datetime.now().strftime("%d-%m-%y")
# print(curDateTime)
# print(curDateTime2)
# print(curDateTime3)

# # print(curDateTime.strftime("%d %b %Y %I:%M%p")) # 21 Dec 2023 11:00AM
# # print(curDateTime.strftime("%d/%m/%Y %X")) # 21/12/2023 11:00:53

# from datetime import datetime
# # # used to parse a string representing a data and time
# # # into a datetime object using the specified format
# dateExp = "2023-12-21 11:15:00"
# parseDate = datetime.strptime(dateExp, "%Y-%m-%d %X")
# print(parseDate)
# print(type(dateExp))
# print(type(parseDate))

# print(curDateTime.year)
# print(curDateTime.month)
# print(curDateTime.day)
# print(curDateTime.weekday())
# print(curDateTime.isoweekday())
# print(curDateTime.isocalendar())

# print(curDateTime.strftime("%A"))
# print(curDateTime.strftime("%a"))

# # dd/mm/YY
# from datetime import date
# today = date.today()
# d1 = today.strftime("%d/%m/%Y")
# print("d1 = ", d1)

# # Textual month, day and year
# today = date.today()
# d2 = today.strftime("%B %d, %Y")
# print("d2 =", d2)

# # mm/dd/y
# today = date.today()
# d3 = today.strftime("%m/%d/%y")
# print("d3 =", d3)

# # Month abbreviation, day and year
# today = date.today()
# d4 = today.strftime("%b-%d-%Y")
# print("d4 =", d4)

# # ================= File Handling ================= 
# # READ
# file = open("KISMEC.txt", "r") 
# print(file.read(5))
# print(file.read(10))
# print(file.readline())
# print(file.readline())

# for x in file: # read by line
#     print(x)

# file.close() #avoid buffer/problem

# # WRITE
# file = open("KISMEC.txt", "a") # append
# file.write("\nThis is to add content in the file using append")
# file.close()

# file = open("KISMEC.txt", "r")
# print(file.read())

# # OVERWRITE
# file = open("KISMEC.txt", "w") # append
# file.write("Now I Overwrite the contents.\nNo more at KISMEC")

# file = open("KISMEC.txt", "r")
# print(file.read())

# file.close()

# # CREATE
# file = open("KISMEC2.txt", "x")
# file.write("This is a new file text.")
# file.close()
# file = open("KISMEC3.txt", "a")
# file = open("KISMEC4.txt", "w")

# # DELETE
# Delete a file
# import os
# os.remove("KISMEC4.txt")

# # Check if a file exist
# import os
# if os.path.exists("KISMEC2.txt"):
#     os.remove("KISMEC2.txt")
# else:
#     print("The file do not exists!")

# # Delete Folder (can only remove empty folder)
# import os
# os.rmdir("myfolder")

# ================== ARRAYS ==============
# List
prog_language = ['python', 'C++', 'C', 'Java', 'R'] # string
# print(prog_language)
# print(len(prog_language))

# Data types
number_list = [1, 3, 9, 11, 76] # number
bool_list = [True, False, True, True] # boolean
mix_list = ['pyhton', 7, True, 'Java']
# print(mix_list)

os_list = list(('Windows', 'Linux', 'macOS'))
# print(os_list)
# print(type(mix_list))
# print(type(os_list))

# # Accessing List Item
# print(prog_language)
# print(prog_language[0:3])
# print(prog_language[-1])
# print(prog_language[-2:])
# print(prog_language[:])

# # Check Items
# if 'python' in prog_language:
#     print("Yes, it exists.")
# else:
#     print("No it doesn't exist.")

# Change items
# prog_language[4] = 'Ruby'
# print(prog_language)

# prog_language[2:4] = ['R', 'Javascript']
# print(prog_language)

prog_language[2:4] = ['C', 'SQL', 'python']
print(prog_language)

prog_language[2:4] = ['java']
print(prog_language)

# Add list items
prog_language.insert(0, 'ruby')
print(prog_language)

prog_language.insert(1, ['SQL', 'R'])
print(prog_language)

prog_language.append('R')
print(prog_language)

# mobileOS_list = ['android', 'ios', 'Windows Phone']

# os_list.extend(mobileOS_list)
# print(os_list)

# os_tuple = ('Unix', 'chrome OS')

# os_list.extend(os_tuple)
# print(os_list)

# # Remove Items
# prog_language.remove('R')
# print(prog_language)

# prog_language.pop(2)
# print(prog_language)

# prog_language.pop() # remove the last item
# print(prog_language)

# # Delete
# del prog_language[1]
# print(prog_language)

# del prog_language
# print(prog_language)

# print(mobileOS_list)
# mobileOS_list.clear()
# print(mobileOS_list)

# # Looping 
# print(os_list)

# for x in os_list:
#     print(x)

# for x in range(len(os_list)):
#     print(os_list[x])

# x = 0
# while x < len(os_list):
#     print(os_list[x])
#     x += 1

# # list comprehension
# [print(x) for x in os_list]

# newlist = []
# print(os_list)
# for x in os_list:
#     if 'W' in x:
#         newlist.append(x)
# print(newlist)

# # new_list = [expression for item in iterable if condition == True]
# newlist2 = [x for x in os_list if 'W' in x]
# print(newlist2)

# newlist3 = [x if x!='Linux' else 'Ubuntu' for x in os_list]
# print(newlist3)

# # Sorting 
# os_list.sort() # capital letter first
# print(os_list)

# # ascending order
# print(number_list)
# number_list = [100, 3, 84, 65, 4, 186]
# number_list.sort()
# print(number_list)

# # descending order
# number_list.sort(reverse=True)
# print(number_list)

# # customize sort
# os_list.sort(key = str.lower) # not case sensitive
# print(os_list)

# os_list.sort(key = len)
# print(os_list)

