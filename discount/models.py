from django.db import models


class Discount(models.Model):
    amount_percent = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f'Discount {self.amount_percent}%'

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'
