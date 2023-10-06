import random

def get_name():
    name = input("Enter your name: ")
    return name

def get_email():
    email = input("Enter your email: ")
    return email

def calculate_ID():
    company_ID = random.randint(1000,9999)
    return company_ID

def get_account():
    x = get_name()
    y = get_email()
    z = calculate_ID()
    return x,y,z

def main():
    name,email,company_ID = get_account()
    print("\nName:",name)
    print("Email:",email)
    print("Company ID:",company_ID)

main()
    

