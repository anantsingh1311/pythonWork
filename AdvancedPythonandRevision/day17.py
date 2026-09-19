"""Queue"""

# You can apply qeue in the following manner, import
# deque from collections
from collections import deque as a

# pass in your variable within the deque class as a list
qeue = a([])

qeue.append(0)
qeue.append(1)
qeue.append(2)
qeue.append(4)

# then you can utilize the pop left function from the deque class to
# remove the first item of the list
qeue.popleft()

print(qeue)

# You could use lists  but they are more memory intensive in this case, so we use
# deque collection object from the deque class
