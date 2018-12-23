from datetime import datetime, timezone
from django.test import TestCase
from django.urls import reverse

from .models import Expense

def create_expense(title, amount, days):
    """
    Factory method to create an expense with a datetime.
    """
    time = timezone.now() - datetime.timedelta(days=days)
    return Expense.objects.create(title=title, amount=amount, transaction_date=time)

class ExpenseIndexViewTests(TestCase):
    def test_no_expenses(self):
        """
        If there are no expenses, show a message
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No expenses are available.")
        self.assertQuerysetEqual(response.context['expense_list'], [])


class ExpenseModelTests(TestCase):

    def test_create_expense(self):
        """
        Just a test case
        """
        date = datetime.strptime('2018-12-12', '%Y-%m-%d')
        expense = Expense(title="Wohoo", amount=1505, transaction_date=date)
        self.assertEqual(str(expense), "Wohoo - 1505 kr, 2018-12-12")
