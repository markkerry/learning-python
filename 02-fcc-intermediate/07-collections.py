from collections import Counter, defaultdict, namedtuple, OrderedDict, deque

# Counter
a = "aaaabbbbccccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

# print first most common 
print(my_counter.most_common(1))

# print top two most common
print(my_counter.most_common(2))

# convert to list and get all the elements
print(list(my_counter.elements()))

# namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

# OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)


# defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print((d['a']))


# deque
c = deque()
c.append(1)
c.append(2)
c.appendleft(3)
print(c)
