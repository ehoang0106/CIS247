"""
1. On Canvas, there is a file named NBAChampions.txt. Add this file to your project. It contains the names, in order, of the basketball teams that won the NBA Championship from 1947-2020.

In main, call a function named load_data which loads these names into a dictionary, with each key a team name and each value a list of years that team won the NBA Championship. To determine the year each team won, use enumerate and start it at 1947:
You can start an enumerate at a number other than 0 by passing it as a second argument:
for year, team in enumerate(file, 1947):
After the data is loaded, back in main, enter a while loop and ask the user to enter a team name. If they enter “q”, the program should quit.
Otherwise, call a function find_wins which prints out the years in which the entered team won the NBA Championship (or prints a message saying the team wasn’t found)

"""

"""
create function load_data()
create names = {}
names[team_name] = {year}
for year, team in enumerate(file, 1947)
create find_wins()

"""

def load_data():
    names = {}
    with open("exam2_review1\\NBA.txt") as file:
        for year, team in enumerate(file,1947):
            team = team.strip()
            if team in names:
                names[team].append(year)
            else:
                names[team] = [year]


    return names

def find_wins(team_name):
    names = load_data()
    for team, years in names.items():
        if team_name.lower() == team.lower():
            return team, ', '.join(str(year) for year in years)




def main():
    quit = False
    while not quit:
        try:
            enter_team = input("Enter team name or 'q' to quit: ")
            if enter_team == 'q':
                quit = True
            else:
                name,years = find_wins(enter_team)
                print(f"{name} is a NBA Championship of the following year(s): {years}")
            
        except TypeError:
            print("Team was not found!")

main()

