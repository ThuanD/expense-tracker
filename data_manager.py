import json
import os


class DataManager:
    def __init__(self, data_file="expenses.json"):
        self.data_file = data_file
        self._ensure_data_file()

    def _ensure_data_file(self):
        """Create the data file if it doesn't exist"""
        if not os.path.exists(self.data_file):
            with open(self.data_file, "w") as f:
                json.dump([], f)

    def _read_data(self):
        """Read expenses from the data file"""
        with open(self.data_file, "r") as f:
            return json.load(f)

    def _write_data(self, data):
        """Write expenses to the data file"""
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def get_next_id(self):
        """Generate the next unique expense ID"""
        expenses = self._read_data()
        return max([expense["id"] for expense in expenses], default=0) + 1

    def add_expense(self, expense):
        """Add a new expense to the data file"""
        expenses = self._read_data()
        expenses.append(expense)
        self._write_data(expenses)

    def get_expenses(self):
        """Retrieve all expenses"""
        return self._read_data()

    def delete_expense(self, expense_id):
        """Delete an expense by its ID"""
        expenses = self._read_data()
        initial_length = len(expenses)
        expenses = [expense for expense in expenses if expense["id"] != expense_id]

        if len(expenses) < initial_length:
            self._write_data(expenses)
            return True
        return False

    def update_expense(self, expense_id, update_data):
        """Update an existing expense"""
        expenses = self._read_data()
        for expense in expenses:
            if expense["id"] == expense_id:
                expense.update(update_data)
                self._write_data(expenses)
                return True
        return False
