from operator import mod
from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('Название товара'))
    received_at = models.DateField(verbose_name=_('Дата поступления'))
    price = models.DecimalField(max_digits=30, decimal_places=2 ,verbose_name=_('Цена товара'))
    measure_unit = models.CharField(max_length=10, verbose_name=_('Единица измерения'))
    supplier_name = models.CharField(max_length=100, verbose_name=_('Имя поставщика'))

    def __str__(self):
        return f'{self.name}'