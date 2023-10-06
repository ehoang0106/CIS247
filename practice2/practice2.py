

def add_employee(employees):

    ID = input("Enter ID: ")
    name = input("Enter Name: ")
    salary = input("Enter Salary: ")
    if ID in employees:
        print("That employee ID is taken!")
    else:
        employees[ID] = {name:salary}
    
    return employees

def update_salary(employees):
    
    employee_ID = input("Enter ID to update salary: ")
    try:
        for name in employees[employee_ID].keys():
            if employee_ID in employees.keys():
                salary = input("Enter new salary: ")
                employees[employee_ID][name] = salary
        
    except:
        print("Employee not found!")
    return employees

def print_employees(employees):
    for ID in employees.keys():
        for name, salary in employees[ID].items():
            print(f"\nID: {ID} \nName: {name} \nSalary: ${float(salary):,.2f}")

def main():
    employees = {}
    while True:
        choose = int(input("(1) for add employee (2) update salary (3) view employee (4) quit: "))
        if choose == 1:
           add_employee(employees)
        elif choose == 2:
            update_salary(employees)
        elif choose == 3:
            if employees == {}:
                print("No data")
            else:
                print_employees(employees)
        else:
            break
main()



