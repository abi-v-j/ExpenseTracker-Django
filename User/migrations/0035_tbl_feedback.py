# Generated by Django 5.1.6 on 2025-03-24 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0001_initial'),
        ('User', '0034_remove_tbl_userincome_incometype_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_date', models.DateField(auto_now_add=True)),
                ('feedback_content', models.TextField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
