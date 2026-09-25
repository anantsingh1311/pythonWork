
# my_hash_set = [[] for i in range(10)]

my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]


def hash_function(value):
    sum_ofChars= 0

    for char in value:
        sum_ofChars += ord(char)

    final_unicode_value = sum_ofChars % 10
    # Storing the value in the hashtable bucket at the unicode value that we got from the value we added
    # my_hash_set[final_unicode_value].append(value)
    # print(sum_ofChars)
    return final_unicode_value


print("Bob has hash code: ",hash_function('Bob'))

print("Rachel has hash code: ",hash_function('Rachel'))

print("Anant has hash code: ",hash_function('Anant'))

print("Lisa has hash code: ",hash_function('Lisa'))
print("Lisa has hash code: ",hash_function('Stuart'))

# print(my_hash_set)


# print(my_hash_set.index("Bob"))
def add(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    if value not in bucket:
        bucket.append(value)

# Now if we want to check our hashset for a name, we can dierectly find it:
print("Checking for the provided name")
def contains(name):
    index = hash_function(name)
    check_name = f"{name} is there at hash code: {hash_function(name)}" if my_hash_set[index] == name else f"{name} is not present in the list"
    print(check_name)
    return index


add('Stuart')

print(my_hash_set)
print('Contains Stuart:',contains('Stuart'))