from django.db import models
from django.utils.translation import gettext as _
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class Product(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('Название товара'))
    received_at = models.DateField(verbose_name=_('Дата поступления'))
    price = models.DecimalField(max_digits=30, decimal_places=2 ,verbose_name=_('Цена товара'))
    measure_unit = models.CharField(max_length=10, verbose_name=_('Единица измерения'))
    supplier_name = models.CharField(max_length=100, verbose_name=_('Имя поставщика'))
    category = models.ForeignKey('product.productcategory', on_delete=models.CASCADE,
                                 verbose_name=_('Категория товара'))
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

    on_site = CurrentSiteManager('site')
    # To keep posibility to work with objects 
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Название категории'))
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

    on_site = CurrentSiteManager('site')
    # To keep posibility to work with objects 
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'
