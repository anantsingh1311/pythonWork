"""Data Structures- List"""

# List is a form of data structure that comprises of a sequence of various types of objects
# these objects can be of type number,booleans, strings and lists itself

# num = [1, 2, 3]
# alphabets = ["a", "b", "c"]

# print("\n", num)
# print("\n", alphabets)


# # Now lists can have lists within them as well:
# matrix = [[1, 2], [3, 4]]

# # above is a list of 2 lists within it, which basically means a 2x2 matrix
# print("\n", matrix)

# # you can also concatenate two lists of different types together to form one list:
# combine = num + alphabets

# print("\n", combine)

# # Now lets say you want to create a list of 100 zeros or anything of as such,
# # Instead of hardcoding each value you could use:
# hundered_zero_list = [0]*100

# print("\n", hundered_zero_list)

# # Lets say a range of numbers need to be implemented within a list so we can:
# nums = list(range(20))

# print("\n", nums)

# accesing elements in a list:
# numbers = list(range(20))

# # print(f"original list: {numbers}")

# # print(numbers[1])

# # print(numbers[0])

# # # slicing a list works like: sequence[start:stop:step]
# # print(numbers[2:3])
# # # if the stop value isnt defined the sequence will produce
# # all the remaining values from start till the stop
# # print(numbers[3:])

# # print(numbers[:-5])

# # print the sequence in revers:

# # print(numbers[::-1])
# # reversed can also be used to reverse the list to produce the same one but in the reversed order
# # print(f"reversed list: {list(reversed(numbers))}")

# # unpacking lists:
# # to access first and second element and the storing the remaining in the others:
# first, second, *others = numbers

# print(first)
# print("*"*10)
# print(second)
# print("*"*10)
# print(others)
# print("*"*10)


# # lets say I want to access the last and the first element leave others as it is in a list
# first, *second, last = numbers
# print(f"First number: {first}")
# print("*"*10)
# print(f"last number: {last}")
# print("*"*10)
# print(f"Remaining: {second}")


# List unpacking:
# to unpack lists we can utilize for loops to get
# back the values that we store in the list, individually.

list_of_items = ["a", "a", "b", "b", "c", 1, 2, 4]

# loop to return all values individually on a seprate line:

# for objs in list_of_items:
#     print(objs)

# Now if we want to get back the values with the index, we could use the enumerate function:
# Enumerate function is used to get back a tuple(a read only data struct)
# lets see how that works:

# for objs in enumerate(list_of_items):
#     print(objs)

# Now lets say I want the index seperate, we can use:
# for objs in enumerate(list_of_items):
#     print(objs[0], objs[1])

# # The above syntax is not easy to understand is lowkey weird
# # the above code is incosistent so we use:

# for index, objs in enumerate(list_of_items):
#     print(index, objs)

# Adding and removing items from the list:

# Adding:
# Adds item to the end of the list
list_of_items.append(True)
# adds item to the specified index
list_of_items.insert(0, "_?")
print(f"The original list: {list_of_items}")
# Removing:
# Removes the last element of the list
# list_of_items.pop()
# another variation of pop: specify the index withting the brackets
# list_of_items.pop(2)
# print(f"Editted list 1: {list_of_items}")

# you can also your remove() function to remove that item,
# it deletes the first occurence of that item
# list_of_items.remove("n")
# if an item doesnt exist, it will throw an error and suggest that the item is not part of the list
# print(f"Editted list 2: {list_of_items}")

# delete function can delete a single item or a range
# # of items which makes it super convinent to use in certain cases
# del list_of_items[0]

# print(list_of_items)

# del list_of_items[2:6]
# print(list_of_items)
# to clear the list of all items use:
# list_of_items.clear()

# Finding items
# print(list_of_items.index("c"))

# if we try finding an item that doesnt exit:
# print(list_of_items.index("z"))
# the above statment gives an error, since z does not exist
# to prevent this error we can use an if stament:
if "z" in list_of_items:
    print(list_of_items.index("z"))
else:
    print("Item doesnt exist")

# lets say we dont want to use any control flow, or get any sort of error, we can use the count():
# it will return the total number of occurences of that item, within that list
print(f"NUmber of times z occurs in our list: {list_of_items.count("z")}")
# if that item doesnt exist in our sequence it will just give zero
# print(list(reversed(list_of_items)))
# print(list_of_items[::-1])

# Sorting items:
print("*"*10)
items = [1, 5, 8, 9, 98, 65, 24]
items.sort()
print(f"Ascending order:{items}")
items.sort(reverse=True)
print(f"Descending order:{items}")

# an uncoventional list of tuples is given,
#  we use key to utilize a function to sort the objects:

listed_items = [
    ("product 0", 10),
    ("product 1", 8),
    ("product 2", 5)
]


# this function is too unclean to use, lengthy and time consuming to code

def sort_listed_items(itms):
    """Function to return 1st item of every tuple
    which is 10 in first tuple, 8 in the second
    and 5 in the third and so on"""
    return itms[1]

# so in such a case we use lambda functions:
# which are simple one line anonymous functions that can be called in other functions
# syntax :- lambda parameter:expression

print(sort_listed_items(listed_items),10*"x")

listed_items.sort(key=sort_listed_items)
print(f"Sorting using a key: {listed_items}")
