# Generated by Django 2.2.16 on 2020-10-18 22:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a Category (e.g. grocery)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True, editable=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Enter a brief description of the Expense', max_length=1000)),
                ('amount', models.DecimalField(decimal_places=2, help_text='Enter Expense Amount', max_digits=9)),
                ('category_id', models.ManyToManyField(help_text='Select a Category for this Expense', to='catalog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Expense_Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular Expense across whole System', primary_key=True, serialize=False)),
                ('posted_amount', models.DecimalField(decimal_places=2, help_text='Enter Posted Amount', max_digits=9)),
                ('trans_date', models.DateField(blank=True, null=True)),
                ('payment_type', models.CharField(blank=True, choices=[('c', 'Credit'), ('d', 'Debit')], default='c', help_text='Transaction Type', max_length=1)),
                ('expense', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Expense')),
            ],
            options={
                'ordering': ['trans_date'],
            },
        ),
        migrations.AddField(
            model_name='expense',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Users'),
        ),
    ]
