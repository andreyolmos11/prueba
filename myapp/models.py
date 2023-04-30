from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'


class Pet(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    breed = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Vet(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
