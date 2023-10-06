def main():
    lst = []

    for i in range(5):
        sale_input = int(input(f"Enter today's sale for store {i+1}: "))
        lst.append(sale_input)

    print("\nSALE BAR CHAR (EACH * $100)\n")

    for index, value in enumerate(lst):
        str = ""
        asterisk = int(value/100)
        for i in range(asterisk):
            str += "*"       
        print(f"Store {index + 1}: {str}")
main()
        



