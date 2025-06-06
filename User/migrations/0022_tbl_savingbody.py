# Generated by Django 5.1.6 on 2025-03-08 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0021_delete_tbl_savingbody'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_savingbody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('savingbody_amount', models.CharField(max_length=30)),
                ('savingbody_date', models.DateField(auto_now_add=True)),
                ('savinghead_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_savinghead')),
            ],
        ),
    ]
