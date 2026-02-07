# core/models.py
from django.db import models

class CryptoPrice(models.Model):
    symbol = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=30, decimal_places=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol}: {self.price}"

    @property
    def trend(self):
        """
        Logic to determine if the price is going up or down 
        compared to the previous record.
        """
        previous_entry = CryptoPrice.objects.filter(
            symbol=self.symbol, 
            timestamp__lt=self.timestamp
        ).order_by('-timestamp').first()

        if not previous_entry:
            return 'neutral'
        
        if self.price > previous_entry.price:
            return 'up'
        elif self.price < previous_entry.price:
            return 'down'
        return 'neutral'

class PriceAlert(models.Model):
    """
    Model to store user-defined price thresholds for alerts.
    """
    symbol = models.CharField(max_length=20)
    target_price = models.DecimalField(max_digits=30, decimal_places=10)
    alert_type = models.CharField(max_length=10, choices=[('ABOVE', 'Above'), ('BELOW', 'Below')])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Alert: {self.symbol} {self.alert_type} {self.target_price}"