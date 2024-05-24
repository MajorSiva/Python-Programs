#1. Write a Python program to create a tuple.

tup=tuple(input("Enter tuple elements:"))
print(tup)

#2. Write a Python program to create a tuple with different data types

tup1=tuple(input("Enter diff datatype elements for tuple:"))
print(tup1)

#3. Write a Python program to add an item in a tuple

original_tuple = tuple(input("Enter elements for tuple:"))
new_element = input("Enter a number to add item in tuple:")
appended_tuple = original_tuple + (new_element,)
print(appended_tuple)

#4. Write a Python program to convert a tuple to a string.

tup = tuple(input("Enter tuple elements:"))
print(tup)
result = ''.join(tup)  
print(result)

#5. Write a Python program to check whether an element exists within a tuple

tup= tuple(input("Enter elements for tuple:"))
n=input("Enter the element to check:")
if n in tup:
    print("The element",n,"exists")
else:
    print("The element",n,"does not exists")

#6. Write a Python program to convert a list to a tuple

tup = tuple(input("Enter tuple elements:"))
print(tup)
result = ''.join(tup)  
print(list(result))

#7. Write a Python program to remove an item from a tuple

def remove_tuple(tup,n):
    lst= list(tup)
    lst.remove(n)
    tup=tuple(lst)
    return tup

tup=tuple(input("Enter tuple elements:"))
n= input("Enter the element to be removed:")
print(remove_tuple(tup,n))

#8. Write a Python program to find the length of a tuple

tup=tuple(input("Enter tuple elements:"))
print(len(tup))

#9. Write a Python program to convert a tuple to a dictionary

key_tup=tuple(input("Enter key tuple element:"))
val_tup = tuple(input("Enter value tuple elements:"))
print(dict(zip(key_tup,val_tup)))

#10. Write a Python program to reverse a tuple

def reverse_tuple(tuples):
    return tuples[::-1]

original_tuple = tuple(input("Enter tuple elements:"))
reversed_tuple = reverse_tuple(original_tuple)
print("Original Tuple:", original_tuple)
print("Reversed Tuple:", reversed_tuple)
