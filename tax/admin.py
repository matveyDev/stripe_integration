from django.contrib import admin
from .models import Tax


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    model = Tax
