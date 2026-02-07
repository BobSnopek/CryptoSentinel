# get_price.py
import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import CryptoPrice, PriceAlert

def check_alerts(symbol, current_price):
    """
    Checks if the current price triggers any active alerts in the database.
    """
    alerts = PriceAlert.objects.filter(symbol=symbol, is_active=True)
    
    for alert in alerts:
        triggered = False
        if alert.alert_type == 'ABOVE' and current_price >= alert.target_price:
            triggered = True
        elif alert.alert_type == 'BELOW' and current_price <= alert.target_price:
            triggered = True
            
        if triggered:
            print(f"!!! ALERT TRIGGERED !!! {symbol} is now {alert.alert_type} {alert.target_price} (Current: {current_price})")
            # In a real bot, we would trigger a trade or send a Telegram message here.
            # alert.is_active = False # Optional: deactivate alert after trigger
            # alert.save()

def fetch_and_alert():
    symbols = ['BTCUSDT', 'ETHUSDT', 'SUIUSDT', 'SOLUSDT', 'BNBUSDT']
    api_url = "https://api.binance.com/api/v3/ticker/price"
    
    for symbol in symbols:
        try:
            response = requests.get(api_url, params={'symbol': symbol})
            data = response.json()
            current_price = float(data['price'])
            
            # Save to history
            CryptoPrice.objects.create(symbol=symbol, price=current_price)
            
            # Run alert logic
            check_alerts(symbol, current_price)
            
        except Exception as e:
            print(f"Error fetching {symbol}: {e}")

if __name__ == "__main__":
    fetch_and_alert()