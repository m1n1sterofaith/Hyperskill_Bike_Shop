from django.urls import path
from shop.views import bikes_view, OrderCreateView, order_success_view

urlpatterns = [
    path('bikes/', bikes_view, name='bikes'),
    path('bikes/<int:pk>/', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:order_number>/', order_success_view, name='order_success')
]
