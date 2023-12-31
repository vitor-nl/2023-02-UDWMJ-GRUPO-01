# Generated by Django 4.1 on 2023-12-05 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('author', models.CharField(max_length=50, verbose_name='Autor')),
                ('sinopse', models.TextField(max_length=100, verbose_name='Sinopse')),
                ('status', models.TextField(max_length=20, verbose_name='Status')),
                ('photo', models.FileField(blank=True, null=True, upload_to='static')),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
                'ordering': ['id'],
            },
        ),
    ]
