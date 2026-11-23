from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation

@dataclass
class Expense:
    amount : Decimal
    category : 