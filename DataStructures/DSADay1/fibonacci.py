# 1 Using fibonacci sequence
# using for loop
# prev = 0
# next = 1
# temp = 0

# print(prev)
# print(next)



# for i in range(18):
#     result = prev + next
#     # storing next value in temp variable
#     print(result)
#     prev = next
#     next = result



# using functions:


# def fibonacci(prev = 0,next=1,count=0):

#     if count <= 19:
#         newFib = prev+next
#         print(prev)
#         prev = next
#         next = newFib
#         count+=1
#         fibonacci(prev,next,count)
#     else:
#         return

# fibonacci()

# Using numerical formula F(n) = F(n-1) + F(n-2)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(19)) 