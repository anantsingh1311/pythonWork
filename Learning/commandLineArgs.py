import sys

# print(sys.argv)

if len(sys.argv) == 1:
    print("USAGE: PYTHON 3 APP PASSWORD")
else:
    password = sys.argv[1]
    print(f"Password: {password}")