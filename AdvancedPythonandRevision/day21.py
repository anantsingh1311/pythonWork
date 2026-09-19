"""Dictionary comprehensions"""


# lambda param: expression you want to return
# map: map(function,iterable)
print(list(map(lambda i: i*2, range(5))))
# filter: filter(function with some conditions, iterable)
print(list(filter(lambda i: i*3 < 5, range(5))))
# list comprehensions:
# list comprehension for maping a list to i*2 values of a list
a = [i*2 for i in range(5)]
print(a)
# filtering a list based on a condition using list comprehension
b = [i for i in range(5) if i*3 < 5]
print(b)

# list comprehension: [expression for i in iterable]
# expression is what gets output-ted by the console
# for ever item i in the iterable, i is basically each item within the list

# Now if I want to create a dictionary comprehension:
values = {nums for nums in range(5)}
# the above gives a set but if we do this:-
values = {nums: nums*20 for nums in range(5)}
# the above statement will generate key value pairs
print(values)


list_items = [("Product1", 10), ("Product5", 4), ("product8", 24)]


# def sort_items(i):
#     return i[1]

list_items.sort(key=lambda items: items[1])

a = list(map(lambda items: items[1], list_items))

print("Only price list", a)

a = list(filter(lambda items: items[1] >= 10, list_items))
print("greater than 10 list", a)
