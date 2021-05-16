# give this chef the same functionality as class in chef.py

# first import the chef class from chef.py
from chef import chef

# create a new class with name of chef class to inherit in the param
class chef2(chef):
    def make_rice(self):
        print("The chef2 makes rice")