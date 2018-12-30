"""
View-objects in application
"""

from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView

from .models import Expense

class IndexView(ListView):
    template_name = 'expenses/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Expense.objects.order_by('-transaction_date')[:5]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['sum'] = context['expense_list'].aggregate(Sum('amount'))['amount__sum']
        return context


class ExpenseDetail(DetailView):
    model = Expense


class ExpenseCreate(CreateView):
    model = Expense
    fields = ['title', 'amount', 'transaction_date']


class ExpenseUpdate(UpdateView):
    model = Expense
    fields = ['title', 'amount', 'transaction_date']


class ExpenseDelete(DeleteView):
    model = Expense
    success_url = reverse_lazy('index')
