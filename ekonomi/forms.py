from django import forms

class ExpenseForm(forms.ModelForm):
    title = forms.CharField(label="Titel", max_length=200)