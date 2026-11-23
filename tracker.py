import json
from pathlib import Path
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal, InvalidOperation

@dataclass
class Expense:
    amount : Decimal
    category : str
    spent_on : date
    note : str = ""

def create_expense(amount_raw, category : str, date_raw : str | None = None, note : str = "") -> Expense:
    c_category = category.strip()
    if not c_category:
        raise ValueError("Category cannot be empty.")
    c_note = note.strip()
    try:
        amount = Decimal(str(amount_raw).strip())
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError(f"Invalid amount : {amount_raw!r}") from exc
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if date_raw is None:
        spent_on = date.today()
    else:
        try:
            spent_on = datetime.strptime(str(date_raw).strip(), "%d-%m-%Y").date()
        except (ValueError, TypeError) as exc:
            raise ValueError(f"Invalid date (use DD-MM-YYYY): {date_raw!r}") from exc
    return Expense(amount = amount, category = c_category, spent_on = spent_on, note = c_note)

def save_expense(expenses : list[Expense], path : Path) -> None:
    path.parent.mkdir(parents = True, exist_ok = True)
    data = [{ "amount" : str(exp.amount), "category" : exp.category,"spent_on" : exp.spent_on.isoformat(), "note" : exp.note} for exp in expenses]
    with path.open("w", encoding = "utf-8") as f:
        json.dump(data, f, indent = 2)

def load_expenses(path : Path) -> list[Expense]:
    if not path.exists():
        return []
    try:
        with path.open("r", encoding = "utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("Expenses file must contain a list.")
        return [Expense(amount = Decimal(item["amount"]), category = item["category"], spent_on = date.fromisoformat(item["spent_on"]), note = item.get("note", "")) for item in data]
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError, InvalidOperation) as exc:
        raise ValueError(f"Could not load expenses from {path} : {exc}") from exc
    
def summarize_expenses(expenses : list[Expense]) -> dict:
    total = Decimal("0")
    by_category : dict[str, Decimal] = {}
    for exp in expenses:
        total += exp.amount
        by_category[exp.category] = by_category.get(exp.category, Decimal("0")) + exp.amount
    return {"total" : total, "by_category" : by_category}

def filter_expenses(expenses : list[Expense], category : str | None = None, month : str | None = None) -> list[Expense]:
    result = expenses
    if category is not None:
        c_category = category.strip().lower()
        if not c_category:
            raise ValueError("Category filter cannot be empty.")
        result = [exp for exp in result if exp.category.strip().lower() == c_category]
    if month is not None:
        c_month = month.strip()
        try:
            parsed_month = datetime.strptime(c_month, "%m-%Y")
        except ValueError as exc:
            raise ValueError (f"Invalid month (use MM-YYYY) : {month!r}") from exc
        target_month = parsed_month.strftime("%m-%Y")
        result = [exp for exp in result if exp.spent_on.strftime("%m-%Y") == target_month]
    return result

