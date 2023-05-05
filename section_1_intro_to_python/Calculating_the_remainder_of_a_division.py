
"""
Maths lesson!!!
How does division work?

There are 3 main parts to a division's equation. With a 4th available as well.
8 / 2 = 4
13 / 5 = 2.6
# =================
8 = The dividend
The dividend is the number that will be divided
# =================

# =================
2 = The divisor
# =================
The divisor is the number that will be divided by the dividend

# ==================
4 = Quotient
# =================
The Quotient is the answer

# ================
6 = The Remainder
# ================
This is what is remaining.

13 / 5 = 2 R 3
2 comes from the dividend 13, divided 5 times. Leaving REMAINDER 3. This 3 is then divided 5 times, assuming we want to split
into smaller parts. Leaving us with 0.6. Combine to get  your Quotient 2.6
(13 / 5=X) = 2 (R=3 / X = 0.6) = 2.6

How to solve division problems!

Solving division problems are closely linked to multiplication, in order to solve division problems,
we will need to MULTIPLY the Quotient by the divisor, to see if it equals the dividend.

Example: 8 / 2 = 4
         4 x 2 = 8


"""

division = 13 / 5
print(division)

# inter division is used by // and drop all the numbers after the decibel place
integer_division = 13 // 5
print(integer_division)

# Python uses % know as the modulus. This will give you the REMAINDER of a division
# 13 / 5 = 2.(3) <---
remainder = 13 % 5
print(remainder)
