def input_integer():
    integer = False

    while not integer:
        num1 = input("Number 1: ")
        num2 = input("Number 2: ")
        if num1.isdigit() and num2.isdigit():
            integer = True
            print("-------------------")
            print((f"Number 1 is {num1}"))
            print((f"Number 2 is {num2}"))
            sum_num = num1+num2
            print(f"Sum of 2 numbers:", int(num1)+int(num2))
        else:
            print("The values intered is not an integer, please enter again")

def quit():
    quit = False

    while not quit:
        option = input("Do you want to continue (yes/no): ").lower()
        if option == "no":
            quit = True
            print("Thank you for using my software!")
        else:
            input_integer()

def main():
    input_integer()
    quit()


main()



