"""
Defines applications database models
"""

import csv
import re
from datetime import datetime
from decimal import Decimal
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class Expense(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField('date payed')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} kr, {:%Y-%m-%d}".format(self.title, self.amount, self.transaction_date)


    def get_absolute_url(self):
        return reverse('expense-update', kwargs={'pk': self.pk})


class Upload(models.Model):
    ICA_CSV = 0
    KIND_CHOICES = (
        (ICA_CSV, _('ica_csv')),
    )
    file = models.FileField()
    kind = models.IntegerField(choices=KIND_CHOICES, default=ICA_CSV, verbose_name=_('Kind'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('upload-update', kwargs={'pk': self.pk})

    def expenses(self):
        expenses = []
        with self.file.open(mode='r') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                if row["Typ"] in ['Korttransaktion', 'Autogiro']:
                    expense, _ = Expense.objects.get_or_create(title=row["Text"],
                                                                     amount=self._to_decimal(row["Belopp"]),
                                                                     transaction_date=self._parse_date(row["\ufeffDatum"]))
                    expenses.append(expense)
        return expenses

    @staticmethod
    def _to_decimal(string):
        string = re.sub(r',', ".", string)
        string = re.sub(r' |kr', "", string)
        return -1 * Decimal(string)


    @staticmethod
    def _parse_date(string):
        return datetime.strptime(string, '%Y-%m-%d').date()
