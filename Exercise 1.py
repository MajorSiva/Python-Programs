#1.   Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.

     original_string = input("Enter a String:")
     new_string = original_string[:1] + original_string[-2:]
     print(new_string) 

#2.   Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
     
def swap(str1,str2):
    new_str1=str2[:2]+str1[2:]
    new_str2=str1[:2]+str2[2:]
    result = new_str1+' '+new_str2
    return result

string1 = input("Enter first string:")
string2 = input("Enter second string:")

result= swap(string1,string2)
print(result)
      
#3.   Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string.

string1= ("he is not a poor guy")
print(string1.find('not'),string1.find('poor'))

#4.   Write a Python program to count the occurrences of a word in a given sentence

str1 = input("Enter a string:")
str2 = str1.split(' ')
word = input("Enter the word from string to be counted:")

res = str2.count(word)
print(res)

#5.   Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

items = input("Input comma-separated sequence of words: ")
words = sorted(set(items.split(',')))
print(",".join(words))

#6.   Write a Python program to insert a string in the middle of a string.

str1= input("Enter the original string:")
new_str = input("Enter a string to be inserted in middle:")
str_len = len(str1)

if str_len%2 ==0:
    mid_of_str = int(str_len/2)
else:
    mid_of_str = int((str_len+1)/2)
res = str1[:mid_of_str]+ new_str+' ' +str1[mid_of_str:]
print(res)

#7.   Write a Python program to convert the first letter of each word in given string to uppercase.

import string

str1 = input("Enter a sentence:")
cap_str1 = string.capwords(str1)
print(cap_str1)

#8.   Write a Python program to check whether a string starts with specified characters

str1 = input("Enter a string:")
specific_char = 'a e i o u'
if str1[0].lower() in specific_char:
    print("The word starts with the specified character,",str1[0])
else:
    print("The word doesn't start with the specified characters")


#9.   Write a Python program to remove duplicates from a list.

lst1 = list(input("Enter a list of numbers:"))
lst2 = sorted(set(lst1))
print(lst2)

#10.  Write a Python program to check a list is empty or not.

lst1 = list(input("Enter a list of elements:"))
print(lst1)
if len(lst1) ==0:
    print("The list is empty!")
else:
    print("The is not empty!")

#11.  Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']

def remove_elements_by_index(lst, indices):
    for index in sorted(indices, reverse=True):
        del lst[index]
    return lst

my_list = ['Red','Green','White','Black','Pink','Yellow']
indices_to_remove = [0,4,5]
new_list = remove_elements_by_index(my_list, indices_to_remove)
print(new_list)


#12.  Write a Python program to get the difference between the two lists.

lst1=list(input("Enter elements of list 1:"))
lst2=list(input("Enter elements of list 2:"))
res= list(set(lst1)-set(lst2))
print(res)

#13.  Write a Python program to replace the last element in a list with another list.

def replace(og_list,rep_lst):
    if not og_list:
        return rep_lst
    else:
        return og_list[:-1]+rep_lst

og_lst = list(input("Enter Original list elements:"))
rep_lst= list(input("Enter replacement lsit elements:"))
new_lst = replace(og_lst,rep_lst)
print(new_lst)

#14.  Write a Python program to check if all items of a list is equal to a given string.

def equal_lst(lst1, lst2):
    return lst1 == lst2

lst1 = list(input("Enter the 1st list elements:"))
lst2 = list(input("Enter the 2nd list elements:"))

if equal_lst(lst1, lst2):
    print("The lists are equal.")
else:
    print("The lists are not equal.")


#15.  Write a Python program to concatenate elements of a list to a string.

lst1 = list(input("Enter list of elements:"))
concat_str = "".join(lst1)
print(lst1)
print(concat_str)

#16.  Write a Python program to reverse a tuple.

def reverse_tuple(tuples):
    return tuples[::-1]

original_tuple = tuple(input("Enter tuple elements:"))
reversed_tuple = reverse_tuple(original_tuple)
print("Original Tuple:", original_tuple)
print("Reversed Tuple:", reversed_tuple)

#17.  Write a python program to check if a set a subset of another set.

set1= list(input("Enter set1 values:"))
set2 = list(input("Enter set2 values:"))
if set(set2)<=set(set1):
    print("Set 1 is a subset of Set 2")
else:
    print("Set 1 is not a subset of Set 2")

#18.  Write a python program to check if a set is a superset of another set.

def is_superset(set_a, set_b):
    for element in set_b:
        if element not in set_a:
            return False
    return True

A = set(input("enter setA values:"))
B = set(input("Enter setB values:"))

print(is_superset(A, B))


#19.  Write a python program to find the union and intersection of 2 sets.

lst1 = set(input("Enter set 1 elements:"))
lst2 = set(input("Enter set 2 elements:"))

print("Set Union:", sorted(lst1|lst2))
print("Set Intersection:",sorted(lst1&lst2))

#20.  Write a python program to find the elements in s1 that are not in s2.

lst1 = set(input("Enter set 1 elements:"))
lst2 = set(input("Enter set 2 elements:"))

print("Set Union:", sorted(lst1-lst2))

#21.  Write a python program to check if 2 sets are disjoint.

def are_disjoint(set1, set2):
        if set1 == set2:
            print("Not a Disjoint")
        else:
              print("Is a Disjoint")
        return 0
s1 = set(input("Enter set 1 values:"))
s2 = set(input("Enter set 2 values:"))
print(are_disjoint(s1, s2))


#22.  Write a python program to add all elements from another set to an existing set.

a = set(input("Enter set values:"))
xs = set(input("Enter the updation set values:"))
a.update(xs)
print(sorted(a))

#23.  Write a python program to remove an element from a set if it exists.

def remove_element(my_set, element):
    if element in my_set:
        my_set.discard(element)
        print(f"Element '{element}' removed from the set.")
    else:
        print(f"Element '{element}' does not exist in the set.")

my_set = {1, 2, 3, 4}
element_to_remove = 3
remove_element(my_set, element_to_remove)
print("Updated set:", my_set)


#24.  Write a python code to delete keys from the dictionary.

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
del my_dict['key1']
print(my_dict)  

#25.  Write a python code to sort the based on keys in the dictionary.

myDict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}
print(sorted_dict)
