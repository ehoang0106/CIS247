


def get_sales(div):
    sales = input(f"How many sales for {div}: ")
    return float(sales)

def find_highest(sale_list):
    highest = 0
    div_highest = 0

    for index, sale in enumerate(sale_list):
        if sale > highest:
            highest = sale
            div_highest = index + 1
    print(f"Largest sale is {highest} from division {div_highest}")

def main():
    lst = []
    div = int(input("How many division: "))
    for i in range(1, div + 1):
        val = get_sales(i)
        lst.append(val)
    find_highest(lst)

main()