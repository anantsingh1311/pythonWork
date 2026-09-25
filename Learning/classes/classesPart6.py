# data classes
from collections import namedtuple

# namedTuple are immutable
Point = namedtuple("Point",["x","y"])

p1 = Point(1,2)
p2 = Point(1,2)

print(p1==p2)