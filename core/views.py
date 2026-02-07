# core/views.py
from django.shortcuts import render
from .models import CryptoPrice

def public_dashboard(request):
    """
    Fetches the latest 50 crypto prices and displays them on a public page.
    """
    # Get all price records, ordered by newest first
    prices = CryptoPrice.objects.all().order_by('-timestamp')[:50]
    
    context = {
        'prices': prices,
        'page_title': 'CryptoSentinel Public Monitor'
    }
    
    return render(request, 'dashboard.html', context)