class Transaction:

    def __init__(self,amount, is_withdrawal):
        self._amount = amount
        self._is_withdrawal = is_withdrawal

    def is_withdrawal(self):
        return self._is_withdrawal
    

    def __str__(self):
        return_string = ""
        if self._is_withdrawal == True:
            return_string += f'Withdrawal: -${self._amount:,.2f}'
        else:
            return_string += f'Deposit: +${self._amount:,.2f}'

        return return_string