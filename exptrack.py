import sqlite3
from contextlib import contextmanager

@contextmanager
def db_connection(db_file):
    # Open the database connection
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    
    try:
        # Yield the connection and cursor to the calling code
        yield cursor
    except Exception as e:
        # Handle exceptions (if any)
        print(f"An error occurred: {e}")
        raise
    finally:
        # Ensure the connection is always closed
        connection.commit()  # Commit any changes to the database
        connection.close()   # Close the connection
        print("Database connection closed.")
        
class DataBaseHandler:
    def createTable(self):
        with db_connection("exptrack.db") as cursor:
            command1 = """CREATE TABLE IF NOT EXISTS
            Expenses(ID INTEGER PRIMARY KEY AUTOINCREMENT, AMOUNT FLOAT, CATEGORY TEXT, DATE TEXT, DESCRIPTION TEXT)"""
            cursor.execute(command1)
        return
    
    def add(self, expense):
        with db_connection("exptrack.db") as cursor:
            cursor.execute("INSERT INTO Expenses (AMOUNT, CATEGORY, DATE, DESCRIPTION) VALUES (?, ?, ?, ?)", (expense.amount, expense.category, expense.date, expense.description))
        return "Expense added successfully."

    def edit_desc(self, new, ID):
        with db_connection("exptrack.db") as cursor:
            cursor.execute("UPDATE Expenses SET DESCRIPTION = (?) WHERE ID = (?)", (new,), (ID,))
        return "Description edited successfully."
        
    def edit_amount(self, new, ID):
        with db_connection("exptrack.db") as cursor:
            cursor.execute("UPDATE Expenses SET AMOUNT = (?) WHERE ID = (?)", (new,), (ID,))
        return "Amount edited successfully."
    
    def edit_category(self, new, ID):
        with db_connection("exptrack.db") as cursor:
            cursor.execute("UPDATE Expenses SET CATEGORY = (?) WHERE ID = (?)", (new,), (ID,))
        return "Category edited successfully."

    def edit_date(self, new, ID):
        with db_connection("exptrack.db") as cursor:
            cursor.execute("UPDATE Expenses SET DATE = (?) WHERE ID = (?)", (new,), (ID,))
        return "Date edited successfully."

    def delete_expense(self, index):
        with db_connection("exptrack.db") as cursor:
            cursor.execute("DELETE FROM Expenses WHERE ID = (?)",(index,))
        return "Expense deleted successfully."

    def view_expenses(self):
        with db_connection("exptrack.db") as cursor:
            cursor.execute("SELECT * FROM Expenses")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

class Expense:
    def __init__(self, amount: float, category: str, date: str, description: str):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __str__(self):
        return f"Amount: ${self.amount}, Category: {self.category}, Date: {self.date}, Description: {self.description}\n"
    
    def edit_desc(self, new, user_input, DB):
        self.description = new
        DB.edit_desc(new, user_input)

    def edit_amount(self, new, user_input, DB):
        self.amount = new
        DB.edit_amount(new, user_input)
        
    def edit_category(self, new, user_input, DB):
        self.category = new
        DB.edit_category(new, user_input)

    def edit_date(self, new, user_input, DB):
        self.date = new
        DB.edit_date(new, user_input)

class ExpenseManager:
    def __init__(self, database):
        self.database = database
            
    def add_expense(self):
        amount = int(input("Please enter expense amount:"))
        category = input("Please enter expense category:")
        date = input("Please enter date DD/MM/YYYY:")
        description = input("Please describe the expense:")
        new_expense = Expense(amount,category,date,description)
        self.database.add(new_expense)

    def delete_expense(self,index):
        self.database.delete_expense(index)
    
    def edit_expense(self):
        user_input1 = input("Which expense would you like to edit? Enter the ID")
        user_input2 = input("What would you like to edit? a for amount, da for date, c for category, de for description")
        if user_input2 == 'a':
            new = float(input("Enter new amount"))
            self.database.edit_amount(new, user_input1)
        elif user_input2 == 'da':
            new = input("Enter new date: ")
            self.database.edit_date(new, user_input1)
        elif user_input2 == 'c':
            new = input("Enter new category")
            self.database.edit_category(new, user_input1)
        elif user_input2 == 'de':
            new = input("Enter new description:")
            self.database.edit_description(new, user_input1)
        else:
            print("Invalid input.")
        return

DBH = DataBaseHandler()
EM = ExpenseManager(DBH)
DBH.createTable()

while True:
    choice = input("Hi! How can I help you today? a to add expense, v to view, e to edit, d to delete or q to quit?")
    if (choice == 'a'):
        EM.add_expense()

    elif (choice == 'v'):
        DBH.view_expenses()
    
    elif (choice == 'e'):
        EM.edit_expense()

    elif (choice == 'd'):
        index = int(input("Enter the ID of the expense you want to delete:"))
        EM.delete_expense(index)

    elif (choice == 'q'):
        break

    else:
        print("Invalid input")
        break
