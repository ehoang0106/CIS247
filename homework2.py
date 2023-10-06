import random


def determine_member(member):
    if member == 1:
        return 1 #free member return 1
    elif member == 2:
        return 2 #paid member reuturn 2
    else:
        return 0 #non member return 0

def cal_tax(taxed):
    tax = 9.25
    taxed = ((taxed*tax)/100)
    return taxed
    
def cal_point(purchased, member):
    point = 0
    if purchased == 1:
        point += 5
    elif purchased == 2:
        point += 15
    elif purchased == 3:
        if member == 1: 
            point += 30
        elif member == 2:
            point += 50
        else:
            point += 0
    elif purchased >=4:
        if member == 1:
            point += 60 
        elif member == 2:
            point += 100
        else:
            point += 0
    return point

def enter_new_customer():
    book_purchased = int(input("\nHow many books the customer is buying: "))
    subtotal = float(input("Subtotal cost of the books before tax: "))
    member = int(input("Enter (0) for Non-member | (1) for Free-member | (2) for Paid-member: "))
    
    #calculate tax
    taxed = cal_tax(subtotal)

    #calculate subtotal after taxed
    subtotal_taxed = subtotal + taxed

    #if customer is a paid member remove 10% of the subtotal to the final cost
    if member == 2:
        final_cost = subtotal_taxed - ((subtotal_taxed*10)/100)
    else:
    #if customer is not a paid member
        final_cost = subtotal + taxed
       
    #calculate money saved
    final_cost_non_mem = subtotal + taxed
    money_saved = final_cost_non_mem - final_cost
    #calculate point
    cal_ptn = cal_point(book_purchased, member)

    return book_purchased, subtotal, taxed, final_cost, money_saved, cal_ptn




def main():
    grant_total = 0
    quit = False
    while not quit:
        print("\nChoose 1 to enter a new customer sale")
        print("Choose 2 to see how much money the store has made today")
        print("Choose 3 to QUIT the program")
        choose = int((input("Choose option: ")))
        if choose == 1:
            book_purchased,subtotal,taxed,final_cost,money_saved,cal_pnt = enter_new_customer()
            
            print(f"\nNumber of books was bought: {book_purchased}")
            print(f"Subtotal: ${subtotal:,.2f}")
            print(f"Tax amount: ${taxed:,.2f}")
            print(f"Final cost: ${final_cost:,.2f}")
            #if customer is paid member print out amount saved, if not do not print
            if money_saved != 0.0:
                print(f"Amount saved: ${money_saved:,.2f}")
            print(f"Points received: {cal_pnt} points")

            #calculate grand total cost
            grant_total += final_cost
            
        elif choose == 2:
            print(f"\nMoney the store has made: ${grant_total:,.2f}")
        elif choose == 3:
            quit = True
            print(f"\nMoney the store has made: ${grant_total:,.2f}")
            print("Thank you for using the program. Have a nice day!")



main()
        
    






