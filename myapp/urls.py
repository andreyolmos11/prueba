from django.urls import path
from . import views

app_name = 'petshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('customers/', views.customers, name='customers'),
    path('customers/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('orders/', views.orders, name='orders'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('pets/', views.pets, name='pets'),
    path('pets/add/', views.add_pet, name='add_pet'),
    path('vets/', views.vets, name='vets'),
    path('vets/<int:vet_id>/', views.vet_detail, name='vet_detail'),
]

