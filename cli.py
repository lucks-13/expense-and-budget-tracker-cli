import argparse
from decimal import Decimal, InvalidOperation
from pathlib import Path
from tracker import create_expense, load_expenses, save_expense, summarize_expenses, filter_expenses
data_file = Path("expenses.json")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description = "Track daily expenses from the terminal.")
    subparsers = parser.add_subparsers(dest = "command", required=True)
    add_parser = subparsers.add_parser("add", help = "Add a New Expense.")
    add_parser.add_argument("--amount", required = True, help = "Expense amount (Eg. : 120 or 45.50).")
    add_parser.add_argument("--category", required = True, help = "Expense category (Eg. : Food, Travel).")
    add_parser.add_argument("--date", default = None, help = "Date in DD - MM - YYYY format.")
    add_parser.add_argument("--note", default = "", help = "Optional short note.")
    list_parser = subparsers.add_parser("list", help = "List saved expenses.")
    list_parser.add_argument("--category", default = None, help = "Filter by category (Eg. : Food, Travel).")
    list_parser.add_argument("--month", default = None, help = "Filter by month in MM - YYYY (Eg. : 11-2026).")
    summary_parser = subparsers.add_parser("summary", help = "Show total and category spending")
    summary_parser.add_argument("--category", default = None, help = "Filter by category (Eg. : Food, Travel).")
    summary_parser.add_argument("--month", default = None, help = "Filter by month in MM - YYYY (Eg. : 11-2026).")
    summary_parser.add_argument("--budget", default = None, help = "Budget limit to compare against spending (Eg. : 5000).")
    return parser

def parse_budget(budget_raw : str | None) -> Decimal | None:
    if budget_raw is None:
        return None
    try:
        budget = Decimal(str(budget_raw).strip())
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError(f"Invalid budget : {budget_raw!r}") from exc
    if budget <= 0:
        raise ValueError("Budget must be greater than zero.")
    return budget

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "add":
        expenses = load_expenses(data_file)
        try:
            new_expense = create_expense(amount_raw = args.amount, category = args.category, date_raw = args.date, note = args.note)
        except ValueError as exc:
            print(f"Error : {exc}")
            return
        expenses.append(new_expense)
        save_expense(expenses, data_file)
        print(f"Saved : {new_expense.amount} under {new_expense.category} on {new_expense.spent_on.strftime('%d-%m-%Y')}")
    elif args.command == "list":
        expenses = load_expenses(data_file)
        try:
            filtered = filter_expenses(expenses, category = args.category, month = args.month)
        except ValueError as exc:
            print(f"Error : {exc}")
            return
        if not filtered:
            print("No expenses found.")
            return 
        for exp in filtered:
            note_part = f" - {exp.note}" if exp.note else ""
            print(f"{exp.spent_on.strftime('%d-%m-%Y')} | {exp.category} | {exp.amount}{note_part}")
    elif args.command == "summary":
        expenses = load_expenses(data_file)
        try:
            filtered = filter_expenses(expenses, category = args.category, month = args.month)
            budget = parse_budget(args.budget)
        except ValueError as exc:
            print(f"Error : {exc}")
            return
        summary = summarize_expenses(filtered)
        total = summary["total"]
        print(f"Total spent : {summary['total']}")
        for category, amount in summary["by_category"].items():
            print(f" {category} : {amount}")
        if budget is not None:
            print(f"Budget : {budget}")
            if total <= budget:
                print(f"Remaining : {budget - total}")

if __name__ == "__main__":
    main()