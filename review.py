# #answer 1
# import random



# def main():
#     #Generate 2 random nums
#     num1 = random.randint(0,999)
#     num2 = random.randint(0,999)

#     correct = num1 + num2

#     guess = int(input(f"What is {num1} + {num2}: "))

#     if guess == correct:
#         print("Correct!")
#     else:
#         print(f"Incorrect! The correct answer is: {correct}")



# main()

# #answer 2
# def main():

#     smallest = 0
#     largest = 0

#     first_num_entered = False
#     while True:
#         integer = input("Input integer or 'quit' to stop: ")
#         if integer == "quit":
#             break
        
#         integer = int(integer)
#         if not first_num_entered:
#             largest = integer
#             smallest = integer
#             first_num_entered = True
#         else:
#             if integer > largest:
#                 largest = integer
#             if integer < smallest:
#                 smallest = integer
#     if not first_num_entered:
#         print("You did not enter any number")
#     else:
#         print(f"Largest # is {largest} smallest # is {smallest}")

# main()


#answer #3

def get_sales(div_num):
    sales = input(f'What are the sales for division {div_num}: ')
    return float(sales)

def find_highest(sales_list):
    highest_sale = 0
    div_of_highest = 0
    for index, sales in enumerate(sales_list):
        if sales > highest_sale:
            highest_sale = sales
            div_of_highest = index + 1
    print(f"The highest amount of sales was {highest_sale} from division {div_of_highest}")
        


def main():

    sales = []
    num_div = int(input("How many divisions: "))

    for i in range(1, num_div + 1):
        val = get_sales(i)
        sales.append(val)
    
    find_highest(sales)

        
main()


#answer4

# def main():
#     """ In a while loop, ask the players if they want to play again"""
#     while True:
#         player1 = input("Player 1: Select (p)aper, (r)ock, or (s)cissors: ").lower()
#         player2 = input("Player 2: Select (p)aper, (r)ock, or (s)cissors: ").lower()

#         if player1 == player2:
#             print("It's a tie!")
#         elif player1 == 'p' and player2 == 'r':
#             print("Player 1 wins: paper covers rock!")
#         elif player1 == 'p' and player2 == 's':
#             print("Player 2 wins: scissors cut paper!")
#         elif player1 == 'r' and player2 == 'p':
#             print("Player 2 wins: paper covers rock!")
#         elif player1 == 'r' and player2 == 's':
#             print("Player 1 wins: rock smashes scissors")
#         elif player1 == 's' and player2 == 'p':
#             print("Player 1 wins: scissors cut paper!")
#         elif player1 == 's' and player2 == 'r':
#             print("Player 2 wins: rock smashes scissors!")
#         else:
#             print("One of the players entered an invalid choice!")

#         choice = input("Would you like to play again, y/n? ").lower()
#         if choice == 'n':
#             break


# main()