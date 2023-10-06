

def load_data():
    books = {}
    
    with open("books.txt") as file:
        for line in file:
            book_name, copies = line.split()
            copies = copies.strip()
            books[book_name] = copies
    

    return books


def add_book(books):

    title = input("Enter title: ")
    copies = int(input("Enter copies: "))

    if title not in books:
        books[title] = copies
    else:
        books[title] += copies
    print(f"{title} has been added to library")
    return books

    
def find_book(books):
    
    title = input("Enter tile: ")
    
    if title in books:
        print(f"{title} is in-stock with {books[title]} copies")
    else:
        print("There is no copies in-stock")

def remove_book(books):
    
    title = input("Enter title of book you want to remove: ")
    if title not in books:
        print("There is no book in-stock to remove")
    else:
        
        if books[title] == 0 or title not in books:
            
            print("There is no copies left. Cannot remove the book")
        else:
            books[title] = int(books[title])
            books[title] -= 1
            print(f"Remove 1 copies of {title} book")
        
    
    return books

def quit(books):
    
    with open("books.txt", 'a') as file:
        for title, copies in books.items():
            file.write(f"{title} {copies}\n")

def main():
    try:
        with open("books.txt", 'a') as file:
            books = load_data()
            while True:
                

                choose = int(input("(1) to add book | (2) to remove book (3) to find book (4) to quit: "))
                if choose == 1:
                    add_book(books)
                elif choose == 2:
                    remove_book(books)
                elif choose == 3:
                    find_book(books)
                else:
                    quit(books)
                    break
    except:
        print("Error")
       
   
            
    


main()