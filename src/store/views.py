from django.shortcuts import render

from store.models import Product

# Create your views here.


def home_view(request):
    all_procuts = Product.objects.all()
    context = {"products": all_procuts}
    return render(request, 'store/store.html', context)


def cart_view(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout_view(request):
    context = {}
    return render(request, 'store/checkout.html', context)
