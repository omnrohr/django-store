from .views import *
from django.urls import path

urlpatterns = [
    path('', home_view, name='home'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('update_item/', updateitem, name='updateitem'),
    path('process_order/', orderprocess, name='process_order'),
]
