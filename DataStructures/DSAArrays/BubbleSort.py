my_array = [7,12,9,11,3]

# We need to sort the array by swapping each value with next one
# until all the values are sorted in 
# ascending order.

# we look in the array above:
# if 7<12: swap -> False
# if 12>9: swap ->true,
# until we have a sorted array

# for an outer loop n-1 
# we run throw the whole array
# in the inner loop n times

n = len(my_array)

for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j]>my_array[j+1]:
            my_array[j],my_array[j+1] = my_array[j+1],my_array[j]

print(my_array) 











# import time

# start = time.time()

# n = len(my_array)

# for i in range(n-1):
#     for j in range(n-i-1):
#         if my_array[j+1]<my_array[j]:
#             my_array[j],my_array[j+1]=my_array[j+1],my_array[j]

# print("Sorrted:",my_array)

# end = time.time() - start

# print("Time taken: ",end)