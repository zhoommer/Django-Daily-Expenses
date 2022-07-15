from django.db import models

# Create your models here.


class Expenses(models.Model):
    payment_method = models.CharField(max_length=15, verbose_name='Odeme Yontemi')
    category = models.CharField(max_length=15, verbose_name='Kategori')
    item = models.CharField(max_length=25, verbose_name='Item')
    quantity = models.SmallIntegerField(verbose_name='Adet')
    amount = models.FloatField(verbose_name='Tutar')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Tarih')
    check = models.BooleanField(default=False, verbose_name='Secim')
    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

    def __str__(self):
        return self.item

