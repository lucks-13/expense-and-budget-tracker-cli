from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation

@dataclass
class Expense:
    amount : Decimal
    category : str
    spent_on : date
    note : str = ""

def create_expense(amount_raw, category : str, data_raw : str | None = None, note : str = "") -> Expense:
    c_category = category.strip()
    if not c_category:
        raise ValueError("Category cannot be empty.")
    c_note = note.strip()
    try:
        amount = Decimal(str(amount_raw).strip())
    except (InvalidOperation, ValueError, TypeError) as ex