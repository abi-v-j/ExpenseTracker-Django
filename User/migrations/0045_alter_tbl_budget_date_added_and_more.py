# Generated by Django 5.1.6 on 2025-04-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0044_alter_tbl_repaymentnotification_repaymentnotification_notificationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_budget',
            name='date_added',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tbl_expense',
            name='expense_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tbl_expense',
            name='expense_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='tbl_feedback',
            name='feedback_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tbl_income',
            name='income_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tbl_repayment',
            name='repayment_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tbl_savingbody',
            name='savingbody_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tbl_savinghead',
            name='savinghead_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tbl_score',
            name='score_date',
            field=models.DateField(),
        ),
    ]
