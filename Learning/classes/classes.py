# Class: blue print for creating new objects
# Object: Instance of  a class
# Constructors:

class Point:

    # class level attributes are shared consistently among all the insatnces of a class
    default_color = "red"

    def __init__(self,x,y):
        # self is a refernce to the current object
        # by default all methods under a class need a self attribute which points the current object
        self.x = x
        self.y = y

    # This below @classMethod is called a decorator, it is used to set up default values of an object in case an object being created is a complex object
#    @classmethod makes zero() a method that belongs to the class, rather than a specific object. It receives cls, which refers to the class itself.
# This method acts as an alternative constructor: a convenient way to create an object in a predefined state.
    @classmethod
    def zero(cls):
        return cls(0,0)

    # Magic methods: are represented by __something__ Python automatically calls these methods when certain operations happen.
    # They are also called dunder methods, meaning double underscore methods.
    def __str__(self):
        return f"{self.x}\n{self.y}"

    # draw here is an instance method, that you basically invoke after creating instance of a class named Point, as seen below
    def draw(self):
        print(f"Point ({self.x},{self.y})")

    # to use dunder for comparing two objects
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    # to see if one object is greater than the other:
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    def __add__(self, other1):
        return Point(self.x+other1.x,self.y+other1.y)

point = Point(2,4)
other = Point(2,4)

# instead of writing this statement below everytime:
# print(f"{point.x},{point.y}")
# Since we have __str__ dunder/magic method we can just print the point object:
# print(point)

# print(point+other)

print(point==other);

# print(point != other)
# print(point<other)

# Point.default_color = "yellow"

# point = Point(1,2)

# print(Point.default_color)
# print(point.default_color)
# point.z = 10

# point.draw()

# # print((point.x))

# # print(isinstance(point, int))

# another = Point(3,4)