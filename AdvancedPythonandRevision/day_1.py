"""This module is based on my learning curve of python, it discusses primitive types"""

# Python offers different types of primitives

# Numbers, represented as ints or floats
NUM = 10
NUM2 = 2.99

# boolean values that can be set as true or false
BOOLEAN_VALUE = False
BOOLEAN_VALUE1 = True

# Strings to store a stream/array of chars
# Const values need to be Completely upper case
# string1 = "String1"

print(NUM)
print(NUM2)
print(BOOLEAN_VALUE)
print(BOOLEAN_VALUE1)

# print(string1)

# Strings are an array of chracters in python, which are immutable

message = "Welcome to my world of programming"

print("Printing first elment of the string: \\\"***\n**\"", message[0])
# Negative indexing starts from the last, unlike positive indexing
print(message[-1])
# Slicing: extracting a certain part from the whole string
print(message[0:4])
# not defining the end point in the slicing process,
#  will result in the remaining string from the starting point
print(message[3:])
# leaving an empty slice would produce a copy of the original string
print(message[:])

print(len(message))
