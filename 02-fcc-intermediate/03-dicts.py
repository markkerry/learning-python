# data type which is unordered and mutable. Key-value pairs

a = {
    "name": "Mark",
    "age": 65,
    "city": "London"
}

# To create via the dict function
b = dict(name="Kerry", age=99, city="Stoke")
print(b)

# get the name value
c = a["name"]
print(c)

# add a key/value to a dict
a["email"] = "mark@email.com"
print(a)

# delete an item
del a["age"]
print(a)

if "name" in a:
    print(a["name"])

try:
    print(a["age"])
except:
    print("Error: age not in dict")

for k in a.keys():
    print(k)

for v in a.values():
    print(v)

# Update dict b to be the same as dict a
b.update(a)
print(b)