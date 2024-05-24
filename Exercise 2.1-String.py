#1. Write a Python program to calculate the length of a string.

str1 = input("Enter a string:")
print("Length of the string:",len(str1))

#2. Write a Python program to count the number of characters (character frequency) in a string.

str1 = input("Enter a string:")
count = 0
for char in str1:
    if char.isalpha():
        count += 1
print("The number of characters in this string is:", count)

#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a
#string. If the string length is less than 2, return instead of the empty string

def new_string(input_string):
    count = len(input_string)
    if count < 2:
        return ""
    new_string = input_string[0:2] + input_string[count - 2:count]
    return new_string

str1= input("Enter a string:")
print(new_string(str1)) 


#4. Write a Python program to get a string from a given string where all occurrences of its first
#char have been changed to '$', except the first char itself.

def change_char(str1):
    char= str1[0].lower()
    str1 = str1.replace(char,'$')
    str1 = char+str1[1:]
    return str1

str1= input("Enter a string:")
print(change_char(str1))


#5. Write a Python program to get a single string from two given strings, separated by a space and
#swap the first two characters of each string.

def swap(str1,str2):
    new_str1=str2[:2]+str1[2:]
    new_str2=str1[:2]+str2[2:]
    result = new_str1+' '+new_str2
    return result

string1 = input("Enter first string:")
string2 = input("Enter second string:")

result= swap(string1,string2)
print(result)

#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
#the given string already ends with 'ing' then add 'ly' instead. If the string length of the given
#string is less than 3, leave it unchanged

str1= input("Enter a string:")
if len(str1)>3 and "ing" not in str1:
    print(str1+"ing")
elif len(str1)>3 and "ing" in str1:
    print(str1+"ly")
elif len(str1)<=3:
    print("String Unchanged:",str1)

#7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a
#given string, if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
#Return the resulting string

string1= ("he is not a poor guy")
print(string1.find('not'),string1.find('poor'))


#8. Write a Python function that takes a list of words and returns the length of the longest one

def longest_word(words):
    return max(len(word) for word in words)

lst1 = []
for i in range(4):
  lst1.append(input("Enter string"))
print("Existing list:",lst1)
#list(input("Enter list of words:"))
print(longest_word(lst1))

#9. Write a Python program to remove the nth index character from a nonempty string
#AI & ADVANCED ANALYTICS

def remove_char(input_string, index):
    char_list = list(input_string)
    char_list.pop(index)
    return ''.join(char_list)

str1 = input("Enter a string:")
n = int(input("Enter the index of char to be removed:"))
result = remove_char(str1, n)
print(result)

#10. Write a Python program to change a given string to a new string where the first and last chars
#have been exchanged

def swap(str1):
    new_str1=str1[-1:]+str1[1:-1]+str1[:1]
    return new_str1

string1 = input("Enter first string:")
result= swap(string1)
print(result)

#11. Write a Python program to remove the characters which have odd index values of a given
#string.

def remove_odd_index_chars(text):
    return ''.join([char for index, char in enumerate(text) if index % 2 == 0])

input_string = input("Enter a string:")
result = remove_odd_index_chars(input_string)
print(result) 

#12. Write a Python program to count the occurrences of each word in a given sentence

str1= input("Enter a string:")
word= input("Enter the word to count:")

word_lst= str1.split()
count=0
for i in word_lst:
    if i==word:
        count+=1

print(f"Count of '{word}' is: {count}")

#13. Write a Python script that takes input from the user and displays that input back in upper and
#lower cases

str1 = input("Enter a string:")
upper= str1.upper()
lower= str1.lower()
print("Upper Case:",upper)
print("Lower Case:",lower)

#14. Write a Python program that accepts a comma separated sequence of words as input and
#prints the unique words in sorted form (alphanumerically).

items = input("Input comma-separated sequence of words: ")
words = sorted(set(items.split(',')))
print(",".join(words))

#15. Write a Python function to create the HTML string with tags around the word(s).

def wrap_with_tags(word, tag):
    return f"<{tag}>{word}</{tag}>"

word_to_wrap = input("Enter a String:")
tag_to_use = input("Enter the HTML tag to be used:")
result = wrap_with_tags(word_to_wrap, tag_to_use)
print(result) 

#16. Write a Python function to insert a string in the middle of a string.

str1= input("Enter the original string:")
new_str = input("Enter a string to be inserted in middle:")
str_len = len(str1)

if str_len%2 ==0:
    mid_of_str = int(str_len/2)
else:
    mid_of_str = int((str_len+1)/2)
res = str1[:mid_of_str]+ new_str+' ' +str1[mid_of_str:]
print(res)


#17. Write a Python function to get a string made of 4 copies of the last two characters of a
#specified string (length must be at least 2)

str1= input("Enter a string:")
while (len(str1)>2):
    n= str1[-2:]
    print(n*4)
    break

#18. Write a Python function to reverses a string if it's length is a multiple of 4

str1=input("Enter a String which is a multiple of 4:")
if len(str1)%4==0:
    print(str1[::-1])
else:
    print("The string is not a multiple of 4!")

#19. Write a Python function to convert a given string to all uppercase if it contains at least 2
#uppercase characters in the first 4 characters.

def to_uppercase(str1):
    num_upper = 0
    for letter in str1[:4]:
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper()
    return str1

str1=input("Enter a string:")
print(to_uppercase(str1))

#20. Write a Python program to check whether a string starts with specified characters

str1 = input("Enter a string:")
specific_char = 'a e i o u'
if str1[0].lower() in specific_char:
    print("The word starts with the specified character,",str1[0])
else:
    print("The word doesn't start with the specified characters")
