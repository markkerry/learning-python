# Arrays

# Create the array with 3 elements
operating_system = ["inux", "Windows", "Unix"]
print(operating_system)

# First element at index postition 0
print(operating_system[0])

# Last element at index position 2
print(operating_system[2])

# Add a new element
operating_system.append("MacOS")
print(operating_system)

# Elements 1 and up to 3 (not inc 3). Windows and Unix
print(operating_system[1:3])

# Add another into index 1
operating_system.insert(1, "FreeBSD")
print(operating_system)

# Remove and element
operating_system.remove("Unix")
print(operating_system)

# Pop will removed the last element in the list
operating_system.pop()
print(operating_system)

# Check if FreeBSD is still in the list
print(operating_system.index("FreeBSD"))

# reset the list and sort into order
operating_system = ["Linux", "Windows", "Unix", "MacOS", "FreeBSD"]
operating_system.sort()
print(operating_system)

# create new list with ints
lotto_nums = [24, 53, 1, 15, 33, 35]
print(lotto_nums)

# sort the ints ascending order
lotto_nums.sort()
print(lotto_nums)

# Now lets copy the list and reverse the numbers in descending order
lotto_nums2 = lotto_nums.copy()
lotto_nums2.reverse()
print(lotto_nums2)

# like a data structure container. Similar to a list

# Tuples are immutable. Cannot be changed or modified
# Lists can. Lists like Variables, Tuples like Constants

coordinates = (4, 5)
print(coordinates[0])

# Cordinates are a good example as they are not likely to be modified.
# Majority of the time will use lists