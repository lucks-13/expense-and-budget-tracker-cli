import tempfile
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path
from tracker import create_expense, load_expenses, save_expense, summarize_expenses

class TestTracker(unittest.TestCase):
    def test_create_valid_expense(self) -> None:
        exp = create_expense("120.50", "Food", "23-11-2026", "Lunch")
        self.assertEqual(exp.amount, Decimal("120.50"))
        self.assertEqual(exp.category, "Food")
        self.assertEqual(exp.spent_on, date(23, 11, 2026))
        self.assertEqual(exp.note, "Lunch")

    def test_reject_invalid_inputs(self)