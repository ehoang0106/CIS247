from FullName import *

def main():
    
    first_name1 = input("Input first name 1: ")
    last_name1 = input("Input last name 1: ")
    first_name2 = input("Input first name 2: ")
    last_name2 = input("Input last name 2: ")
    name1 = FullName(first_name1, last_name1)
    name2 = FullName(first_name2, last_name2)
    names = [name1,name2]
    names.sort()
    for n in names:
        print(n)

main()