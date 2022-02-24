# Hello World
print("Hello World")

# VARIABLES
age = 20
print(age)

# Practice: Change the value of age and print it out in the following space.



# Deep Dive: Different types of variables.
age = 20
price = 19.99 
first_name = "Mr. Doe"
is_online = True
print(first_name + " is " + str(age) + " years old")

# Exercise: Check in a new patient named James Smith, who is 20 years old.



# Input
name = input("what is your name")
print("Hello " + name)

# Type conversion
# Error: the input is read in as a string, which cannot be operated on with a number.
birth_year = input("Enter your birth year")
age = 2021 - birth_year
print (age)

# Fixing the code: convert string input to integer
birth_year = input("Enter your birth year")
age = 2021 - int(birth_year)
print (age)

# Exercise: Basic calculator. Adding two numbers



# Strings
# The string class contains a lot of built-in methods
course = 'Intro to Python'
print(course.find('i'))

# OPERATORS
# Arithmetic Operators

# Addition
print("10 + 3 = " + str(10 + 3))

# Subtraction
print("10 - 3 = " + str(10 - 3))

# Multiplication
print("10 * 3 = " + str(10 * 3))

# Division
print("10 / 3 = " + str(10 / 3))

# Division with integer
print("10 //3 = " + str(10 // 3))

# Modulus 
print("10 % 3 = " + str(10 % 3))

# Exponent
print("10 ** 3 = " + str(10 ** 3))

# Augmented operators
x = 10
x += 3
print(x)

# Operator Precedence
x = 10 + 3 * 2
print (x)

# Comparison Operators

# They return boolean (True/False) solutions

# Greater than
print("10 > 3: " + str(10 > 3))
# Greater than or equal to
print("3 >= 3: " + str(10 >= 3))
# Less than
print("10 < 3: " + str(10 < 3))
# Less than or equal to
print("10 <= 3: " + str(10 <= 3))
# Equal
print("10 == 3: " + str(10 == 3))
# Not equal
print("10 != 3: " + str(10 != 3))

# Logical Operators

# Used for building complex rules and conditions

# Using "and" check that a price is between two values
price = 25
print("Price between 10 and 30: " + str(price > 10 and price < 30))

# Using "or" check that a price is either of two values
price = 25
print("Price is either 10 or 30: " + str(price == 10 or price == 30))

# Using "not" check that a price is less than a value
price = 25
print("Price is less than 30: " + str(not price < 30))

# IF STATEMENTS

# Used to make decisions

# Print a message if the temperature is > 30
temperature = 35
if(temperature > 30):
    print("It's a hot day")
    print("Drink plenty of water")
# Everything below will be outside of the conditional statement
print ("Done")

# Practice: Add a condition for printing "It's a nice day" if the temperature is between 20 and 30

temperature = 25
if(temperature > 30):
    print("It's a hot day")
    print("Drink plenty of water")

# Exercise:
# Get weight as input
# Get unit as input (Kgs or Lbs)
# Display weight converted to the opposite unit



# LOOPS
i = 1
while i <= 1000:
    print(i)
    i = i + 1

# LISTS
# list of names
names = ["Jane", "John", "Mary", "Sam", "Safi"]
print(names)

# print the first three names

# Add a name at the head of the list

# List methods

numbers = [1, 2, 3, 4, 5, 6]
# Append

# Insert

# Remove

# Clear

# In 
print(10 in numbers)
# Len
print (len(numbers))

# FOR LOOPS

# Range function
numbers = [1, 2, 3, 4, 5,]
for item in numbers:
    print (item)

# The function can have 1 to 3 arguments.
# Generate numbers up to a value
numbers = range(5)
for number in numbers:
    print(number)

# Tuples

# Immutable (unchangeable) elements
numbers = (1, 2, 3)