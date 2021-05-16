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