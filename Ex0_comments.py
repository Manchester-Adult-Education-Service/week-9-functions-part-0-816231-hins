# -------------------------------------------
# Exercise 0: Comments Practice
# -------------------------------------------
# In this exercise, you'll practice writing clear, helpful comments
# to explain Python code.
#
# Good comments should:
# - Explain WHAT the code does (not just repeat it)
# - Be clear and concise
# - Help someone else understand your code
#
# Below you'll find several code snippets.
# Add comments to explain what each section does.
# -------------------------------------------

# -------------------------------------------
# Task 1: Shopping Cart
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 1: Shopping Cart\n"
      + "-------------------------------------------")

# Add comments to explain this code:
#creating a list called cart
cart = ["apple", "bread", "milk", "eggs"]
total_items = len(cart)#creating a variable called total_items and store the all items from the cart

print(f"You have {total_items} items in your cart")# To print the total items in the cart

for item in cart:
    print(f"- {item}")

# -------------------------------------------
# Task 2: Grade Calculator
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 2: Grade Calculator\n"
      + "-------------------------------------------")

# Add comments to explain this code:
#create a variable called score to ask the user to enter your test score
score = int(input("Enter your test score: "))
#To check the grade whether pass or fail ,if score is above 70 pass 
if score >= 70:
    grade = "Pass"
else:
    grade = "Fail"
#print the grade
print(f"Your grade: {grade}")

# -------------------------------------------
# Task 3: Password Validator
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 3: Password Validator\n"
      + "-------------------------------------------")

# Add comments to explain this code:
#create a variabe name called password 
password = input("Create a password: ")
#To check the length of the password greater than 8
is_long = len(password) >= 8
#has_upper=Hinsha!=hinsha
has_upper = password != password.lower() # created a variable has_upper, checking password  contains uppercase
#has_lower=Hinsha!=HINSHA
has_lower = password != password.upper() #created a varible has_lower, checking password contains lowercase

is_valid = is_long and has_upper and has_lower #  To check password has more tha 8 letters,contains uppercase and lowercase

if is_valid: #if above condition is valid password acceopted or rejected.
    print("Password accepted!")
else:
    print("Password rejected. Must be 8+ characters with upper and lowercase letters.")

# -------------------------------------------
# Task 4: Even Number Counter
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 4: Even Number Counter\n"
      + "-------------------------------------------")

# Add comments to explain this code:

numbers = [12, 7, 18, 5, 22, 9, 14] #create a list called numbers
even_count = 0

for num in numbers: #for looping list of numbers
    if num % 2 == 0:
        even_count = even_count + 1

print(f"There are {even_count} even numbers in the list") #print the even numbers from the list.

# -------------------------------------------
# Task 5: Student Records
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 5: Student Records\n"
      + "-------------------------------------------")

# Add comments to explain this code:
#create a dictionary called student ,add name age and grades
student = {
    "name": "Alice",
    "age": 20,
    "grades": [85, 92, 78, 88]
}

average = sum(student["grades"]) / len(student["grades"])  #created variable called average and find the average
average = round(average, 2)           #Rounding the numbers and get decimals upto 2

print(f"Student: {student['name']}")   #print the student name
print(f"Age: {student['age']}")        #print the student age
print(f"Average grade: {average}")     #print the average

# -------------------------------------------
# Task 6: Countdown Timer
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 6: Countdown Timer\n"
      + "-------------------------------------------")

# Add comments to explain this code:

countdown = 5  #create a variable called countdown and set it to 5

while countdown > 0:  #To countdown from 5 until reaches to 1
    print(countdown)
    countdown = countdown - 1

print("Blast off!") # print "Blast off " when it reaches 1

# -------------------------------------------
# Task 7: Menu Formatter
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 7: Menu Formatter\n"
      + "-------------------------------------------")

# Add comments to explain this code:
# create a list called menu_items and add items 
menu_items = ["burger", "pizza", "salad", "pasta"]
counter = 1
 # To list items in menu_items
for item in menu_items: 
    formatted_item = item.upper()  #created a variable formated_item for items printed in upper
    print(f"{counter}. {formatted_item}") #print all the items from 1 and in uppercase
    counter = counter + 1

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you've added comments to all tasks:
# 1. Save your file
# 2. Open the terminal
# 3. Use Git to:
#    - Stage your changes
#    - Commit your changes
#    - Push your changes to the external repository
# Optional: Check GitHub to confirm your changes appear.
# -------------------------------------------
