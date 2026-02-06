import os
import django

# Nastavení Django prostředí
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import CryptoPrice

# Simulace získání ceny (později zde bude napojení na Binance)
def save_test_price():
    new_entry = CryptoPrice(symbol="BTCUSDT", price=65432.10)
    new_entry.save()
    print("Cena Bitcoinu byla úspěšně uložena do databáze!")

if __name__ == "__main__":
    save_test_price()