# variables are what we use in python to set the information that we are going to us in our program and
# retrieving/using it.
# The syntax for variables is typed text followed by a = and the user input Example: VARIABLE = miz
age = 30

# in order to print the user text we can use print() and in the brackets, input our variable or a input directly
# Example: print(VARIABLE)
# Example: print(30)

print(age)
print(30)

# If we have the same variable which is assigned to different values, python will return the
# last version (line 15's print)
friend_age = 23
friend_age = 25

print("im testing the variable friend_age " + str(friend_age))

# However, if we use the same variables but have a print statement under each one,
# we will return the first instance of the variable as seen below!
# at first, we're assigning the name x to the value 25,
# and then afterwards we're "moving" that name,
# and assigning it to the value 30. We run code from top to bottom so each print uses only the most current value.

x = 25
print(x)
x = 30
print(x)

# in python, we use underscores to separate words in longer variables. This is called SNAKE CASE
countries_visited = 90

# We can also use numbers in our variables, however WE CAN'T USE VARIABLES that start with numbers!
countries_visited_v2 = 93

# We can also name a variable starting with an underscore
_age = 30

# We can also use capital letters in the middle of the variable, this is known as CAMEL CASE
myVariable = 30

# HOWEVER, WE CAN NOT USE SPECIAL CHARACTERS IN VARIABLE NAMES!


# in python, the best practices is if you have variables that will never change,
# the code should be register in upper case
PI = 3.14159

RADIANS_TO_DEGREES = 180 / PI

print(RADIANS_TO_DEGREES)
