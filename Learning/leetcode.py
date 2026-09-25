
# # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
# #     """Adding reversed of l1 and l2"""

# l1 = [1,2,3]
# l2 = [4,5,9]
    
# # print())

# # print(list())

# class ListNode:
#     def _init_(self,val=0,next=None):
#         self.val = val
#         self.next= next

# def listNode_to_List(head: ListNode) -> list:
#     result = []
#     current = head

#     while current:
#         result.append(current.val)
#         current = current.next

#     return result

# head = ListNode(1)

# head.next = ListNode(2)

# head.next.next = ListNode(3)

# print(head)

# l1Rev = list(reversed(l1))
# l2Rev = list(reversed(l2))

# number1 = int("".join(map(str,l1Rev)))
# number2 = int("".join(map(str,l2Rev)))

# result = number1 + number2

# print(result)

# resultInString = str(result)

# list1 = list(map(int,resultInString))

# print(list1)

# # a = 0

# # for i in l1Rev:
# #     print(i+(i+1))
    



# first we need to reverse a list:

# l1 = [3,4,2]
# l2 = [7,0,8]

# l1Rev= int("".join(map(str,list(reversed(l1)))))
# l2Rev = int("".join(map(str,list(reversed(l2)))))


# print(l1Rev)
# print (l2Rev)

# result = l1Rev+l2Rev

# print(result)

# result_list = map(int,list(reversed(str(result))))

# print(list(result_list))

# result_list_reversed = int(map())

# s = "pwwkew"

# setS = set()
# left = 0
# longest = 0

# for right in range(len(s)):

#     if s[right] in setS:
#         setS.remove(s[left])
#         print("removing",s[left])
#         left+=1
#     print("adding",s[right])
#     setS.add(s[right])
#     # longest = max(longest,right-left+1)

# print(len(setS))










# array = [[1,1],[2,2],[3,3],[4,4],[5,5]]

# array.append(10)

# print(array)

# array[2].append(3)

# print(array)

# from statistics import median

# nums1 = [1,2] 
# nums2 = [3,4]

# result_arr = nums1 + nums2

# result_arr.sort()

# # print(result_arr)

# print(median(result_arr))

# x = 123

# y = list(str(x))

# y.reverse()

# print(y)

# a = int("".join(y))

# if -(2**31) < a < (2**31 - 1):
#     print(a)
# else:
#     print(0)

# s = "42"
# a = " -042"

import string
s = "1337c0d3"
a = ""
for i in range(len(s)):
    if s[i] in string.ascii_letters:
        break
    a += s[i]

# print(a)
       

new_integer = int(a)

print(new_integer)






















































