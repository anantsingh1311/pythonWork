"""List::Using Filter"""


def x(listofitems, *products):
    """creating a list of products dynamically"""

    print(listofitems)
    return list(products)


list_a = x("list a", ("Product a", 10), ("Product b", 8), ("Product c", 35))
# getting a sorted list using only lambda function
list_a.sort(key=lambda items: items[1], reverse=True)

print(list_a)

list_a_prices = list(map(lambda items: items[1], list_a))

print(list_a_prices)

# filter function: same as map function, used to filter output,
# based on a certain condition

filtered = list(filter(lambda item: item[1] >= 10, list_a))
print(f"{filtered}filtered list")

# Now we can use map and filter but they have complicated syntax and
# python provides list comprehensions to help solve this:
# [expression for item in list], the expression will print each item
# in the list provided within the for loop

# Now this is the same as the map function above,
# it wont use making an explicit list or using a for loop
# to print your items
list_a_prices = [item[1] for item in list_a]

print(f"new list comprehension func: {list_a_prices}")

# Now if I want to filter out my output based on a certain condition:
newFilter = [item for item in list_a if item[1] >= 10]
print(f"The new filtered list: {newFilter}")

# Zip functin: The zip() function in Python is used to
#  combine multiple iterables (like lists or tuples) element-wise into a new iterable of tuples.

list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))

# list1.pop()

print(list1)
