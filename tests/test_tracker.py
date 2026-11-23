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
        self.assertEqual(exp.spent_on, date(2026, 11, 23))
        self.assertEqual(exp.note, "Lunch")

    def test_reject_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            create_expense("-10", "Food")
        with self.assertRaises(ValueError):
            create_expense("50", " ")
        with self.assertRaises(ValueError):
            create_expense("50", "Food", "32-02-2026")

    def test_save_load_summarize(self) -> None:
        e1 = create_expense("100", "Food", "23-11-2026")
        e2 = create_expense("50", "Travel", "23-11-2026")
        e3 = create_expense("25.50", "Food", "23-11-2026")
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "test_expenses.json"
            save_expense([e1, e2, e3], file_path)
            loaded = load_expenses(file_path)
        summary = summarize_expenses(loaded)
        self.assertEqual(summary["total"], Decimal("175.50"))
        self.assertEqual(summary["by_category"]["Food"], Decimal("125.50"))
        self.assertEqual(summary["by_category"]["Travel"], Decimal("50"))

if __name__ == "__main__":
    unittest.main()