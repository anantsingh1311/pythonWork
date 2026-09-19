"""Control flow part-2"""

# Loops are used to repeat tasks to avoid redudant code
# for loops are used in the following way:

# for x in range(4):
#     print("Exam attempted")

# Now lets say I want to print the number as well with the text:
# for x in range(4):
#     print("Exam attempted", x)

# # Now we know that indexing starts at 0
# # and we know that we want to make it look like its starting from one
# # range function can also be used in this sense: range(start,stop,step)

# for x in range(1, 10, 2):
#     print("Exam attempted", x, x*".")
# # above for loop uses a range between 1,10 (stop val is not included)

# Using the for else loop:

# succesful = True

# for x in range(3):
#     print("Attempted")
#     if succesful:
#         print("Exam passed,Success achieved")
#         break
# else:
#     print("Attempt failed")

# nested for loop: a doubly nested for loop means
# for every outter loop iteration the inner loop executes fully

# print("*"*10, "\n")

# for x in range(10):
#     for y in range(4):
#         print(f"(x:{x},y:{y})")

# iterables: are complex types over which you can iterate and use it in a for loop.
# strings, lists and range function are all examples of the type iterable.

# message1 = "Anant Singh"

# for x in message1:
#     print(x)

# shopping_cart = ["ice cubes", "coke", "Chips", "Burger", "Fries"]

# for x in shopping_cart:
#     print(x)

# Revision:
# for x in range(4):
#     print(f"Exam attempted: {x}*times")


# for else loop:

# print(f"{"x"*20}\n")

# success = True


# for x in range(3):
#     print("Attempting Exam \nExam attempted\nEvaluating your responses....\n")
#     if success:
#         print("Exam cleared!")
#         break
# else:
#     print("Exam Failed, try again next year")

# for x in range(10, 0, -4):
#     print(x)

Day = ["Monday", "Tuesday", "Wedneday",
       "Thursday", "Friday", "Saturday", "Sunday"]

Sched = ["Office", "Gym", "Eat", "Sleep"]


for days in Day:
    for schedule in Sched:
        if days == "Saturday" or days == "Sunday":
            print(f"Day:{days},To-DO: Drink, party and Sleep")
        else:
            print(f"Day:{days},To-DO:{schedule}")
            # print(f"Day:{days},To-DO:{schedule}")
