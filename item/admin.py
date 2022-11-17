from django.contrib import admin
from django import forms

from .models import Item


class ItemAdminForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminForm
    search_fields = ('name', 'price',)
