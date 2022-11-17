from django.db import models

from discount.models import Discount
from tax.models import Tax


class Order(models.Model):
    discount = models.OneToOneField(Discount, related_name='order', default=0, on_delete=models.SET_DEFAULT)
    tax = models.OneToOneField(Tax, related_name='order', default=0, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return f'Order #{self.id}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
