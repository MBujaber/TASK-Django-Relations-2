# Generated by Django 4.1.2 on 2022-10-19 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
    ]