# Generated by Django 4.1 on 2023-12-01 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Livro',
            new_name='Books',
        ),
    ]
