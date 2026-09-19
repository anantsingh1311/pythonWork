"""Data-structures """

items = [("Product #0", 7), ("Product #4", 3), ("Product #3", 9)]

# map function to create a certain part of a list
# items=   | 0          |  1
#          |---------------
#        0 |"Product #0"|  7
#        1 |"Prodcut #4"|  3
#        2 |"Product #3"|  9
# usually we would get only the prices of each product in this way:

# prices = []

# for i in items:
#     prices.append(i[1])

# to write the above expression in a more elegant way we use the map function:
x = map(lambda item: item[1], items)

# so to print a map object you need to iterate over it using a for loop
for i in x:
    print(i)

# but lets say we want a list instead so
#  we use list function to convert any sequence of items into a lis:

a = list(map(lambda item: item[1], items))

print(a)

# for objs in enumerate(items):
#     print(objs)

# for index, objs in enumerate(items):
#     print(index, objs)
