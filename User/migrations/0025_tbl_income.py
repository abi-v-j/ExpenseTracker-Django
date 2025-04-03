# Generated by Django 5.1.6 on 2025-03-08 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_tbl_adminregistration_tbl_expensetype'),
        ('Guest', '0001_initial'),
        ('User', '0024_tbl_budget_tbl_complaint_tbl_savinghead_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_amount', models.CharField(max_length=30)),
                ('income_date', models.DateField(auto_now_add=True)),
                ('income_note', models.TextField(max_length=30)),
                ('incomecategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_incometype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
