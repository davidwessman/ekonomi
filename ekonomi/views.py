from django.http import HttpResponse
from .models import Expense

def index(request):
    expenses = Expense.objects.order_by('-transaction_date')[:5]
    return HttpResponse("Hello World!")