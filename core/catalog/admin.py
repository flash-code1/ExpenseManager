from django.contrib import admin
from .models import Category, Expense, Expense_Transaction, Users
# Register your models here.
admin.site.register(Category)
admin.site.register(Expense)
admin.site.register(Expense_Transaction)
admin.site.register(Users)