# if, elif, else

# and, or, not()

is_python = True
is_windows = False

if is_python:
    print("Python is True")
else:
    print("Python is not True")

if is_python and is_windows:
    print("Both are True")
elif is_python and not(is_windows):
    print("Python is True but Windows is not")
elif not(is_python) and is_windows:
    print("Python is not True but Windows is")
else:
    print("Neither of these are True")

# Comparison operators
# >, <, >=, <=, ==, !=

# function to return the largest function
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(str(num1) + " is the largest")
    elif num2 >= num1 and num2 >= num3:
        print(str(num2) + " is the largest")
    else:
        print(str(num3) + " is the largest")

# specify different ints. doesn't work if you select the same int

print(max_num(5, 6, 15))