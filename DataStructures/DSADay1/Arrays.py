

# finding min value in a given set of array
arr = [2,9,45,650,-1]

current_min = arr[0]

for i in range(len(arr)):
    if arr[i]< current_min:
        current_min = arr[i]

print(f"Min number in the given list of Array {arr} is:{current_min}")

