# Expense Tracker

# Background Story
I’m an international student, and when I first arrived in a new country, I quickly realized I needed a better way to track my spending. Between tuition, rent, groceries, and everyday expenses, it was difficult to keep it all organized. This project started out as a personal tool to help me understand my own financial habits.

Being new to both budgeting and Python, I combined my desire to learn software development with my need to stay on top of expenses. It was intimidating at first—especially juggling classes, part-time jobs, and managing finances in a different currency—but building this project step by step really helped me gain confidence.

# Purpose

The goal of this code is to create a straightforward expense-tracking application using Python and SQLite. I wanted it to:

1) Track Expenses: Easily add an expense with details like amount, category, date, and description.
2) Edit & Update: Quickly fix mistakes (e.g., if I mistyped an amount or date).
3) Delete Expenses: Remove entries to keep the database clean.
4) View Past Expenses: See all your spending in one place to find patterns or areas for improvement.

# How It Works

Database Connection:
* Uses a context manager (@contextmanager) to ensure every database transaction is managed and closed cleanly.
* Stores data in exptrack.db, an SQLite database.
Data Models:
* The Expense class holds the data for individual expenses.
* The DataBaseHandler class provides methods to add, edit, and remove expenses in the database.
* The ExpenseManager class handles user interaction (prompts and input).
User Interaction:
* The script runs in a simple loop to ask what the user wants to do: add, view, edit, or delete an expense.
* After the user chooses an action, the script prompts for the relevant details (expense amount, category, date, etc.).
Minimal Setup:
* All you need is Python 3.x and the sqlite3 library (built into Python) to get started.
* The code will automatically create the table if it doesn’t exist.

# Why It Helped Me

Practical Learning: Building this project taught me a lot about Python, databases, and the importance of organizing my finances.
Hands-On Budgeting: I finally have a place to store and review all my expenses—no more digging through notes or email receipts.
Confidence Booster: As a student, finishing this project boosted my confidence to tackle more complex coding tasks.
Future Ideas

Graphical Interface: Turning this command-line tool into a simple GUI or a web app.
Categorized Reports: Summaries by category or monthly breakdown to really visualize spending patterns.
Integration: Possibly link it to other student-focused apps or incorporate currency conversion if you’re dealing with multiple currencies as an international student.
