#creating empty list called transactions self._transaction = []
from Transaction import Transaction
class Account:

    def __init__(self, balance):

        self._balance = balance
        self.valid_balance(balance)
        self._transactions = []

    @property
    def balance(self):
        return self._balance
    
    def valid_balance(self, balance):
        if balance < 0:
            print("The balance is less than 0. Please enter valid number.")
            raise ValueError("Balance can't be less than 0")
        
    def withdraw(self, amount):
        if self._balance - amount < 0:
            print("Error: Not enough funds to complete withdrawal")
            return False
        else:
            self._balance -= amount
            trans = Transaction(amount, True)
            self._transactions.append(trans)
            return True
    
    def deposit(self, amount):
        self._balance += amount
        trans = Transaction(amount, False)
        self._transactions.append(trans)    

    def __str__(self):
        return_string = "--Transactions--\n"
        return_string += f'Number of transactions: {len(self._transactions)}\n'
        return_string += 'List of transactions: \n'
        
        for trans in self._transactions:
            return_string += f'\t{trans}\n'
        return_string += f'Account balance: ${self._balance:,.2f}\n'
        return return_string