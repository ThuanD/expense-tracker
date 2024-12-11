import argparse
from datetime import datetime
from data_manager import DataManager


class ExpenseTracker:
    def __init__(self, data_file="expenses.json"):
        self.data_manager = DataManager(data_file)

    def add_expense(self, description, amount, category=None):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be a positive number")

            expense = {
                "id": self.data_manager.get_next_id(),
                "date": datetime.now().strftime("%Y-%m-%d"),
                "description": description,
                "amount": amount,
                "category": category,
            }

            self.data_manager.add_expense(expense)
            print(f"Expense added successfully (ID: {expense['id']})")
        except ValueError as e:
            print(f"Error: {e}")

    def list_expenses(self):
        expenses = self.data_manager.get_expenses()
        if not expenses:
            print("No expenses found.")
            return

        print("ID  Date       Description  Amount  Category")
        for expense in expenses:
            print(
                f"{expense['id']:<4} {expense['date']}  {expense['description']:<12} ${expense['amount']:<6} {expense.get('category', 'N/A')}"
            )

    def delete_expense(self, expense_id):
        try:
            expense_id = int(expense_id)
            if self.data_manager.delete_expense(expense_id):
                print("Expense deleted successfully")
            else:
                print(f"No expense found with ID {expense_id}")
        except ValueError:
            print("Invalid expense ID")

    def update_expense(self, expense_id, description=None, amount=None, category=None):
        try:
            expense_id = int(expense_id)
            update_data = {}
            if description is not None:
                update_data["description"] = description
            if amount is not None:
                amount = float(amount)
                if amount <= 0:
                    raise ValueError("Amount must be a positive number")
                update_data["amount"] = amount
            if category is not None:
                update_data["category"] = category

            if self.data_manager.update_expense(expense_id, update_data):
                print("Expense updated successfully")
            else:
                print(f"No expense found with ID {expense_id}")
        except ValueError as e:
            print(f"Error: {e}")

    def get_summary(self, month=None):
        expenses = self.data_manager.get_expenses()

        if month:
            try:
                month = int(month)
                expenses = [
                    expense
                    for expense in expenses
                    if datetime.strptime(expense["date"], "%Y-%m-%d").month == month
                ]
            except ValueError:
                print("Invalid month. Please use a number between 1-12.")
                return

        total_expenses = sum(expense["amount"] for expense in expenses)

        if month:
            print(f"Total expenses for month {month}: ${total_expenses:.2f}")
        else:
            print(f"Total expenses: ${total_expenses:.2f}")

    def export_to_csv(self, filename="expenses.csv"):
        import csv

        expenses = self.data_manager.get_expenses()

        with open(filename, "w", newline="") as csvfile:
            fieldnames = ["ID", "Date", "Description", "Amount", "Category"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for expense in expenses:
                writer.writerow(
                    {
                        "ID": expense["id"],
                        "Date": expense["date"],
                        "Description": expense["description"],
                        "Amount": expense["amount"],
                        "Category": expense.get("category", ""),
                    }
                )
        print(f"Expenses exported to {filename}")


def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    parser.add_argument(
        "command", choices=["add", "list", "delete", "update", "summary", "export"]
    )

    # Add arguments for each command
    parser.add_argument("--id", type=int, help="Expense ID for delete/update")
    parser.add_argument("--description", help="Expense description")
    parser.add_argument("--amount", type=float, help="Expense amount")
    parser.add_argument("--category", help="Expense category")
    parser.add_argument("--month", type=int, help="Month for summary (1-12)")
    parser.add_argument("--file", help="Export filename")

    args = parser.parse_args()
    tracker = ExpenseTracker()

    if args.command == "add":
        if not args.description or args.amount is None:
            print("Error: Description and amount are required for adding an expense")
            return
        tracker.add_expense(args.description, args.amount, args.category)

    elif args.command == "list":
        tracker.list_expenses()

    elif args.command == "delete":
        if not args.id:
            print("Error: Expense ID is required for deletion")
            return
        tracker.delete_expense(args.id)

    elif args.command == "update":
        if not args.id:
            print("Error: Expense ID is required for update")
            return
        tracker.update_expense(args.id, args.description, args.amount, args.category)

    elif args.command == "summary":
        tracker.get_summary(args.month)

    elif args.command == "export":
        tracker.export_to_csv(args.file or "expenses.csv")


if __name__ == "__main__":
    main()
