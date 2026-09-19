"""While loops and Infinite loops"""

# answer = ""

# while answer != "quit":
#     answer = input(">>>")
#     print(answer)

# beginner coding mistake: only checks for two types, what if the user entered QUIT
# while answer != "quit" and answer != "Quit":
#     answer = input(">>>")
#     print(answer)

# print("Thanks for using the \"terminal\"")

# To avoid above we just convert any message to
# lower, upper or title, or however we want,
# in that case user input doesnt matter and the
# quit will cause the user to exit out of the loop

# while answer.lower() != "quit":
#     answer = input(">>>")
#     print(answer)

# infinite while loops: they evaluate infinitely unless you create a function to jump out of them.
# very memory intensive and only create issues if not utilized properly.
# can cause the program to crash since the acquire too much memory.

# while True:
#     message = input(">>>")
#     print(message)
#     if message.lower() != "quit":
#         break

# Excercise, print all even numbers in range 1,10 without using the third argument

# count = 0
# for x in range(1, 10):
#     if (x % 2 == 0):
#         count += 1
#         print(x)

# print(f"Even numbers:{count}")

# ans = ""

# while ans != "quit":
#     ans = input(">>>")
#     print(ans)

# print("Hey What is your name: ")
# ans = input("Name: ")
# print(ans)


while True:
    message = input(":::")
    print(message)
    if message.lower() == "quit":
        print("quitting the custom built terminal")
        break
