# create your own data type with a class

obj_str = type("String")
obj_int = type(34)
obj_float = type(1.4)
obj_bool = type(True)

print(f"The data type for a string is {obj_str}")
print(f"The data type for an integer is {obj_int}")
print(f"The data type for a float is {obj_float}")
print(f"The data type for a boolean is {obj_bool}")

# import the Student class from the student_class.py file
from student_class import Student

student1 = Student("Mark", 67, True)
obj_student = type(student1)
print(f"The data type for the Student class is {obj_student}")
print(f"Student's name is {student1.name}")
print(f"Student's age is {student1.age}")
print(f"Student passed: {student1.passed}")
print(f"Class created by {student1.created_by}")