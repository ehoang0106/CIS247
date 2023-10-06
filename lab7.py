
def load_employee():
    employees = {}
    
    with open ("employees.txt") as file:
        for line in file:
            id, *name = line.split()
            employees[id] = name
    return employees


def lookup_employee(id:int):
    employees = load_employee()
    return {id:employees[id]}
            
def lookup_ID(first:str,last:str):
    employees = load_employee()
    for id,name in employees.items():
        if first == name[0] and last == name[-1]:
            return {id:name}
    return None


def main():
    quit = False
    while not quit:
        choose = int(input("Enter (1) to look up employee base on ID | (2) to look up ID base on first and last name | (3) to quit: "))
        if choose == 1:
            try:
                id = input("Input ID: ")
                if not id.isdigit():
                    raise Exception("You did not enter integer")
                return_employee = lookup_employee(id)
                print(f"ID: {id} | Name: {' '.join(return_employee[id])}")
                
            except KeyError:
                print("ID not found")
            except Exception as err:
                print(err)
        elif choose == 2:
            try:
                first = input("Input first name: ")
                last = input("Input last name: ")
                return_employee = lookup_ID(first,last)
                if return_employee == None:
                    raise Exception("Unable to find employee")
            
                for id,name in return_employee.items():
                    print(f"ID: {id} | Name: {' '.join(name)}")


            except Exception as err:
                print(err)
        elif choose == 3:
            quit = True
            print("Thank you for using this program!")


            


main()