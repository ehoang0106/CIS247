

def average(lst):
    return sum(lst)/float(len(lst))

def get_score(game):
    integer = False
    while not integer:
        score = input(f"Input score of game {game}: ")
        if score.isdigit():
            integer = True
        else:
            print("You did not enter a integer. Try again")
    return int(score)

    

# def perform_calculations(score_list):
#     avg = average(score_list)
#     min = 0
#     max = 0
#     first_number_entered = False
#     for score in score_list:
#         if not first_number_entered:
#             min = score
#             max = score
#             first_number_entered = True
#         else:
#             if score > max:
#                 max = score
#             if score < min:
#                 min = score
#     return min,max,avg

def perform_calculations(score_list):
    avg = average(score_list)
    min = score_list[0]
    max = score_list[0]
    for score in score_list:
        if score > max:
            max = score
        if score < min:
            min = score
    return min,max,avg
    

def main():
    game_list = []
    game = int(input("How many games the player played: "))
    for i in range (1, game + 1):
        val = get_score(i)
        game_list.append(val)
    
    min,max,avg = perform_calculations(game_list)

    print(f"The average score is: {avg:,.2f}")
    print(f"The lowest score is: {min}")
    print(f"The highest score is: {max}")

    
main()