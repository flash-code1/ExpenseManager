from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique id
# Create your models here.
class Category(models.Model):
    """ Model representing an Expense Category"""
    name = models.CharField(max_length=200, help_text='Enter a Category (e.g. grocery)')
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Expense(models.Model):
    """Model representing a Expense."""
    # FK used - beacause expenses are posted by individuals and also tied to a category
    user_id = models.ForeignKey('Users', on_delete=models.SET_NULL, null=True)
    # ManyToManyField 
    category_id = models.ManyToManyField(Category, help_text='Select a Category for this Expense')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the Expense')
    amount = models.DecimalField(decimal_places=2, help_text='Enter Expense Amount', max_digits=9)
    date = models.DateField(null=True, blank=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('expense-detail', args=[str(self.id)])
    def display_category(self):
        """Create a string for the Category. This is required to display category in Admin."""
        return ', '.join(category_id.name for category_id in self.category_id.all()[:3])
    #give it a short name
    display_category.short_description = 'Category'
class Expense_Transaction(models.Model):
    """Model representing a specific Transaction of Expenses"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Expense across whole System')
    expense = models.ForeignKey('Expense', on_delete=models.SET_NULL, null=True)
    posted_amount = models.DecimalField(decimal_places=2, help_text='Enter Posted Amount', max_digits=9)
    trans_date = models.DateField(null=True, blank=True)
    PAYMENT_STATUS = (
        ('c', 'Credit'),
        ('d', 'Debit')
    )
    payment_type = models.CharField(max_length=1, choices=PAYMENT_STATUS, blank=True, default='c', help_text='Transaction Type')
    class Meta:
        ordering = ['trans_date']
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.expense.title})'
class Users(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'