# strings are immutable so elements cannot be changed

# Triple quotes for multi-line
multi_line_string1 = """Start here
and finish here"""
print(multi_line_string1)

# use escape to create multi-line but print on same line
multi_line_string2 = """Start here \
and finish here"""
print(multi_line_string2)

# get first character
char = multi_line_string1[0]
print(char)

# get last character
char_end = multi_line_string1[-1]
print(char_end)

# slicing/ starts at index 2 and up to 9 which is not inclided
substring = multi_line_string1[2:9]
print(substring)

# reverse the string
reverse = multi_line_string2[::-1]
print(reverse)

# concatinate stings
print(multi_line_string1 + " " + multi_line_string2)

for i in multi_line_string2:
    print(i)

if 'e' in multi_line_string2:
    print('yes')
else:
    print('no')

# trim white space
white_space = "    Strip out the white space      "
print(white_space.strip())

# upper character and strip
print(white_space.upper().strip())

# 
print(white_space.strip().startswith("S"))

# count the whitespaces
print(white_space.count(" "))

# split each word into an element
# default agument is a space so this does not include the white spaces
print(white_space.split())

# strip out the commas, create a new string without them
my_string = "This,did,include,commas,not,anymore"
my_list = my_string.split(",")
new_string = " ".join(my_list)
print(new_string)

# Different ways to format strings
# old %, or .format(), or new f-Strings
var = "Mark"
my_name = "The variable is %s" % var
print(my_name)

# don't use %s if int (decimal) use %d. Use %f for a float
var_int = 3
var_value = "The variable is %d" % var_int
print(var_value)

# .format()
print("The variable is {} and {}".format(var,var_int))

# f-Strings
print(f"The variable is {var} and {var_int}")