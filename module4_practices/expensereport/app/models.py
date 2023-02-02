from django.db import models


class ExpenseTracker(models.Model):
    date = models.DateField(auto_now_add=True)
    location = models.TextField()
    amount = models.FloatField()
    notes = models.TextField(blank=True, null=True)

    def update_expense(self, date, location, amount, notes):
        if date:
            self.date = date
        if location:
            self.location = location
        if amount:
            self.amount = amount
        if notes:
            self.notes = notes
        self.save()

    def delete_expense(self):
        self.delete()

    @classmethod
    def filter_expenses(cls, location=None, amount=None):
        expenses = cls.objects.all()
        if location:
            expenses = expenses.filter(location=location)
        if amount:
            expenses = expenses.filter(amount=amount)
        return expenses

    @classmethod
    def report(cls):
        return cls.objects.all()

    def amount_as_currency_string(self):
        return "${:,.2f}".format(self.amount)
