from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse
from .models import Expense

class IndexView(generic.ListView):
    template_name = 'expenses/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Expense.objects.order_by('-transaction_date')[:5]


class DetailView(generic.DetailView):
    model = Expense
    template_name = 'expenses/detail.html'


class ResultsView(generic.DetailView):
    model = Expense
    template_name = 'expenses/results.html'

def create(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    return HttpResponseRedirect(reverse('results', args=(expense.id,)))
