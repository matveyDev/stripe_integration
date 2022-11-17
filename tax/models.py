from django.db import models


class Tax(models.Model):
    amount_percent = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    amount_fixed = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f'Tax {self.amount_percent}%, fixed: {self.amount_fixed}'

    class Meta:
        verbose_name = 'Tax'
        verbose_name_plural = 'Taxes'
