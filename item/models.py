from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name')
    description = models.TextField(max_length=1024, verbose_name='description')
    price = models.DecimalField()

    def __str__(self):
        return f'Item - {self.name}, {self.price}'

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
