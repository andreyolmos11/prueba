from django.contrib import admin
from .models import Product, Category, Customer, Order, Cart, Pet, Vet

# Registra los modelos para que sean accesibles desde el panel de administración de Django
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Pet)
admin.site.register(Vet)


# Register your models here.
