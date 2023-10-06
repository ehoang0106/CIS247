def add_num():
    quit = False
    while not quit:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        sum = num1+num2
        

        with open('data\\results.txt', 'a') as file:
            file.write(str(num1)+ " + " + str(num2) + " = " + str(sum) + "\n")
        print("Successfully added to results.txt")
        choose = input("Do you want to continue? (y/n) ").lower()
        if choose == 'n':
            quit = True
            with open('data\\results.txt', 'r') as file:
                for line in file.readlines():
                    print(line, end='')
            

add_num()

