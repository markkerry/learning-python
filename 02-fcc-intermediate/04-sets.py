# unordered and mutable but does bit allow duplicates
my_set = {1, 2, 3, 4}
print(my_set)

# can't have duplicates and will print unordered
new_set = set("Hello")

new_set.add(1)
new_set.add(2)
new_set.add(3)

print(new_set)
new_set.remove(3)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}

u = odds.union(evens)
print(u)