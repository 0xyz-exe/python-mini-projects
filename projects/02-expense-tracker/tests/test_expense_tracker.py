"""Tests for expense tracker."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from expense_tracker import ExpenseTracker, Transaction


def test_add_income():
    with TemporaryDirectory() as tmpdir:
        et = ExpenseTracker(Path(tmpdir) / "exp.json")
        txn = et.add("income", 1000.0, "Salary", "Monthly salary")
        assert txn.type == "income"
        assert txn.amount == 1000.0


def test_add_expense():
    with TemporaryDirectory() as tmpdir:
        et = ExpenseTracker(Path(tmpdir) / "exp.json")
        txn = et.add("expense", 50.0, "Food", "Lunch")
        assert txn.type == "expense"


def test_invalid_amount():
    with TemporaryDirectory() as tmpdir:
        et = ExpenseTracker(Path(tmpdir) / "exp.json")
        try:
            et.add("expense", -10.0, "Food")
            assert False
        except ValueError as e:
            assert "positive" in str(e).lower()


def test_monthly_summary():
    with TemporaryDirectory() as tmpdir:
        et = ExpenseTracker(Path(tmpdir) / "exp.json")
        et.add("income", 1000.0, "Salary", date="2026-10-15")
        et.add("expense", 200.0, "Food", date="2026-10-16")
        et.add("expense", 50.0, "Transport", date="2026-09-10")
        
        summary = et.monthly_summary(2026, 10)
        assert summary["income"] == 1000.0
        assert summary["expense"] == 200.0
        assert summary["balance"] == 800.0
        assert summary["count"] == 2


def test_category_summary():
    with TemporaryDirectory() as tmpdir:
        et = ExpenseTracker(Path(tmpdir) / "exp.json")
        et.add("expense", 100.0, "Food")
        et.add("expense", 50.0, "Food")
        et.add("income", 1000.0, "Salary")
        
        cats = et.category_summary()
        assert cats["expense:Food"] == 150.0
        assert cats["income:Salary"] == 1000.0


def test_csv_export_import():
    with TemporaryDirectory() as tmpdir:
        storage1 = Path(tmpdir) / "exp1.json"
        storage2 = Path(tmpdir) / "exp2.json"
        csv_path = Path(tmpdir) / "export.csv"
        
        et1 = ExpenseTracker(storage1)
        et1.add("income", 500.0, "Freelance")
        et1.export_csv(csv_path)
        
        et2 = ExpenseTracker(storage2)
        et2.import_csv(csv_path)
        assert len(et2.transactions) == 1
        assert et2.transactions[0].category == "Freelance"


if __name__ == "__main__":
    test_add_income()
    test_add_expense()
    test_invalid_amount()
    test_monthly_summary()
    test_category_summary()
    test_csv_export_import()
    print("✓ All tests passed")
