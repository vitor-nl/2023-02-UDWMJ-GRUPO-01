# Generated by Django 4.1 on 2023-12-02 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_remove_books_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
    ]
