class SalesPersons:
    def __init__(self, name, pay_rate):
        self._name = name
        self._pay_rate = pay_rate

        #self._sales keeps track of each sale this employee made. It will containt floating point values
        self._sales = []
        
        #hours work this week
        self._num_hour = 0

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

    def add_sale(self, sale_amount):
        #Add a new sale to this employee's list of sales

        self._sales.append(sale_amount)



    def hours_worked(self, num_hours):
        #user is logging that this SalesPerson worked 'num_hours' hours today

        self._num_hour += num_hours

    def pay_employee(self):
        #calculate how much this employee is owned for the week and reset weekly hours

        amount_owed = self._pay_rate * self._num_hour

        #A new week is starting, so reset num hours worked
        self._num_hour = 0

        return amount_owed
    
    def __str__(self):
        return_string = f'Employee name {self._name}' + '\n'
        return_string += f'Number of Sales:{len(self._sales)}\n'
        return_string += "List of Sales: \n"

        total_sales = 0

        for sale in self._sales:
            return_string += f'${sale:.2f}\n'
            total_sales += sale

        return_string += "Total Sales Amount: \n"
        return_string += f'${total_sales}'
        return return_string