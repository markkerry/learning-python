# ordered, mutable data type which allows for duplicate elements
# a list allows for different data types e.g int, bool, string
# starts with sqaure brackets

my_list = ["Azure", "AWS", "GCP"]
print(my_list)

# can create an empty list before appending data to it
# my_list2 = list()

for i in my_list:
    print(i)

if "Azure" in my_list:
    print("Azure in the list")
else:
    print("Azure not in the list")

print(len(my_list))

# add on-prem
my_list.append("On-prem")
print(my_list)

# remove the last one (on-prem)
my_list.pop()

# remove GCP
my_list.remove("GCP")

# other list methods
# .clear() method will remove the list
# .reverse()
# .sort()

# list comprehension
a = [1, 2, 3, 4, 5]
b = [i*i for i in a]
print(b)