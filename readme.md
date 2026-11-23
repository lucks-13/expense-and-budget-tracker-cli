# Expense and Budget Tracker Cli
Hello everyone! This project is just a trail to the bigger project actually i planned of building this as a bigger project but the application must be either mobile or web application so that its easier to be used across all the device

# My Upcoming project.

so its a single app to handle all the person finance,
like portfolio management, emi alerts etc. like entire flow in one page to handle someones personal finance
stay tuned for more update.

# Concept



# How to Run it.

```
git clone https://github.com/lucks-13/expense-and-budget-tracker-cli.git
cd expense-and-budget-tracker-cli
```

# Available Commands.

1. Add an expense { default date = today }:

```
python cli.py add --amount 250 --category Food --note "Lunch"
```

if custom date then

```
python cli.py add --amount 120.50 --category Travel --date 23-11-2026 --note "Bus"
```

2. To list saved expenses

```
python cli.py list
```

filter by category

```
python cli.py list --category Food
```

3. View spending summary and budget status:

```
python cli.py summary --month 11-2026 --budget 5000
```

# what I learned.

* fundamentals of finance
* modelling data using @dataclass and handling money using Decimal instead of using float.
* parsing and formatting dates

# 
