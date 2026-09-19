"""Debugging"""


# use f5 to get into debug mode
# apply a break point where neccessary to step into your
#  function/program and see its iteration step by step
# F10 (Step Over)
# Executes the current line, including any function calls, b
# ut doesn’t step into them. Instead, it runs the entire call behind
# the scenes and lands on the next line in the current function


# F11 (Step Into)
# Executes the current line and, if there’s a
# function call, dives into that function, letting you debug its internal steps

# Breakpoints:
# Why

# To pause program execution at a specific point.

# Lets you inspect variables, call stack, memory, watch expressions, etc
# Helps isolate bugs by narrowing down where unexpected behavior occurs.

# Where
# Typically on the line where you want execution to pause—e.g.
# , before a critical function call or logical branch.

# In IDEs like Visual Studio, simply click the left margin or press F9 to toggle a breakpoint

def func(*args):
    """Function defining xargs to calc multiplication of numbers"""
    result = 1
    for nums in args:
        result = nums
    return result


print("Start")
print(func(1, 2, 3))
