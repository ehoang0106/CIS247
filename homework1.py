#calculate price after tax
def cal_price(price, tax):
    return float(price + (price*tax)/100)
#calculate price per square footage after tax
def cal_sqft(price_taxed,sqft):
    return float(price_taxed/sqft)

def main():
    #input house 1
    print("Information of House 1")
    address1 = input("Address: ")
    sqft1 = int(input("Square footage: "))
    price1 = float(input("Price: "))
    tax_rate1 = float(input("Tax rate: "))
    #input house 2
    print("Information of House 2")
    address2 = input("Address: ")
    sqft2 = int(input("Square footage: "))
    price2 = float(input("Price: "))
    tax_rate2 = float(input("Tax rate: "))

    print("--------------------------")
    #calculate tax
    house1_taxed = cal_price(price1,tax_rate1)
    house2_taxed = cal_price(price2,tax_rate2)
    sqft1_taxed = cal_sqft(house1_taxed,sqft1)
    sqft2_taxed = cal_sqft(house2_taxed,sqft2)

    print("House 1")
    print(f"Address: {address1}")
    print(f"Price after tax: ${house1_taxed:,.2f}")
    print(f"Price per sqft after tax: ${sqft1_taxed:,.2f}/sqft")
    print(" ")
    print("House 2")
    print(f"Address: {address2}")
    print(f"Price after tax: ${house2_taxed:,.2f}")
    print(f"Price per sqft after tax: ${sqft2_taxed:,.2f}/sqft")


main()