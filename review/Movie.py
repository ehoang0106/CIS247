class SalesPerson:
    
    def __init__(self, name, pay_rate):

        self._name = name
        self._pay_rate = pay_rate

        self._sales = []
        self._work_hours = 0

        

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def pay_rate(self):
        return self._pay_rate
    @pay_rate.setter
    def pay_rate(self, new_pay_rate):
        self._pay_rate = new_pay_rate

    def add_sale(self, amount_sale):
        self._sales.append(amount_sale)

    def hours_worked(self, hour):
        self._work_hours += hour

    def pay_employee(self):

        earned = self._pay_rate * self._work_hours
        self._work_hours = 0

        return earned
    
    def __str__(self):
        return_string = f'Employee name: {self._name}\n'
        return_string += f'Number of sales: {len(self._sales)}\n'
        return_string += 'List of sale: \n'
        total_sales = 0
        for sale in self._sales:
            return_string += f'${sale:.2f}\n'
            total_sales += sale
        return_string += f'Total sales amount: ${total_sales}\n'
        
        return return_string
            

