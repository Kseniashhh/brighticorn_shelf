# print title
# show menu
# ask for command
# show command
# prompt function based on command

def add(item):
    book_shelf.append(book)
    return book_shelf

def view(lst):
    for item in lst:
        print ("- " + item)


def check(lst, item):
    if book in lst:
        print ("This book is on the shelf already \n")
    else:
        question = input("This book is not on the shelf, do you want to add it? Y/N  ").title()
        if question == "Y":
            add(book)
            return lst
        else:
            return lst


def print_menu():
    print (menu)
#exit


menu = """  Menu:

            - (A)dd a Book
            - (V)iew my Books
            - (C)heck if Brighticorn has it
            - (E)xit

            """



print("Brighticorn's Books")
print("-------------------")
book_shelf=[]

while True:
    print_menu()
    command = input("Please select an action:  ").capitalize()
    if command == "A":
        print("You chose to add a new book")
        book = input("What book do you want to add? \n").capitalize()
        add(book)
    elif command == "V":
        print("You chose to view your bookshelf")
        view(book_shelf)
    elif command == "C":
        print("You chose to check to see if you already have this book")
        book = input("What book do you want to see if you have? \n").capitalize()
        check(book_shelf, book)
    elif command == "E":
        print("Goodbye!")
        exit()
    else:
        print ("Sorry, not an option, please try again")
        continue