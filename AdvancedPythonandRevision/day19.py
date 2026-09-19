"""Arrays"""

from array import array

numbers = array("i", [1, 3, 8, 6])

numbers.append(3)

print(numbers)

numbers.pop()

print(numbers[1])

numbers.insert(0, 2)

print(numbers)

# Sets: Collection of items that doesnt allow duplicacy
print(f"{"X"*10}\n")
numbers = range(0, 5)

first = set(numbers)
second = {1, 7}

print("first", first)
print("Second", second)

# To find out length of the set
print(len(first))
first.add(8)

print(first)

# to remove an element from the set
first.remove(8)
print("first", first)
print("Second", second)

# performing set functions:
# Union prints all the elemnts of the first and second set
print("Union of first and second", first | second)
# Intesection prints only the common values among the first and second set
print("Intersection of first and second", first & second)
# Subtraction prints all the items of the first set that dont exist in the first and second:
print("Subtraction: ", first-second)
# Semantic subtraction: Includes all the items that are not common in the first and second
print("Semantic sub: ", first ^ second)
