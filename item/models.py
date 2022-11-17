from django.db import models
from order.models import Order


class Item(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name')
    description = models.TextField(max_length=1024, verbose_name='description')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='price')
    order = models.ForeignKey(Order, related_name='items', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.price}'

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
