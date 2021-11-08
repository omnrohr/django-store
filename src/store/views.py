from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Order, OrderItems, User, ShippingAddress
import json

# Create your views here.


def home_view(request):
    all_procuts = Product.objects.all()
    context = {"products": all_procuts}
    return render(request, 'store/store.html', context)


def cart_view(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, completed=False)
        # go to newdjango project to understand the relation from terminal
        items = order.orderitems_set.all()
        # it will return all orderitems have the order number
    else:
        items = []
        # if user not authenticated
        order = {'get_cart_items': 0, 'get_cart_total': 0}
    context = {"all_items": items, "the_order": order}
    return render(request, 'store/cart.html', context)


def checkout_view(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, completed=False)
        # go to newdjango project to understand the relation from terminal
        items = order.orderitems_set.all()
        # it will return all orderitems have the order number
    else:
        items = []
        # if user not authenticated
        order = {'get_cart_items': 0, 'get_cart_total': 0}
    context = {"all_items": items, "the_order": order}

    return render(request, 'store/checkout.html', context)


def updateitem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(action, productId)
    return JsonResponse('Item was added', safe=False)
