from django.db import models
from django.utils.timezone import now

# Create your models here.
CATEGORY_CHOICES = [
    ("Food","Food"),
    ("Travel","Travel"),
    ("Shopping","Shopping"),
    ("Necessities","Necessities"),
    ("Entertainment","Entertainment"),
    ("Other","Other")]

class Expense_data(models.Model):
        amount=models.CharField(max_length=10)
        category=models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='Food')
        date=models.DateField(default=now)
        description=models.CharField(max_length=200, blank=True)

        def __str__(self):
            return self.category
