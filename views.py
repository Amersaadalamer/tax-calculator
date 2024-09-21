from django.http import HttpResponse
from django.shortcuts import render

def calculate_tax(request, price):
    try:
        price = float(price)
    except (ValueError, TypeError):
        price = 100.0

    tax_rate = 0.15
    tax = price * tax_rate
    total_price = price + tax

    context = {
        'price': price,
        'tax_rate': tax_rate * 100,
        'total_price': total_price,
    }
    return render(request, 'calculator/tax_calculation.html', context)
