"""
Write a Python program that asks the user to enter the name of the file they would like to open. If the file does not exist, ask them to try again (hint: use a while loop and a try/except block). If the file does exist, open it and do the following:
Load the swimmers into a dictionary such that each key is a swimmer's name and each value is a list of years that swimmer participated in the Olympics. Note: Each line in the file is a swimmer's first name, last name, followed by a list of years.
After the data has been loaded, use a dictionary comprehension to create a second dictionary. In this dictionary, each key should be a swimmer's name and each value should be how many times that swimmer participated in the Olympics. However, only swimmers who participated more than two times should be included.
Finally, print the data out!

"""

"""
Psuedo code

def enter_file():
    while True:
        try:
            if file does not exit:
                try again
            else:
                open file
                load_data
                swimmers = {}
                swimmers[name] = year
        except:
            file does not exit

def participated():

"""

def load_data(file_name):
    swimmers = {}
    with open(f"exam2_review2\\{file_name}") as file:
        for line in file:
            first, last, *year = line.split()
            swimmer = first+ " " +last
            swimmers[swimmer] = year
       
    return swimmers

def participated(swimmers):
    participated = {}
    for name, years in swimmers.items():
        ptced = len(years)
        if ptced > 2:
            participated[name]=ptced
    
    return participated

# def dict_comprehesion(swimmers):
#     participated = {key: len(value) for key, value in swimmers.items() if len(value)>2}
#     for key, value in participated.items():
#         return participated


def main():
    while True:
        file_name = input("Enter file name: ")
        try:
            swimmers = load_data(file_name)
            swimmers_participated = participated(swimmers)
            for name, time in swimmers_participated.items():
                print(f"{name} participated in the Olympics {time} times")
            break
        except:
            print("File does not exist. Enter again!")
    

main()