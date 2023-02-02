from django.test import TestCase
from .models import ExpenseTracker
import datetime


class ExpenseTrackerTestCase(TestCase):
    def setUp(self):
        ExpenseTracker.objects.create(
            date=datetime.date.today(), location="location1", amount=10.0
        )
        ExpenseTracker.objects.create(
            date=datetime.date.today(), location="location2", amount=20.0
        )

    def test_update_expense(self):
        expense = ExpenseTracker.objects.get(location="location1")
        expense.update_expense(location="location1_updated")
        expense.refresh_from_db()
        self.assertEqual(expense.location, "location1_updated")

    def test_delete_expense(self):
        expense = ExpenseTracker.objects.get(location="location1")
        expense.delete_expense()
        self.assertFalse(ExpenseTracker.objects.filter(location="location1").exists())

    def test_filter_expenses(self):
        expenses = ExpenseTracker.filter_expenses(location="location1")
        self.assertEqual(expenses.count(), 1)
        self.assertEqual(expenses.first().location, "location1")

    def test_report(self):
        report = ExpenseTracker.report()
        self.assertEqual(report.count(), 2)

    def test_amount_as_currency_string(self):
        expense = ExpenseTracker.objects.get(location="location1")
        self.assertEqual(expense.amount_as_currency_string(), "$10.00")
