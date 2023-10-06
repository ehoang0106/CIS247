from SalesPerson import SalesPersons


def main():
    s1 = SalesPersons("Bob", 17.5)
    s2 = SalesPersons("Bill", 20.5)

    s1.add_sale(150)
    s1.add_sale(50)
    s2.add_sale(225.50)

    s1.hours_worked(10)
    s2.hours_worked(80)
    s1.hours_worked(5)
    s2.hours_worked(10)

    print(f'{s1.name} is paid {s1.pay_employee()}')
    print(f'{s1.name} is paid {s1.pay_employee()}')

    print(s1)

main()