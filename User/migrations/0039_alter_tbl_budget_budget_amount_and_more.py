# Generated by Django 5.1.7 on 2025-03-27 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0038_tbl_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_budget',
            name='budget_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tbl_expense',
            name='expense_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tbl_expense',
            name='expense_bill',
            field=models.FileField(blank=True, null=True, upload_to='Assets/ExpenseBill/'),
        ),
        migrations.AlterField(
            model_name='tbl_expense',
            name='expense_note',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='tbl_income',
            name='income_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tbl_income',
            name='income_note',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='tbl_savingbody',
            name='savingbody_amount',
            field=models.FloatField(),
        ),
    ]
