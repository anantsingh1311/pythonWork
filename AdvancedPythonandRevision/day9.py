"""Functions"""

# Functions: Re-usable piece of code, set to perform a certain task


def greet():
    """Function printing a greeting"""
    print("Welcome Anant")
    print("Great to have you aboard!")


greet()

print("\n")

# You can plug in parameters while defining functions and utilize arguments to call em:

# parameters are input values defined while defining the function


def greet2(first_name, last_name):
    """Function to greet with parameters"""
    print(f"Hey {first_name} {last_name}")
    print("Welcome Aboard")


# arguments are the output values plugged into the function to help it perform it's task
greet2("Anant", "Singh")


# functions are of two types:
# 1. Perform  a task
# 2. Calc and return a value

print("\n")


def func(name):
    return f"Hey {name}"


print(func("Abhay"))

# lets say we apply print to the above task performing function:

print(greet())

# It prints out "NONE" which basically means that by default a function returns "NONE"

# Key word args: used to make the code readable, they basically are used to
# tell the user or coder which argument is used where:


def func2(num, by):
    return num+by


# here we are explicitly defining that by is 10 to make the code more readable
print(func2(2, by=10))

# we use default args/ optional args when we want to avoid overusing,
# key word args


def function3(num, by=3):
    return num+by


print(function3(5))

# Note: Dont use optional or default params
# before required params because then they will cause a syntactical error

# def func(num=1,by):
#     print("Error code")
# this function will give an error
# so always include optional parameters after declaring all the required ones

# using xargs for multiple args to be applied to the functions
# they produce a tuple which is type of data-stucture same as lists a collection
# of items, but it is immutable


def func4(*args):
    # return args
    result = 1
    for index,nums in enumerate(args):
        result = result*nums
        print(index,result)
    return "Done"


print(func4(2, 3, 4, 5, 5))


print("\n")
print("*"*10)
# XXargs produce a dictionary of key value pairs


def save_user(**args):
    return args


# you basically use kwargs to identify each key and you can give any
# values to them are saved in the form of dictionary ds, which is basically
# a ds which is a seq of key value pairs
user1 = save_user(id=9786, Name="Josh", DOB="11/01/1994")

print(user1["id"])
print(user1.get("gender", None))

user1["gender"] = "female"

print(user1.get("gender"))
