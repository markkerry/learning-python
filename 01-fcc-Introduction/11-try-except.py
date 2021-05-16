# except meaning exception
# can catch a specific error
try:
    10/0 # in here for the ZeroDivisionError catch/except
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")