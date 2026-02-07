# core/admin.py
from django.contrib import admin
from .models import CryptoPrice, PriceAlert

@admin.register(CryptoPrice)
class CryptoPriceAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'price', 'timestamp')
    list_filter = ('symbol',)

@admin.register(PriceAlert)
class PriceAlertAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'target_price', 'alert_type', 'is_active')
    list_editable = ('is_active',)