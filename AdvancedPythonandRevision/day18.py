"""Tupples"""

# Tuples: Are a list of objetcts that cannot be modified, ie, you cant add
# or remove a new item from a tuple

tup1 = (1, 2, 3, 4)

# you can access items within tuples, using indexing or slicing:
print(tup1[2])

print(tup1[::-1])

# You can concatenate two tuples:
tup2 = tup1 + (1, 3)

print(tup2)

# You can create repeated tuples like this:

tup4 = (1, 4)*10
print(tup4)

# Now lets say you want to convert a list to a tuple:

list1toTuple = tuple([1, 2, 3, 45, 3])
print(list1toTuple)

# also:
tup4 = 1, 2

print(type(tup4))

tup5 = 1,

print(type(tup5))

# Swapping variables:

x = 10

y = 2

# this creates a tuple, whic you are unpacking in the variables x and y
x, y = y, x

print(f"{x},{y}")
# to avoid writiing the redundant code below
# swap = 0

# swap = x

# x = y

# y = swap
# x, y = y, x creates a temporary tuple (y, x) → (2, 10)

# Then it unpacks that tuple so:

# x gets 2

# y gets 10
