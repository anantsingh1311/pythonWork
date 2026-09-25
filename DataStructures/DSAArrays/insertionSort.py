# To implement the Insertion Sort algorithm in a programming language, we need:

# An array with values to sort.
# An outer loop that picks a value to be sorted. For an array with 
# n
#  values, this outer loop skips the first value, and must run 
# n
# −
# 1
#  times.
# An inner loop that goes through the sorted part of the array, to find where to insert the value. If the value to be sorted is at index 
# i
# , the sorted part of the array starts at index 
# 0
#  and ends at index 
# i
# −
# 1
# .
# The resulting code looks like this:


my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(1,n):
    insert_at_index = i
    current_value = my_array[i]
    for j in range(i-1,-1,-1):
        if my_array[j]>current_value:
            my_array[j+1] = my_array[j]
            insert_at_index = j
        else:
            break

    my_array[insert_at_index] = current_value


print(my_array)


