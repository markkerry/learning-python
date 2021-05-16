# Create a Student data type
class Student:
    # attributes (variables which are called properties in PowerShell)
    # This will always be the same each time the class is called
    created_by = "Mark"
    # create an initialise function. 
    # creates an object with 3 params which become attributes of the object
    def __init__(self, name, age, passed):
        self.name = name
        self.age = age
        self.passed = passed