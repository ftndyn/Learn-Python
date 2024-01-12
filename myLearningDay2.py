# # QnA conditional statement
# nombor = 20
# CGPA = 3.5
# huruf = "A"
# umur = 30

# if nombor > 10 and CGPA > 3.6:
#     nombor = 9999999
#     print("Nombor anda besar.")
# else:
#     print("Nombor anda TAK besar dan huruf bukan A")

# QnA Function
# umur = 0
# def calcAge(tahun):
#     global umur
#     umur = 2023 - tahun  
#     # print(umur)

# calcAge(1999)
# print(umur)

# # return - kembalikan variable ke luar, return focus kepada value sahaja
# def calcAge(tahun):
#     global umur
#     umur = 2023 - tahun 
#     return umur, tahun # paling bawah dan return banyak benda

# result = calcAge(1999)
# print(result)

# # keyword arguments (membantu kalau ada pelbagai variables) 
# def calcAge(tahun, jantina):
#     global umur
#     umur = 2023 - tahun 
#     return umur, tahun, jantina
# # print(calcAge("F", tahun= 1980)) - "F" consider as tahun, calcAge() got multiple values for argument 'tahun'
# print(calcAge(jantina = "F", tahun= 1980)) 

# # LOOPS AND ITERATIONS (repeat)
# # While Loops

# nombor = int(input("Enter a whole number: "))
# while nombor < 10:
#     print(nombor)
#     nombor += 1
#     # nombor = nombor + 1

# # Else statement in while loop
# nombor = int(input("Enter a whole number: "))
# while nombor < 10:
#     print(nombor)
#     nombor += 1
# else:
#     print("You've escaped the loop. The final number is", + nombor)

# # Break statement in while loop (emergency brake)
# nombor = int(input("Enter a whole number: "))
# while nombor < 10:
#     if nombor == 9:
#         break
#     print(nombor)
#     nombor += 1
# else:
#     print("You've escaped the loop. The final number is", + nombor)

# # Continue statement in while loop (jump one step)
# nombor = int(input("Enter a whole number: "))
# while nombor < 10:
#     # nombor += 1
#     if nombor == 8:
#         continue
#     print(nombor)
#     nombor += 1
# else:
#     print("You've escaped the loop. The final number is", + nombor)

# # For Loops
# skills = ["Python", "C++", "Arduino"]
# for skill in skills:
#     print(skill)

# # For Loops, else statements
# skills = ["Python", "C++", "Arduino"]
# for skill in skills:
#     print(skill)
# else:
#     print("You have no more skills.")

# # For Loops, break statements
# skills = ["Python", "C++", "Arduino"]
# for skill in skills:
#     print(skill)
#     if skill == "C++":
#         break
# else:
#     print("You have no more skills.")

# # For Loops, continue statements
# skills = ["Python", "C++", "Arduino"]
# for skill in skills:
#     if skill == "C++":
#         continue
#     print(skill)
# else:
#     print("You have no more skills.")

# # For Loops, continue, else, break statements combined
# skills = ["Python", "C++", "Arduino", "Public Speaking"]
# for skill in skills:
#     if skill == "Public Speaking":
#         continue
#     print("I am good at Hard Skill: " + skill)
#     if skill == "Nothing":
#         break
# else:
#     print("I will learn more new skills.")

# # For Loops, range functions
# for num in range(6):
#     print(num)
# print("")

# for num in range(2,6):
#     print(num)
# print("")

# for num in range(2,20,3):
#     print(num)
# print("")

# nombor = range(1000,2000,200)
# for num in nombor:
#     print(num)

# nombor = [0] # considered as list

# for num in range(-1,-16,-2):
#     print(num)
# print("")

# # Pass statement (tak buat apa-apa)
# for x in [0,1,2]:
#     pass

# # STRING
# print("")
# text1 = 'My first\'s sentence'
# print(text1)

# text2 = "My second \"sentence\"!"
# print(text2)
# print("")

# # Multiline string
# text3 = """3. This sentence has many lines,
# I want to separate them.
# So, I do this.

# """
# print(text3)
      
# text4 = '''4. This sentence has many lines,
# I want to separate them.
# So, I do this.

# '''
# print(text4)

# text5 = "5. This sentence has many lines, \nI want to separate them. \nSo, I do this.\n"
# print(text5)

# # Use backslash to separate long sentences
# print("Hi, I am a girl dfgdfgfffffffffffffffffffffffffffffffffffffffff \ fffff ggggggggggg")

# # Formatted string
# first = 'Python'
# last = 'Programming'

# message = first + ' ['+ last + '] for beginner.'
# print(message)

# msg = f'{first} [{last}] for Beginner.'
# print(msg)
# print("Yes, {} [{}] for beginner.".format(first, last))

# # Looping through a string
# for item in "Python":
#     print(item)

# # Print t in Python
# a = "Python"
# print(a[2])
    
# # String length
# course = "Python is the best"
# print(len(course))

# # Find a word inside a string
# course = "Python is the best"
# print('best' in course) # True
# print('forever' not in course) # True
# print('forever' in course) # False

# if 'best' in course:
#     print("Yes, best is here.")
