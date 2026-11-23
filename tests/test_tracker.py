import tempfile
import unittest
from datetime import Decimal
from pathlib import Path
from tracker import create_expense, load_expenses, save_expense, summarize_expenses

class TestTracker(unittest.TestCase):
    def test_create_valid_expense(self) -> None:
        exp = create_expense("120.50", "")
