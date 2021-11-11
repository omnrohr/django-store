from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer, Product, Order, OrderItems, User, ShippingAddress
import json
import datetime
from .utils import cookieCart, cartData, guestOrder
# Create your views here.


def home_view(request):

    data = cartData(request)
    cartItems = data['cartItems']

    all_procuts = Product.objects.all()
    context = {"products": all_procuts, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart_view(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    context = {"all_items": items, "the_order": order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout_view(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
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
    data = json.loads(request.body)
    transaction_id = datetime.datetime.now().timestamp()
    print(transaction_id)
    if request.user.is_authenticated:
        data = json.loads(request.body)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, completed=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    if total == order.get_cart_total:
        order.completed = True

    else:
        total = order.get_cart_total
        order.completed = True

    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            zipcode=data['shipping']['zipcode'],
            state=data['shipping']['state']
        )

    return JsonResponse('payment done...', safe=False)
