# comment

# Print function
print("Hello World")

# Variables. Best practive in Python is to user lower case and seperate words with underscores
users_name = "Mark"
users_age = "89"

# Varaibles can used in the print function like this
print(f"Hello {users_name}, you are {users_age}\n")

# Or like this with string concatination
print("Hello " + users_name + ", you are " + users_age + "\n")

# Use a backslash escape character to print a literal character
print("Contains a \" in the string")

## Print a variable
os_version = "CentOS 8"
print(os_version)

# Print the same string using the .tolower method
print(os_version.lower())

# This should return True. Set to lower then test is upper
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

six = 2 + 4
print(six)

# order of operation through parathsis
print(3 * 4 + 5) # equals 17
print(3 * (4 + 5)) # equals 27

# mod gives you the remainder
print(10 % 3) # equals 1

# min and max functions. print smallest of two numbers, then largest of two numbers
print(min(4, 6))
print(max(4, 6))
print(round(9.8))