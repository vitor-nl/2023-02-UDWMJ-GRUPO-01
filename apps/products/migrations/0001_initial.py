# Generated by Django 4.2.6 on 2023-10-31 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.TextField(max_length=100, verbose_name='Descricao')),
                ('date_fabrication', models.DateField(verbose_name='Data Fabricacao')),
                ('is_active', models.BooleanField(default=False, verbose_name='Ativo')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['id'],
            },
        ),
    ]