# """For Revision and Practising"""

# # message = input(">:")


# # # if message.lower() == "exit":
# # #     print("exit")
# # # else:
# # #     print("Welcome")
# # # while message.lower() != "exit":
# # #     print(message)
# # #     # remember to update your while loop to prevent entering in an infinite loop
# # #     message = input(">:")

# # while True:
# #     print(message)
# #     message = input(">:")
# #     if message.lower() == "exit":
# #         break
# # print("Thank you for using my terminal")


# # answer = ""

# # while answer.lower() != "exit":
# #     answer = input(">>")
# #     print(answer)


# # success = False


# # for i in range(5):
# #     print("Trying")
# #     if success:
# #         print("Test passed")
# #         break
# # else:
# #     print("Failed all 5 attempts, Try next year!!")

# def make_list(*args):
#     """function to produce a user defined list"""
#     return list(args)


# products = make_list(("product0", 5), ("product2", 7.5),
#                      ("product5", 3), ("product8", 9))

# print(f"Products in stock:{products} \n")

# # lets say I want to sort this list out:


# def sort_prices(items):
#     """ref function to sort prices"""
#     return items[1]


# # products.sort(key=sort_prices, reverse=False)

# products.sort(key=lambda items: items[1], reverse=True)

# print(products)


# for i in range(5-2, 0, -2):
#     print(i)

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())

#     list_output = [[i, j, k]
#                    for i in range(x+1)
#                    for j in range(y+1)
#                    for k in range(z+1)
#                    if i+j+k != n]

#     print(list_output)

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())

#     set_arr = list(set(arr))

#     set_arr.sort(reverse=True)
#     print(set_arr[1])


# if __name__ == '__main__':

#     records = []

#     for _ in range(int(input())):
#         name = input()
#         score = float(input())

#         records.append([name, score])

#     # records.sort(key=lambda x: x[1])

#     unique_numbers = set(x[1] for x in records)
#     sorted_unique_numbers = sorted(unique_numbers)

#     second_lowest = sorted_unique_numbers[1]

#     result = [x for x, y in records if y == second_lowest]

#     result.sort()

#     for names in result:
#         print(names)

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()

#     result = 0

#     for name, scores in student_marks.items():
#         if name == query_name:
#             total = 0
#             for i in scores:
#                 total += i
#             result = total / len(scores)

#     print(round(result, 2))

# for x, y in student_marks.items:
#     print(y)

# query_name = input()2

# for key, values in student_marks:
#     print(key, values)
# print(student_marks)


# if __name__ == '__main__':
#     N = int(input())
#     list_output = []
#     for i in range(N):
#         command = input().lower().split()
#         if command[0] == "insert":
#             list_output.insert((command[1]), (command[2]))
#         elif command[0] == "print":
#             print(list_output)
#         elif command[0] == "remove":
#             list_output.remove(command[1])
#         elif command[0] == "append":
#             list_output.append(command[1])
#         elif command[0] == "sort":
#             list_output.sort()
#         elif command[0] == "pop":
#             list_output.pop()
#         elif command[0] == "reverse":
#             list_output.reverse()

# if __name__ == 'main':
#     N = int(input())

#     command = tuple(map(int, input().split()))

#     print(command.__hash__())
# def swap_case(s):
#     letters = []
#     str = ""

#     for i in s:
#         # print(i)
#         if i == i.lower():
#             i = i.upper()
#         elif i == i.upper():
#             i = i.lower()

#         letters.append(i)

#     newString = str.join(letters)
#     return newString


# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)


# def split_and_join(line):
#     # write your code here
#     a = line.spilt("")
#     return a


# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

# def count_substring(string, sub_string):
#     count = 0
#     for i in range(0, len(string)):
#         if string[i] == sub_string:
#             count += 1

#     return (count)
#     # return


# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()

#     count = count_substring(string, sub_string)
#     print(count)
