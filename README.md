
# Library Management System

This is a simple library management system implemented in Python using SQLite. The system allows users to manage books, customers, and loans through a command-line interface.

## Features

- **Add Customer**: Add new customers to the database.
- **Add Book**: Add new books to the database.
- **Loan Book**: Loan books to customers.
- **Return Book**: Return loaned books.
- **Display All Books**: Display all books in the library.
- **Display All Customers**: Display all customers.
- **Display All Loans**: Display all active loans.
- **Display Late Loans**: Display all loans that are overdue.
- **Find Book by Name**: Search for books by name.
- **Find Customers by Name**: Search for customers by name.
- **Remove Book**: Remove books from the database.
- **Remove Customers**: Remove customers from the database.
- **Exit**: Exit the application.

## Getting Started

### Prerequisites

- Python 3.x
- SQLite3

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/library-management-system.git
    cd library-management-system
    ```

2. Install required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:
    ```sh
    python app.py
    ```

### Usage

The application provides a menu-driven interface. Upon running the application, you will see a menu with various options. Enter the corresponding number to perform the desired action.

### Code Structure

- `app.py`: The main application file. Contains the menu, database initialization, and user interaction.
- `functions.py`: Contains helper functions to manage books, customers, and loans.

### Example

```
Menu:
1. Add Customer
2. Add Book
3. Loan Book
4. Return Book
5. Display All Books
6. Display All Customers
7. Display All Loans
8. Display Late Loans
9. Find Book By Name
10. Find Customers By Name
11. Remove Book
12. Remove Customers
13. Exit

Enter your choice: 1
```

### Database Schema

- `books` table:
    - `id`: INTEGER PRIMARY KEY AUTOINCREMENT
    - `name`: TEXT
    - `author`: TEXT
    - `year`: INTEGER
    - `type`: INTEGER

- `customers` table:
    - `id`: INTEGER PRIMARY KEY AUTOINCREMENT
    - `name`: TEXT
    - `city`: TEXT
    - `age`: INTEGER

- `loans` table:
    - `custID`: INTEGER
    - `bookID`: INTEGER
    - `loanDate`: DATE
    - `returnDate`: DATE

### Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any feature additions or bug fixes.

### License

This project is licensed under the MIT License.

