from django.contrib import admin
from .models import Category, Expense, Expense_Transaction, Users
# Register your models here.
admin.site.register(Category)
# admin.site.register(Expense)
# admin.site.register(Expense_Transaction)
# admin.site.register(Users)
# Define the admin class
class AuthorUser(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    pass

# Register the admin class with the associated model
admin.site.register(Users, AuthorUser)

# Register the Admin classes for Book using the decorator
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'amount', 'date', 'user_id', 'display_category')
    pass

# Register the Admin classes for BookInstance using the decorator
@admin.register(Expense_Transaction) 
class ExpenseTransactionAdmin(admin.ModelAdmin):
    list_filter = ('payment_type', 'trans_date')
    fieldsets = (
        (None, {
            'fields': ('id', 'expense', 'posted_amount')
        }),
        ('Transaction Type', {
            'fields': ('payment_type', 'trans_date')
        }),
    )
    pass