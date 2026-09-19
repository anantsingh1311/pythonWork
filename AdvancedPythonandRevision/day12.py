"""Fizz-buzz excercise:"""


def fizz_buzz(a):
    """fizz-buzz"""
    if a % 3 == 0 and a % 5 == 0:
        return "fizz-buzz"
    if a % 3 == 0:
        return "fizz"
    if a % 5 == 0:
        return "buzz"
    return a


print("Startin the fizz buzz function: \n")
print("-"*15)
print("||", fizz_buzz(15), "||")
print("-"*15)
