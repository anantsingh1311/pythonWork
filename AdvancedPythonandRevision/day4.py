"""This python files works with numbers, diff types of operators and ops performed on numbers"""

# to perform more complex ops we use math module, which is a seprate file with python code in it
import math

# python offers three different types of numbers:
# 1
x = 10  # integers
x = 3.5  # floats
# complex numbers (rarely used in software dev, mostly in electrical or math ops)
x = 2+3j

# all standard procedures apply to them:

print(10+10)

print(10-1)

print(10*3)

print(10/3)  # performs a floating point division
print(10//3)  # performs integer division

# modulus operator to obtain remainder after div of two numbers
print(10 % 3)

# exponential operation to perform power functions like x^3 type stuff

print(10**3)

# Augmented assignment operator like += or -= or /= or *=
x += 10
print(x)

print("ceil", math.ceil(2.2))
print(math.floor(2.8))
print(abs(-2.3))

print(round(2.5))
