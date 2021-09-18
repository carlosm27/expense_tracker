from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',Expenses.as_view(),name='expense-tracker'),
    path('dataframe', views.expenses_dataframe, name='expenses-dataframe'),


]