from Movie import SalesPerson



def main():
    s1 = SalesPerson('Bob', 20)
    s2 = SalesPerson('Bill', 17)
    s1.add_sale(500)
    s1.add_sale(200)
    s1.hours_worked(8)
    s1.hours_worked(5)

    

    s2.add_sale(200)
    s2.add_sale(300)
    s2.hours_worked(8)
    s2.hours_worked(5)

   

    print(s1)
    print(s2)
    print(f"{s1._name}'s salary: {s1.pay_employee()}")
    print(f"{s2._name}'s salary: {s2.pay_employee()}")
main()