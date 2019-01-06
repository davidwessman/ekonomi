"""
View-objects in application
"""

from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractYear
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from .models import Expense, Upload

class ExpenseSummary(ListView):
    template_name = 'ekonomi/expense_summary.html'
    model = Expense


    def get_queryset(self):
        expenses = Expense.objects \
                          .order_by('-transaction_date') \
                          .annotate(month=ExtractMonth('transaction_date'),
                                    year=ExtractYear('transaction_date')) \
                          .values('month', 'year') \
                          .annotate(sum=Sum('amount')) \
                          .order_by()
        return expenses


class ExpenseIndex(ListView):
    model = Expense
    def get_queryset(self):
        """Return the last five published questions."""
        return Expense.objects.order_by('-transaction_date')

    def get_context_data(self, **kwargs):
        context = super(ExpenseIndex, self).get_context_data(**kwargs)
        context['sum'] = context['expense_list'].aggregate(Sum('amount'))['amount__sum']
        return context


class ExpenseCreate(CreateView):
    model = Expense
    fields = ['title', 'amount', 'transaction_date']


class ExpenseUpdate(UpdateView):
    model = Expense
    fields = ['title', 'amount', 'transaction_date']


class ExpenseDelete(DeleteView):
    model = Expense
    success_url = reverse_lazy('expense-list')


class UploadCreate(CreateView):
    model = Upload
    fields = ['file', 'kind']

    def post(self, request, *args, **kwargs):
        print('POST')
        print(request.POST)
        print(request.FILES)
        return super(UploadCreate, self).post(request, *args, **kwargs)


class UploadUpdate(UpdateView):
    model = Upload
    fields = ['file', 'kind']


class UploadIndex(ListView):
    def get_queryset(self):
        """Return the last five published questions."""
        return Upload.objects.all()


class UploadDelete(DeleteView):
    model = Upload
    success_url = reverse_lazy('upload-list')
