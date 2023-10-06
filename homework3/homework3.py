

def load_file():
    score_list = {}
    with open("scores.txt") as file:
        for line in file:
            month,day,*scores = line.split()
            date = month + " " + day
            score_list[date] = scores
    return score_list

def view_scores(score_list):
    if score_list == {}:
        print("No data to view")
    else:
        for date,score in score_list.items():
            scores = ', '.join(str(score) for score in score)
            print(f"On {date}, you scored {scores}")


def score_exists_for_date(date):
    scores_list = load_file()
    if date in scores_list.keys():
        return True
    else:
        return False
            
def write_data(score_list):
    with open("scores.txt", 'w') as file:
        for date, score in score_list.items():
            scores = ' '.join(str(score) for score in score)
            file.write(f"{date} {scores}\n")        

def add_score(scores_list):
    valid_day = False
    while not valid_day:
        day = int(input("Enter day: "))
        if day < 1 or day > 31:
            print("You entered wrong format of day. Enter again!")
        else:
            valid_day = True
    
    month = input("Enter month: ")
    
    day = str(day)
    date = day + " " + month
    exist = score_exists_for_date(date)
    if exist == True:
        print("Scores already exists Do not enter new data")
    else:
        valid_score = False
        while not valid_score:
            score = int(input("Enter score: "))
            if score < 0 or score > 300:
                print("The score must be in range from 1 to 300. Enter again!")
            else:
                valid_score = True
        if date not in scores_list:
            scores_list[date] = [score]
        else:
            scores_list[date].append(score)

    return scores_list


def average_scores():
    numerator = 0
    denominator = 0
    with open("scores.txt") as file:
        for line in file:
            month, day, *scores = line.split()
            for score in scores:
                numerator += int(score)
                denominator += 1
        average = numerator/denominator
        print(f"Your average score is: {average:,.2f}")
        
        
    
def num_300s():
    count = 0
    with open("scores.txt") as file:
        for line in file:
            month, day, *scores = line.split()
            for score in scores:
                if score == '300':
                    count +=1
        print(f"{count} times you scored 300")

        
def main():
   
    with open("scores.txt",'w') as file:
        scores = load_file()
        while True:
            choose = int(input("(1) to quit | (2) to view score | (3) to add score | (4) to view average score | (5) to view number of 300s: "))

            if choose == 1:
                #write data to file before quit
                write_data(scores)
                break
            elif choose == 2:
                view_scores(scores)
            elif choose == 3:
                add_score(scores)
            elif choose == 4:
                average_scores()
            elif choose == 5:
                num_300s()
            else:
                print("You chose wrong option. Please choose again!")
    

main()