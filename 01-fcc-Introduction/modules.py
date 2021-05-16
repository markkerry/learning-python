# https://docs.python.org/3/py-modindex.html

# import a module
import random

# create some variables
feet_in_mile = 5280
meters_in_km = 1000

# function to get a files extension
def get_file_ext(filename):
    return filname[filename.index(".") + 1:]

# function to choose a random number from 1 to x
def roll_dice(num):
    return random.randint(1, num)