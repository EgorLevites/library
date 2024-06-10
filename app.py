import sqlite3
from functions import *
from datetime import datetime
from enum import Enum, auto


# Enum class for menu options
class MenuOptions(Enum):

    ADD_CUSTOMER = auto()
    ADD_BOOK = auto() 
    LOAN_BOOK = auto() 
    RETURN_BOOK = auto() 
    DISPLAY_ALL_BOOKS = auto() 
    DISPLAY_ALL_CUSTOMERS = auto() 
    DISPLAY_ALL_LOANS = auto() 
    DISPLAY_LATE_LOANS = auto()
    FIND_BOOK_BY_NAME = auto() 
    FIND_CUSTOMERS_BY_NAME = auto() 
    REMOVE_BOOK = auto()
    REMOVE_CUSTOMERS = auto()
    EXIT = auto()


# Connect to the database (creates a new one if it doesn't exist)
con = sqlite3.connect("library.db")
# Create a cursor object
cur = con.cursor()

try:
    # Create the books table if it doesn't exist
    cur.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                author TEXT,
                year INTEGER,
                type INTEGER
            )
        """)
    # Create the customers table if it doesn't exist
    cur.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                city TEXT,
                age INTEGER
            )
        """)
    # Create the loans table if it doesn't exist
    cur.execute("""
            CREATE TABLE IF NOT EXISTS loans (
                custID INTEGER,
                bookID INTEGER,
                loanDate DATE,
                returnDate DATE
            )
        """)
    con.commit()
except sqlite3.Error as e:
     print(f"An error occurred while creating the table: {e}")


#Menu
while True:
    print("\nMenu:")
    for option in MenuOptions:
        print(f"{option.value}. {option.name.replace('_', ' ').title()}")
    
    try:
        choice = int(input("Enter your choice: "))
        selected_option = MenuOptions(choice)
    except ValueError:
        print("Invalid choice. Please enter a numeric value.")
        continue
    except KeyError:
        print("Invalid choice. Please select a valid menu option.")
        continue
    if selected_option == MenuOptions.ADD_CUSTOMER:
        name = input("Enter customer name: ")
        city = input("Enter customer city: ")
        age = int(input("Enter customer age: "))
        add_customer(con, cur, name, city, age)
    elif selected_option == MenuOptions.ADD_BOOK:
        name = input("Enter book name: ")
        author = input("Enter book author: ")
        year = int(input("Enter book year: "))
        type = int(input("Enter book type 1/2/3: "))
        add_book(con, cur, name, author, year, type)
    elif selected_option == MenuOptions.DISPLAY_ALL_BOOKS:
        display_books(cur)
    elif selected_option == MenuOptions.DISPLAY_ALL_CUSTOMERS:
        display_customers(cur)
    elif selected_option == MenuOptions.DISPLAY_ALL_LOANS:
        display_all_loans(cur)
    elif selected_option == MenuOptions.LOAN_BOOK:
        custID = int(input("Enter Customer ID: "))
        bookID = int(input("Enter Book ID: "))
        loan_book(con, cur, custID, bookID)
    elif selected_option == MenuOptions.RETURN_BOOK:
        bookID = int(input("Enter Book ID: "))
        return_book(con, cur, bookID)
    elif selected_option == MenuOptions.EXIT:
        print("Exiting...")
        break
    elif selected_option == MenuOptions.DISPLAY_LATE_LOANS:
        display_late_loans(cur)
    elif selected_option == MenuOptions.FIND_BOOK_BY_NAME:
        book_name = input("Enter Book Name: ")
        find_book_by_name(cur, book_name)
    elif selected_option == MenuOptions.FIND_CUSTOMERS_BY_NAME:
        customer_name = input("Enter Customer Name: ")
        find_customer_by_name(cur, customer_name)
    elif selected_option == MenuOptions.REMOVE_BOOK:
        bookID = int(input("Enter Book ID to remove: "))
        remove_book(con, cur, bookID)
    elif selected_option == MenuOptions.REMOVE_CUSTOMERS:
        customerID = int(input("Enter Customer ID to remove: "))
        remove_customer(con, cur, customerID)
    else:
        print("Invalid choice. Please try again.")

# Close the connection
con.close()

