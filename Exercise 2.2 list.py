#1. Write a Python program to sum all the items in a list.

lst1= [1,2,3,4]
res=0
for i in range(0,len(lst1)):
    res=res+lst1[i]
print(res)

#2. Write a Python program to multiplies all the items in a list.

lst1= [1,2,3,4]
res=1
for i in range(0,len(lst1)):
    res=res*lst1[i]
print(res)

#3. Write a Python program to get the largest number from a list.

lst1=list(input("Enter list elements:"))
print(max(lst1))

#4. Write a Python program to get the smallest number from a list

lst1=list(input("Enter list elements:"))
print(min(lst1))

#5. Write a Python program to remove duplicates from a list.

lst1=list(input("Enter list elements:"))
n=sorted(set(lst1))
print(n)

#6. Write a Python program to check a list is empty or not.

lst1=list(input("Enter list elements:"))
if len(lst1)==0:
    print("This list is empty")
else:
    print("The list is not empty")

#7. Write a Python program to clone or copy a list.

lst1=list(input("Enter list elements:"))
print(lst1)
lst2= lst1[:]
print(lst2)

#8. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
   Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
   Expected Output : ['Green', 'White', 'Black']

def remove_elements_by_index(lst, indices):
    for index in sorted(indices, reverse=True):
        del lst[index]
    return lst

my_list = ['Red','Green','White','Black','Pink','Yellow']
indices_to_remove = [0,4,5]
new_list = remove_elements_by_index(my_list, indices_to_remove)
print(new_list)

#9. Write a Python program to get the difference between the two lists.

lst1=list(input("Enter list 1 elements:"))
lst2=list(input("Enter list 2 elements:"))
lst=set(lst1)-set(lst2)
print(lst)

#10. Write a Python program to find all the values in a list are greater than a specified number.

def check(lst1,n):
    for i in lst1:
        if n>=i:
            return False
    return True

lst1=list(input("Enter list elements:"))
n=input("Enter a number:")
if check(lst1,n):
    print("The list values are greater than the specified number",n)
else:
    print("The list values are lesser than the specified number",n)

#11. Write a Python program to find a tuple, the smallest second index value from a list of tuples.

i = [(4, 1), (1, 2), (6, 0)]
print(min(i, key=lambda n: (n[1], -n[0])))

#12. Write a Python program to check if the n-th element exists in a given list

def check_element_exists(lst, n):
    if n < len(lst) and lst[n] is not None:
        return True
    return False

# Example usage:
my_list = list(input("Enter list elements:"))
n = int(input("Enter a number:"))
result = check_element_exists(my_list, n)
print(f"Element at index {n} exists: {result}")

#13. Write a Python program to replace the last element in a list with another list.

def replace(og_list,rep_lst):
    if not og_list:
        return rep_lst
    else:
        return og_list[:-1]+rep_lst

og_lst = list(input("Enter Original list elements:"))
rep_lst= list(input("Enter replacement lsit elements:"))
new_lst = replace(og_lst,rep_lst)
print(new_lst)

#14. Write a Python program to check if all items of a list is equal to a given string

def equal_lst(lst1, lst2):
    return lst1 == lst2

lst1 = list(input("Enter the 1st list elements:"))
lst2 = list(input("Enter the 2nd list elements:"))

if equal_lst(lst1, lst2):
    print("The lists are equal.")
else:
    print("The lists are not equal.")

#15. Write a Python program to convert a string to a list

str1= input("Enter a string value: ")
lst1= list(str1)
print("The string to list output is:",lst1)

#16. Write a Python program to concatenate elements of a list

lst1=list(input("Enter list 1 elements:"))
lst2=list(input("Enter list 2 elements:"))
lst= lst1+lst2
print(lst)

#17. Write a Python program to create multiple lists

list1, list2, list3, list4 = ([] for _ in range(4))

#18. Write a Python program to find common items from two lists

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    common_elements = a_set & b_set
    return list(common_elements)

lst1 = list(input("Enter the 1st list elements:"))
lst2 = list(input("Enter the 2nd list elements:"))
print(common_member(lst1, lst2))

#19. Write a Python program to generate all sublists of a list

def sublists(lst):
    n = len(lst)
    sublists = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublists.append(lst[i:j])
    return sublists

lst1 = list(input("Enter list elements:"))
sublists_nested = sublists(lst1)
print(sublists_nested)

#20. Write a Python program to get unique values from a list

lst1=list(input("Enter list elements:"))
print("The unique values from the list is/are:",sorted(set(lst1)))