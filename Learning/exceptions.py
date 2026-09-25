


# try:
#    with open("text.txt") as file, open("another.txt") as target:
#        print("file opened")
#    age = int(input("age:"))
#    xfactor = 10/age
# #    a.close()


# except ValueError,ZeroDivisionError:
#     print("Age not accepted")
# else:
#     print("Age defined")


# defining a calculation function

def calculate_xFacypr(age):
    if age <= 0:
        raise ValueError("age cannot be less than 0 or 0")
    return 10/age

try:
    calculate_xFacypr(-1)
except ValueError as error:
    print(error)