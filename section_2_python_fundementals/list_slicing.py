# list slicing is the process of getting a part of a list
# you can use this to skip elements in a list

# [:] <--- List slicing syntax
# [Start here : to here]
# [:Start here]
# [Start here:]

friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]

print(friends[1:], "Testing [1:]")
# Return's all the list except the first element (skip's Rolf)

print(friends[:4], "Testing [:4]")
# Returns all the list except the forth element (skip's Jen)

print(friends[2:4], "Testing [2:4]")
# Returns all the list between the second and forth element (Starts at Anna, and Retrieves and stops at Bob)

print(friends[-3:4], "Testing [-3:4]")
# We can use minuses as well to start from the end of the list and work backwards. This starts at the third element
# from the back of the list (Anna) and grabs the forth element from the start of the list (Bob)

print(friends[-3:-4], "Testing [-3:-4]")  # INCORRECT!

"""
When using negative indexes we count from right to left, -1 being the last item in the list (”Jen”). 
Therefore, the position -4 belongs to “Charlie” and -3 to “Anna”.
When Python processes the slice, it starts from left to right, so it will first find -4 and then -3.
Because of that, the correct way to slice using negative indexes would be [-4:-3] instead of the other way around.

So, to get Rolf you would need to do:
friends[-5]
Or
friends[-5:-4]
"""

print(friends[-5:-4], "Testing [-5:-4]")

print(friends[:-4], "Testing [:-4]")
# Starts at the back of the list and skips four elements and returns Rolf

print(friends[-3:], "Testing [-3:]")
# Starts at the front of the list Third element from the start and returns Rolf

print(friends[:], "Testing [:]")
# This is used to create a new list (COULD BE VERY USEFUL!!!!)
