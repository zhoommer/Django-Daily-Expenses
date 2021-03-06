# Generated by Django 3.2.12 on 2022-04-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=15, verbose_name='Odeme Yontemi')),
                ('category', models.CharField(max_length=15, verbose_name='Kategori')),
                ('item', models.CharField(max_length=25, verbose_name='Item')),
                ('quantity', models.SmallIntegerField(verbose_name='Adet')),
                ('amount', models.FloatField(verbose_name='Tutar')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Tarih')),
            ],
            options={
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
            },
        ),
    ]
