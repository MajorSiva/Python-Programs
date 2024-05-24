#1. Write a Python program to read an entire text file.

with open('readme.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    print(line.strip()) 

#2. Write a Python program to read first n lines of a file.

inputFile = "readme.txt"
N = int(input("Enter N value: "))


with open(inputFile, 'r') as filedata:
    linesList = filedata.readlines()

    print(f"The following are the first {N} lines of the text file:")
    for textline in linesList[:N]:
        print(textline, end='')

filedata.close()

#3. Write a Python program to append text to a file and display the text

with open("readme.txt", "a") as myfile:
    myfile.write("Batman: Oops.My Bad.\n")

#4. Write a Python program to read last n lines of a file.

def LastNlines(fname, N):
    with open(fname) as file:
        for line in (file.readlines() [-N:]):
            print(line, end ='')
 
if __name__ == '__main__':
    fname = 'readme.txt'
    N = int(input("Enter number of lines to be displayed:"))
    LastNlines(fname, N)