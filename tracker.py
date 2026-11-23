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
        raise ValueError("Amount must be grater than zero.")
    if date_raw is None:
        spent_on = date.today()
    else:
        try:
            spent_on = datetime.strftime(str(date_raw).strip(), "%d-%m-%y").date()
        except (ValueError, TypeError) as exc:
            raise ValueError(f"Invalid date ( use DD - MM - YYYY ) : {date_raw!r}") from exc
    return Expense(amount = amount, category = c_category, spent_on = spent_on, note = c_note)