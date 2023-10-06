import random

def flip():
    coin = random.randint(0,1)
    if coin == 0:
        return "Heads"
    else:
        return "Tails"

def main():
    toss = flip()
    guess = int(input("Choose 1 for Heads or choose 2 for Tails: "))
    
    result = ""
    if guess == 1:
        result = "Heads"
    else:
        result = "Tails"

    if result == toss:
        print(f"Correct! It's a {toss}")
    else:
        print(f"Incorrect! It's a {toss}")

main()