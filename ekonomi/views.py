"""
View-objects in application
"""

from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from .models import Expense, Upload

class ExpenseIndex(ListView):
    model = Expense
    def get_queryset(self):
        """Return the last five published questions."""
        return Expense.objects.order_by('-transaction_date')[:5]

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

    def form_valid(self, form):
        valid = super(UploadCreate, self).form_valid(form)
        if self.request.POST.get('file'):
            file = form.cleaned_data['file']
            print(file)
        else:
            print('Wohoo')
        form.save()
        return valid

    def form_invalid(self, form):
        print('Form invalid')
        return super(UploadCreate, self).form_invalid(form)


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
