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

# write to file
open("example_file.txt", "w")

# append to file
open("example_file.txt", "a")

# read and write
open("example_file.txt", "r+")