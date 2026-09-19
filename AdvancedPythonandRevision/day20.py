"""Dictionaries"""

# Dictionaries are a key value pair sequence which can be defined in the following two ways:
point = {"X": 1, "Y": 2}
# or
point = dict(X=1, Y=2)
# To access a dictionary val:
print(point["X"])
# To add value:
point["Z"] = 11

print(point)

# if we try to access an element in the dict which doesnt exit,
# it results into an error
# the get method returns none if the key val pair doesnt exist
if "c" in point:
    print(point["c"])
else:
    print(point.get("c"))


# using for loops:
# for i in point:
#     print(i)

# to print the values as well we can re-write it as:

# for i in point:
#     print(i, point[i])
# above statement is not easy to understand and is also too complex and pylance reccomends using .items()
for key, value in point.items():
    print(value)
