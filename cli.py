import argparse
from pathlib import Path
from tracker import create_expense, load_expenses, save_expense, summarize_expenses
data_file = Path("expenses.json")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description = "Track daily expenses from the terminal.")
    subparsers = parser.add_subparsers(dest = "command", required=True)
    add_parser = subparsers.add_parser("add", help = "Add a New Expense")
    add_parser.add_argument()