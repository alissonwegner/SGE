from django.shortcuts import render

def home(request):
    product_metrics = {
        'total_cost_price': 10000,
        'total_selling_price': 30000,
        'total_quantity': 1000,
        'total_profit': 200000
    }
    context = {
        'product_metrics': product_metrics
    }
    return render(request,'home.html', context)