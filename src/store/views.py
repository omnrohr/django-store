from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Order, OrderItems, User, ShippingAddress
import json

# Create your views here.


def home_view(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, completed=False)
        # go to newdjango project to understand the relation from terminal
        items = order.orderitems_set.all()
        # it will return all orderitems have the order number
        cartItems = order.get_cart_items

    else:
        items = []
        # if user not authenticated
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']

    all_procuts = Product.objects.all()
    context = {"products": all_procuts, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart_view(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, completed=False)
        # go to newdjango project to understand the relation from terminal
        items = order.orderitems_set.all()
        # it will return all orderitems have the order number
        cartItems = order.get_cart_items
    else:
        items = []
        # if user not authenticated
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
    context = {"all_items": items, "the_order": order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout_view(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, completed=False)
        # go to newdjango project to understand the relation from terminal
        items = order.orderitems_set.all()
        # it will return all orderitems have the order number
        cartItems = order.get_cart_items
    else:
        items = []
        # if user not authenticated
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {"all_items": items, "the_order": order, 'cartItems': cartItems}

    return render(request, 'store/checkout.html', context)


def updateitem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(action, productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, completed=False)

    orderItems, created = OrderItems.objects.get_or_create(
        order=order, product=product)

    if isinstance((orderItems.quantity), int):
        print(product)
        print(order)
        if action == 'add':
            orderItems.quantity = (orderItems.quantity + 1)

        elif action == 'remove':
            orderItems.quantity = (orderItems.quantity - 1)

        orderItems.save()

        if orderItems.quantity <= 0:
            orderItems.delete()
    else:
        raise TypeError
    return JsonResponse('Item was added', safe=False)


def orderprocess(request):
    print(request.body)
    return JsonResponse('payment done...', safe=False)
