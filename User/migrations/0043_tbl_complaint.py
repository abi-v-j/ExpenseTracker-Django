# Generated by Django 5.1.7 on 2025-04-02 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0001_initial'),
        ('User', '0042_delete_tbl_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_title', models.CharField(max_length=100)),
                ('complaint_content', models.TextField(max_length=100)),
                ('complaint_reply', models.TextField(max_length=100)),
                ('complaint_date', models.DateField(auto_now_add=True)),
                ('complaint_status', models.TextField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
