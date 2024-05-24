#1. Explain the scope of the variable 's' in the following program.
def f():
    print(s)
s = "I love Python training"
f()

#The Scope of the variable 's' is only inside the function and cannot be used anywhere in the program. 

#2. Write a program using Lambda in python.

x = lambda a, b: a * b
print(x(5, 6))

#3. Write python program using positional parameters or required parameters.

def greet(name, age):
    print(f"Hi, I am {name}. My age is {age}.")

greet("Siva", 21)

#4. Write python program using positional only.

def function(a, b, /, c, d, *, e, f): 
	print (a, b, c, d, e, f) 

function(1, 2, 3, d = 4, e = 5, f = 6) 

#5. Write python program using keyword Parameters and default parameters.

def greet(name, age=21):
    return f"Hello, {name}! You are {age} years old."

print(greet(name="Siva"))
print(greet(name="Prakash"))

#6. Write python program using variable length positional parameter.

def sum_all(*args):
	result = 0
	for num in args:
		result += num
	return result

print(sum_all(1, 2, 3, 4, 5))

#7. Write python program using variable length keyword parameter.

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Siva", age=21, city="Chennai")

#8. Write python program using keyword parameter.

def greet(name, age):
    return f"Hello, {name}! You are {age} years old."

print(greet(name="Siva",age=21))
print(greet(name="Prakash",age=21))

#9. Write a program to receive arguments from command line (as system arguments).

import sys

a= sys.argv[1:]
print(a)