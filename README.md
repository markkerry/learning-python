# Learning-Python

Table of contents:
1. [Variables and Data Types](#Variables and Data Types)
2. [Basic Operators](#Basic Operators)
3. [User Input]()
4. [List arrays and Tupples]()
5. [Functions]()
7. [If Else Elif]()
8. [Dictionaries]()
9. [Loops]()
10. [Modules]()

<br>

## Variables and Data Types

Four main data types in Python

```python
# Whole numbers
int 1, 4, 5

# Strings
str 'Mark', "Kerry", '1'

# Boolen
bool True, False # must start with capitals

# Float
float 0.1, 1.3

# Use double quotations ("") if you want to include single quotations ('') in your string e.g.

str "This is a 'string'"

# Variables in Python cannot start with a number but can end in one. Can include _ but not *.

## Create a variable
os_version = "CentOS 8"

# Print the same string using the .tolower method
print(os_version.lower())

# This should return True. Set to upper then test is upper
print(os_version.upper().isupper())

# Len function
print(len(os_version))

# Get specific characters
print(os_version[0] + " is index 0 in " + os_version)

# Or if you want to find the index of a character. Use the index function
print("\"t\" in " + os_version + " is at index " + os_version.index("t").__str__())

# Another way to convert an int to a string
print(str(os_version[7]) + " has been converted to a str")

# Now we can replace 8 with 7
print("Changed version using replace method to " + os_version.replace("8", "7"))
```

## Basic Operators

TO DO

## User Input

```python
# incorrectly as for numbers and add them together
# What will actually happen is python will concatinate the two numbers as they are strings
num1 = input("Enter a number: ")
num2 = input("And another: ")
result = num1 + num2
print("strings of " + num1 + " add " + num2 + " concatinated together is " + result)

# to make these ints, we can convert the strings to int
result = int(num1) + int(num2)
print(f"But the strings converted into ints and added equals {result}")
```

## List arrays and Tupples

```python
# Create the array with 3 elements
operating_system = ["inux", "Windows", "Unix"]

# First element at index postition 0
print(operating_system[0])

# Add a new element
operating_system.append("MacOS")

# Elements 1 and up to 3 (not inc 3). Windows and Unix
print(operating_system[1:3])

# Add another into index 1
operating_system.insert(1, "FreeBSD")

# Remove and element
operating_system.remove("Unix")

# Pop will removed the last element in the list
operating_system.pop()

# reset the list and sort into order
operating_system = ["Linux", "Windows", "Unix", "MacOS", "FreeBSD"]
operating_system.sort()

# create new list with ints
lotto_nums = [24, 53, 1, 15, 33, 35]

# sort the ints ascending order
lotto_nums.sort()

# Now lets copy the list and reverse the numbers in descending order
lotto_nums2 = lotto_nums.copy()
lotto_nums2.reverse()
print(lotto_nums2)

# Tupples are immutable. Cannot be changed or modified
# Lists can. Lists like Variables, Tupples like Constants

coordinates = (4, 5)
print(coordinates[0])

# Cordinates are a good example as they are not likely to be modified.
# Majority of the time will use lists
```

## Functions

```python
# keyword to create a function in python is def

# name it lowercase with underscore if more than one word
# code in function must be indented. (tabs not spaces)
def hello_world():
    print("Hello World")

# call the function
hello_world()

# parameters
def hello_user(name, age):
    print("Hello " + name + " your are " + str(age))

# Another way to include a variable in a string. Good if it is an int
# print(f"You are {age}")
hello_user("Mark", 70)

# Return statement. Return output value from the function
def cube(num):
    return num*num*num

result = cube(3)
print(result)

# Exponent Function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 4))
```

## If Else Elif

```python
# if, elif, else

# and, or, not()

is_python = True
is_windows = False

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
num1 = float(input("Enter a number: "))
op = input("Enter operator: ")
num2 = float(input("Enter another number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print(str(op) + " is an invalid operator. Does not match +, -, * or /")
```

## Dictionaries

```python
# Key/Value pair
# All keys have to be unique

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Jun"])
print(monthConversions.get("Jul"))

# Can set a default value if key not available
print(monthConversions.get("fdfds", "Not a valid key"))
```

## Loops

### While Loop

```python
i = 1
while i < 10:
    print("i is equal to " + str(i))
    i += 1

print("Finished with loop as i is equal to 10")
```

### For Loop

```python
letters = "Python"
print("Demonstrating for loop to spell out Python")
for letter in letters:
    print(letter)

operating_systems = ["Linux", "Windows", "Unix"]
print("Each OS in list")
for operating_system in operating_systems:
    print(operating_system)

# 3 elements in the the operating_systems list
print("Another way to print each OS in list")
for index in range(len(operating_systems)):
    print(operating_systems[index])
```

## Modules

```python
#Import the math module
import math
math.pi

# Import just the pi variable from the math module
from math import pi
pi

# Rename the module to m
import math as m
m.pi
```

## Comments

```python
# hash for a regular, single line comment

'''
Or inside a triple quotation mark
for multi-line
'''
```

## Try Except

```python
# except meaning exception
# can catch a specific error
# catch a value error if not an int
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input")

# can't devide 10 by 0
try:
    10/0
except ZeroDivisionError as err:
    print(err)
```

## Reading and Writing Files

### Reading

```python
# Read the file in same dir
# First open the file
file = open("example-file.txt", "r")

# Ensure it is readable
readable = file.readable()
if readable:
    print(file.read())
else:
    print("The file is not readable")

# for loop to print each line in the file
for line in file.readlines():
    print(line)

# Read the whole file
print(file.read())

# Read first line
print(file.readline())
# Again will read the secnd line
print(file.readline())

# Read all lines as a list (array)
print(file.readlines())

# Close the file
file.close()
```

### Writing

```python
# First open the file with append
file = open("example-file.txt", "a")

# Add escape charater to add a new line first
file.write("\n# EOF")

# Close the file
file.close()

# Create a new file which doesn't exist
file_new = open("index.html", "w")
file_new.write("<p>This HTML file was created with Python</p>")
file_new.close()
```

## pip

```terminal
# install a module
pip install python-docx

# use the module
import docx

# remove the module
pip uninstall python-docx
```

## modules

```python

```
