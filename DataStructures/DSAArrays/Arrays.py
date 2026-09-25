# Go through the values in the array one by one.
# Check if the current value is the lowest so far, and if it is, store it.
# After looking at all the values, the stored value will be the lowest of all values in the array.

my_array = [7,12,9,4,11]

print(my_array[0])

lowest_value = my_array[0]

for i in my_array:
    if i < lowest_value:
        lowest_value = i

print(lowest_value)