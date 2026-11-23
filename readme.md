# Expense and Budget Tracker Cli
Hello everyone! This project is just a trail to the bigger project actually i planned of building this as a bigger project but the application must be either mobile or web application so that its easier to be used across all the device

# My Upcoming project.

so its a single app to handle all the person finance,
like portfolio management, emi alerts etc. like entire flow in one page to handle someones personal finance
stay tuned for more update.

# Concept

my idea for my upcoming project is a remainder app which remeinds me at particular where i set remainder lets say credit card bill payment on 25th of every month, my project has a keep note + calender + alarm app, it also has total revenue and total expense tracker + portfolio management which tells me how much percentage and on what like either in stocks or in bonds or in gold so basically its a end to end to manage remaind etc.

the backend and the authentication will be handled by firebase or supabase.

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

# Ai Disclosure
I used google gemini ai mode in chrome for learining and debugging the code.
