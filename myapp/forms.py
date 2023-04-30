from django import forms
from .models import Customer, Pet, Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone')

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'species', 'breed', 'age', 'customer')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer', 'pet', 'date', 'status')
