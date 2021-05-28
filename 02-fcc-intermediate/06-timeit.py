# time two commands
from timeit import default_timer as timer

# create a list with 1m a's
my_list = ['a'] * 1000000

# Bad, don't use this method
# start the timer
start = timer()
# put each element of list to a string
my_string = ''
for i in my_list:
    my_string += i
# stop the timer
stop = timer()
# print the time it took
print(stop-start)

# Good, use this method
# start the timer
start = timer()
# put each element of list to a string
my_string = ''.join(my_list)
stop = timer()
print(stop-start)
