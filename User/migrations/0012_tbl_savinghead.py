# Generated by Django 5.1.6 on 2025-03-07 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_tbl_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_savinghead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('savinghead_id', models.CharField(max_length=100)),
                ('savinghead_title', models.CharField(max_length=30)),
                ('savinghead_goal', models.TextField(max_length=100)),
                ('savinghead_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
