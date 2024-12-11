# Expense Tracker CLI

A simple, command-line expense tracking application built with Python.

_Note: This project is part of the Roadmap Projects: https://roadmap.sh/projects/expense-tracker_


## Features

- Add expenses with description, amount, and optional category
- List all expenses
- Delete and update expenses
- Generate expense summaries by month
- Export expenses to CSV file

## Prerequisites

- Python 3.7+
- No external libraries required (uses standard library)

## Installation

1. Clone the repository
2. Ensure you have Python 3.7+ installed
3. Run the application using Python

## Usage Examples

### Add an Expense
```bash
python expense_tracker.py add --description "Lunch" --amount 20
```

### List Expenses
```bash
python expense_tracker.py list
```

### Deleting an Expense
```bash
python expense_tracker.py delete --id 1
```

### Updating an Expense
```bash
python expense_tracker.py update --id 1 --description "Breakfast" --amount 15
```

### View Summary
```bash
python expense_tracker.py summary
python expense_tracker.py summary --month 8
```

### Export Expenses to CSV
```bash
python expense_tracker.py export --file expenses.csv
```

## Commands

- `add`: Add a new expense
- `list`: List all expenses
- `delete`: Delete an expense by ID
- `update`: Update an existing expense
- `summary`: View total expenses
- `export`: Export expenses to CSV

## License

This project is open-source.

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact & Support

Found an issue? Please open a GitHub issue with detailed information.

Project Link: [https://github.com/ThuanD/expense-tracker](https://github.com/ThuanD/expense-tracker)
