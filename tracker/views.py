from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Expense_data

import pandas as pd
# Create your views here.

def expenses_form(request):
    expenses=Expense_data.objects.all()
    form=ExpenseForm()

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("expenses-dataframe")
    context={'expenses': expenses, 'form':form}
    return render(request,'tracker/tracker_form.html',context)




def expenses_dataframe(request):
    data=Expense_data.objects.all().values()
    df=pd.DataFrame(data)
    context={'df':df.to_html()}
    return render(request, 'tracker/tracker_data.html', context)






