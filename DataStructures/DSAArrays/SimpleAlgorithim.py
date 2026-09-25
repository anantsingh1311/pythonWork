# Using brute force to create fibonacci algorithim:

# import time

# start_time = time.time()


# prev = 0
# next = 1

# result = 0

# print(prev)
# print(next)

# for i in range(18):
#     result = prev+next

#     print(result)

#     prev = next
#     next = result

# end_Time = time.time()

# time_taken = end_Time - start_time

# print(f"time taken by the brute force algorithim is: {time_taken}")

# Brute force 0.00041 s 

# Implementation using recursion:
# When a function calls itself 

# import time

# start_time = time.time()

# print(0)
# print(1)

# count = 17

# def fibonacci(prev,next):

#     global count

#     if count>=0:
#         result = prev+next
#         print(result)
#         prev = next
#         next = result
#         count -= 1
#         fibonacci(prev,next)
#     else:
#         return

# fibonacci(0,1)

# result_time = time.time() - start_time

# print("Time taken via recursion: ",result_time)

# Time taken via recursion:  0.0006725788116455078

# When we use a properly designed algorithim:

# Mathematical formula for fibonacci number is :
# f(n) = f(n-1) + f(n-2)

# import time

# start = time.time()

# def F(n):
#     if n <= 1:
#         return n
#     else:
#         return F(n - 1) + F(n - 2)

# print(F(19))

# result_time = time.time() - start

# print(result_time)

# time taken by a formulated algorithim 0.0004811286926269531