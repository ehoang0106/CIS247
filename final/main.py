from Transaction import Transaction
from Account import Account

def main():
    acc = Account(0)
    
    
    acc.deposit(500)
    acc.withdraw(100)
    print(acc)

    acc.withdraw(300)
    acc.deposit(400)
    print(acc)

    acc.deposit(5000)
    acc.deposit(3000)
    acc.withdraw(2000)
    acc.withdraw(200)
    print(acc)



main()