from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Expense_data

import pandas as pd
# Create your views here.

class Expenses(CreateView):
    model=Expense_data
    fields = ['amount', 'category', 'date', 'description']
    context_object_name = 'expenses'
    template_name = 'tracker/tracker_form.html'




def expenses_dataframe(request):
    data=Expense_data.objects.all().values()
    df=pd.DataFrame(data)
    context={'df':df.to_html()}
    return render(request, 'tracker/tracker_data.html', context)






