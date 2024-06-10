import sqlite3
from datetime import datetime, timedelta

# Function to add a customer to the database
def add_customer(con, cur, name, city, age):
    try:
        cur.execute("INSERT INTO customers (name, city, age) VALUES (?, ?, ?)", (name, city, age))
        con.commit()
        print("Customer added successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while adding the customer: {e}")
    
# Function to add a book to the database
def add_book(con, cur, name, author, year, type):
    try:
        cur.execute("INSERT INTO books (name, author, year, type) VALUES (?, ?, ?, ?)", (name, author, year, type))
        con.commit()
        print("Book added successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while adding the book: {e}")

# Function to display all books in the database
def display_books(cur):
    try:
        cur.execute("SELECT * FROM books")
        books = cur.fetchall()
        if not books:
            print("No books found in the database.")
            return
        for book in books:
            print(f"Name: {book[0]}, Author: {book[1]}, Year: {book[2]}, Type: {book[3]}")
    except sqlite3.Error as e:
        print(f"An error occurred while fetching the cars: {e}")

# Function to display all customers in the database
def display_customers(cur):

    try:
        cur.execute("SELECT * FROM customers")
        customers = cur.fetchall()
        if not customers:
            print("No customers found in the database.")
            return
        for customer in customers:
            print(f"Name: {customer[0]}, City: {customer[1]}, Age: {customer[2]}")
    except sqlite3.Error as e:
        print(f"An error occurred while fetching the cars: {e}")

#Function to loan a book from list of books
def loan_book(con, cur, custID, bookID):
    try:
        # Fetch the book type
        cur.execute("SELECT type FROM books WHERE id = ?", (bookID,))
        result = cur.fetchone()
        
        if result:
            book_type = result[0]
            # Determine the maximum loan duration based on the book type
            if book_type == 1:
                max_loan_days = 10
            elif book_type == 2:
                max_loan_days = 5
            elif book_type == 3:
                max_loan_days = 2
            else:
                print("Invalid book type.")
                return
            
            # Calculate the loan date and return date
            loan_date_obj = datetime.today()
            return_date_obj = loan_date_obj + timedelta(days=max_loan_days)
            loanDate = loan_date_obj.strftime("%Y-%m-%d")
            returnDate = return_date_obj.strftime("%Y-%m-%d")
            
            # Check if both the customer and book exist using a JOIN
            cur.execute("""
                SELECT customers.id, books.id 
                FROM customers 
                JOIN books ON customers.id = ? AND books.id = ?
            """, (custID, bookID))
            
            result = cur.fetchone()
            
            if result:
                # If both exist, insert the loan record
                cur.execute("INSERT INTO loans (custID, bookID, loanDate, returnDate) VALUES (?, ?, ?, ?)", 
                            (custID, bookID, loanDate, returnDate))
                con.commit()
                print("Book loaned successfully.")
            else:
                print("Either the customer or the book does not exist.")
        else:
            print("Book not found.")
    except sqlite3.Error as e:
        print(f"An error occurred while loaning the book: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to return a book using only bookID
def return_book(con, cur, bookID):
    try:
        # Verify the loan exists
        cur.execute("SELECT * FROM loans WHERE bookID = ?", (bookID,))
        result = cur.fetchone()
        
        if result:
            # If the loan exists, delete the loan record
            cur.execute("DELETE FROM loans WHERE bookID = ?", (bookID,))
            con.commit()
            print("Book returned successfully.")
        else:
            print("No such loan found.")
    except sqlite3.Error as e:
        print(f"An error occurred while returning the book: {e}")

# Function to display all loans in the database
def display_all_loans(cur):
    try:
        # Fetch all loans
        cur.execute("""
            SELECT loans.custID, loans.bookID, loans.loanDate, loans.returnDate, customers.name, books.name
            FROM loans
            JOIN customers ON loans.custID = customers.id
            JOIN books ON loans.bookID = books.id
        """)
        loans = cur.fetchall()
        if not loans:
            print("No loans found in the database.")
            return
        for loan in loans:
            print(f"Customer ID: {loan[0]}, Customer Name: {loan[4]}, Book ID: {loan[1]}, Book Name: {loan[5]}, Loan Date: {loan[2]}, Return Date: {loan[3]}")
    except sqlite3.Error as e:
        print(f"An error occurred while fetching the loans: {e}")

# Function to display all late loans in the database
def display_late_loans(cur):
    try:
        today = datetime.today().strftime("%Y-%m-%d")
        # Fetch all loans
        cur.execute("""
            SELECT loans.custID, loans.bookID, loans.loanDate, loans.returnDate, customers.name, books.name
            FROM loans
            JOIN customers ON loans.custID = customers.id
            JOIN books ON loans.bookID = books.id
            WHERE loans.returnDate < ?
        """, (today,))
        loans = cur.fetchall()
        if not loans:
            print("No late loans found in the database.")
            return
        for loan in loans:
            print(f"Customer ID: {loan[0]}, Customer Name: {loan[4]}, Book ID: {loan[1]}, Book Name: {loan[5]}, Loan Date: {loan[2]}, Return Date: {loan[3]}")
    except sqlite3.Error as e:
        print(f"An error occurred while fetching the loans: {e}")

#Function to find book by name
def find_book_by_name(cur, book_name):
    try:
        # Fetch books matching the name
        cur.execute("SELECT * FROM books WHERE name LIKE ?", ('%' + book_name + '%',))
        books = cur.fetchall()
        if not books:
            print(f"No books found with the name: {book_name}")
            return
        for book in books:
            print(f"ID: {book[0]}, Name: {book[1]}, Author: {book[2]}, Year: {book[3]}, Type: {book[4]}")
    except sqlite3.Error as e:
        print(f"An error occurred while fetching the books: {e}")

#Function to find customer by name
def find_customer_by_name(cur, customer_name):
    try:
        # Fetch customers matching the name
        cur.execute("SELECT * FROM customers WHERE name LIKE ?", ('%' + customer_name + '%',))
        customers = cur.fetchall()
        if not customers:
            print(f"No customers found with the name: {customer_name}")
            return
        for customer in customers:
            print(f"ID: {customer[0]}, Name: {customer[1]}, City: {customer[2]}, Age: {customer[3]}")
    except sqlite3.Error as e:
        print(f"An error occurred while fetching the customers: {e}")

#Function to remove book from the database
def remove_book(con, cur, bookID):
    try:
        cur.execute("DELETE FROM books WHERE id = ?", (bookID,))
        con.commit()
        if cur.rowcount > 0:
            print(f"Book with ID {bookID} removed successfully.")
        else:
            print(f"No book found with ID {bookID}.")
    except sqlite3.Error as e:
        print(f"An error occurred while removing the book: {e}")

#Function to remove customer from the database
def remove_customer(con, cur, customerID):
    try:
        cur.execute("DELETE FROM customers WHERE id = ?", (customerID,))
        con.commit()
        if cur.rowcount > 0:
            print(f"Customer with ID {customerID} removed successfully.")
        else:
            print(f"No customer found with ID {customerID}.")
    except sqlite3.Error as e:
        print(f"An error occurred while removing the customer: {e}")
