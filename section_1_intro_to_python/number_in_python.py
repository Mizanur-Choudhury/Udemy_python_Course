# In python, we have two types of numbers, integers (whole numbers) and floating point numbers
# (numbers with a decimal place).

age = 34  # (integers)
PI = 3.14159  # (float)

# Maths operations follow PEMDAS/BODMAS

# PEMDAS: Parentheses () -> Exponents ** -> Multiplication * ->
#                                               Division / -> Addition + -> Subtraction -

# BODMAS: (B-Brackets () -> O-Orders ** (powers/indices or roots) -> D-Division /
#                       -> M-Multiplication * -> A-Addition + -> S-Subtraction -)


# Python follows standard mathematics practices
# Following pemdas/bodmas, the following will resolve in the order of the following:
# 3*4 -> /2 -> +1 -> -2 = 5.0
maths_operations = 1 + 3 * 4 / 2 - 2
print(maths_operations)
# NOTE: When performing division in python, we will always return a float (5.0, from the above variable)

float_division = 12 / 3
print(float_division)
# NOTE: Even if the number is full number, a float is still returned (4.0)

# In order to remove the floating point, we use python's integer division //, This will remove the .0
integer_division = 12 // 3
print("Testing integer division " + str(integer_division))

# NOTE: float division does not round up or down the numbers, it only gets rid of it.
# EXAMPLE: The below returns as 2.6666666666666665
float_division = 8 / 3
print(float_division)

# EXAMPLE: The below returns as 2. And does not round up to 3
integer_division = 8 // 3
print(integer_division)
