#1. Write the syntax for try-finally block.

try:
  #statements
except:
  #statements
else:
  #statements
finally:
  #statements

#2. Write a python program for except clause with exception.

def div(a,b):
    try:
        n=a/b
        print(n)
    except:
        if b==0:
            print("Error:ZeroDivisionError")
a=int(input("Enter number A:"))
b=int(input("Enter number B:"))
div(a,b)

#3. Write a python program for except clause with multiple exception.

def div(a,b):
    try:
        n=a/b
        print(n)
    except ZeroDivisionError:
        print("Error:ZeroDivisionError")
    except ValueError:
        print("Invalid Input")

a=int(input("Enter number A:"))
b=int(input("Enter number B:"))
div(a,b)

#4. Write a python program for raising an exception using raise clause.

x =int(input("Enter x number:"))
y=int(input("Enter y number:"))
if y==0:
    raise ZeroDivisionError("Cannot divide by zero")

#5. Write a python program for user defined exceptions.

class UserdefinedException(Exception):
    pass
try:
    raise UserdefinedException("This is an example of a custom exception")
except UserdefinedException as error:
    print(f"A new exception occurred: {error}")

#6. Write a python program for custom exception

class InvalidAgeException(Exception):
    pass

try:
    input_num = int(input("Enter a number: "))
    if input_num < 18:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
except InvalidAgeException:
    print("Exception occurred: Invalid Age")
