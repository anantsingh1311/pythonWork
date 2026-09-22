# Go through the array to find the lowest value.
# Move the lowest value to the front of
#  the unsorted part of the array.
# Go through the array again as many 
# times as there are values in the array.


# for i in range(1,8):
#     print(i)



my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)

for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
        if my_array[j]<my_array[min_index]:
            min_index = j

    # new_min_value =  my_array.pop(min_index)
    # my_array.insert(i,new_min_value)
    my_array[i],my_array[min_index] = my_array[min_index], my_array[i]

print(my_array)





# for i in range(n-1):
#     min_index = i
#     for j in range(i+1,n):
#         if my_array[j] < my_array[min_index]:
#             min_index = j

#     # # tHIS IS A MEMORY INTENSIVE TASK, SO WE SWAP INSTEAD:
#     # min_value = my_array.pop(min_index)
#     # my_array.insert(i,min_value)

#     # WE USE THIS TECHNIQUE OF SWAPPING
#     my_array[i],my_array[min_index] = my_array[min_index],my_array[i]

# print(my_array)
    


