"""Control flow"""
age = 19

# if age > 18:
#     print("Eligible")
# elif age > 13 and age < 18:
#     print("start preparing")
# else:
#     print("In-elligible")

# print("done evaluating")

# use of ternary operator:

# if age > 18:
#     message = ("Elligible")
# else:
#     message = ("Inelligible")

# print(message)

# Now we can write the above code in one line as follows, utilizing the ternary operator:

message = "Elligible" if age > 18 else "inelligible"

print(message)

a = 10
b = 12

print(f"a:{a}, b:{b}")

print("\n")


print("*"*20)
# logical operators:
# Python offers 3 types of logical operators:
# a. and -> evaluates to true if all conditions are met
# b. or -> evaluates to true if one of the conditions are met
# c. not -> a boolean expression is inversed

high_income = True
good_credit = True
student = False

# if high_income or good_credit:
#     print("Loan passed")

# placing not before a boolean expression inverses it's value
# if not student:
#     print("Too young to approve")
#     # print("Elligible")

# in python logical ops are shor circuited,
#  meaning if the first condition below is met
# then it wont even care about checking good credit and not student
if high_income and good_credit and not student:
    print("Loan Approved")

# but to solve this issue, we use brackets
if (high_income or good_credit) and not student:
    print("Loan Approved")

# chaining comparison ops:
# lets say we want an expression to evaluate age in between 18 and 65 so one might type it like:

if age >= 18 and age <= 65:
    print("Adult")

# to write the above if statment clean,
#  we can use the following expression,
# as how we would use in math: age in between 18 and 65: 18<=age<=65
if 18 <= age <= 65:
    print("adult")
