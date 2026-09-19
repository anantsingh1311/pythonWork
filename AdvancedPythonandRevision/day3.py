# # Important string methods to remember, which can be useful during coding

# message = " python  programming "

# # String method to determine the length of a string:
# print(len(message))

# # method to convert all chars in the string to upper or lower case:
# print(message.lower())
# print(message.upper())

# # method to delete all white spaces in the string, left white spaces and right white spaces
# print(message.strip(), "*")
# print(message.lstrip(), "*")
# print(message.rstrip(), "*")

# # method to convert the string into title case:
# print(message.title())

# # method to find a particular
# # char or seq of chars in the form of indexes(method returns -1 if false):
# print(message.find("prog"))
# # -1 since the find func is case sensitve and prog exists but not Prog
# print(message.find("Prog"))

# # method to replace a specific character in the string:
# message2 = message.replace("p", "J")
# print(message2)

# # expression to return a boolean value, to check wether a char or seqeunce of chars exists or
# # does NOT exist in the given string
# print("prog" in message)
# print("prog" not in message)


# String1

str1 = " welcome to the world of zOdddddddd!!!!!** "

print(str1)
# print(len(str1))

# print(str1.rstrip())

print(str1[3:8])

print(str1.index("z"))

print(str1.find("W"))

print(str1.find("z"))

# Basically you can aslo use the index number while using the replace function
str2 = str1.replace("z", "G", 25)
print(str2,"**********8")
str3 = str1.replace("w","b")

print(str3)

print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.capitalize())
