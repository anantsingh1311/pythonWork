"""Generator Exrpessions and Unpacking Operators"""

from sys import getsizeof

# Used when youre dealing with large data set to
# prevent over-use of memory:

# defining a generator:
values = (x*2 for x in range(100))

print((getsizeof(values)))

values = [x*2 for x in range(100)]
# More memory intensive
print(getsizeof(values))

# """Unpacking Operators:"""

# Used to unpack individual values without the need to use a for loop

a = [1, 20, 30]

print("Unpacking a:", *a)

# you can also use the unpacking operator like:
# using it to unpack a list of any type:
a = [*range(10)]

print(a)

# Combining different lists or unpacking different iterables into one list
b = [*range(10), *"Hello", *"abc"]
print(b)

myDic = {"key1": "abcd", "Key2": [6, 7, 8]}

mydic1 = {"key3": 5}

combine = {**myDic, **mydic1}

# print(combine)

for keys, values in combine.items():
    print(keys, values)
    # print((values))

# Excercise:

Question = "This is a common interview question"

dictonaryResult = {}

for char in Question:
    if char in dictonaryResult:
        dictonaryResult[char] += 1
    else:
        dictonaryResult[char] = 1
# print(dictonaryResult)

# To print highest repeated character:
# .items() converts dictionary to tuple
mostrepeatedValue = (sorted(dictonaryResult.items(),
                            key=lambda x: x[1], reverse=True))

print(mostrepeatedValue[0])
