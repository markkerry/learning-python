# get user input

name = input("What is your name: ")
age = input("How old are you: ")
print("Hello " + name + " you are " + age)

# incorrectly as for numbers and add them together
# What will actually happen is python will concatinate the two numbers as they are strings
num1 = input("Enter a number: ")
num2 = input("And another: ")
result = num1 + num2
print("strings of " + num1 + " add " + num2 + " concatinated together is " + result)

# to make these ints, we can convert the strings to int
result = int(num1) + int(num2)
print(f"But the strings converted into ints and added equals {result}")