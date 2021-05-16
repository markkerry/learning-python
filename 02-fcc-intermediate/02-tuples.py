import sys # for the compare size later on
import timeit

# collection data with immutable data which can't be changed.
# allows duplicate elements

tup = ("Azure", 4096)
print(tup)
print(type(tup))

# can create a tupple from a list
a = tuple(["Azure", "AWS", 1024, True])
print(a)

# get type of element 2 (int)
b = a[2]
print(type(b))

# get type of element 3 (bool)
c = a[3]
print(type(c))

d = ('a','b','c','a')
print(d.count('a')) # 2
print(len(d)) # 4

# convert a tupple to a list
my_list = list(d)
print(my_list)
print(type(my_list))

# convert list back to tuple
my_tupple = tuple(my_list)

# comapre the size in bytes between list and tuple
print(f"The list is {sys.getsizeof(my_list)} bytes")
print(f"The tuple is {sys.getsizeof(my_tupple)} bytes")


# Slicing allows accessing parts of tuple with ::
print(my_tupple[1:3])
print(my_tupple[::2])
print(my_tupple[1::])

# create the tuple and elements
new_tuple = "Mark", 78, "London"
# assign the same elements to vars. Must have same number of vars as elements in tuple
name, age, city = new_tuple
print(name)
print(age)
print(city)

# tuples are slightly more efficient that lists
print("To create 1,000,000 lists takes:")
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print("To create 1,000,000 tuples takes:")
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))