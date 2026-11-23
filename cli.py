import argparse
from pathlib import Path
from tracker import create_expense, load_expenses, save_expense, summarize_expenses
data_file = Path("expenses.json")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description = "Track daily expenses from the terminal.")
    subparsers = parser.add_subparsers(dest = "command", required=True)
    add_parser = subparsers.add_parser("add", help = "Add a New Expense.")
    add_parser.add_argument("--amount", required = True, help = "Expense amount (Eg. : 120 or 45.50).")
    add_parser.add_argument("--category", required = True, help = "Expense category (Eg. : Food, Travel).")
    add_parser.add_argument("--date", default = None, help = "Date in DD - MM - YYYY format.")
    add_parser.add_argument("--note", default = "", help = "Op")