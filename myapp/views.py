from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Category, Customer, Order, Cart, Pet, Vet
from .forms import PetForm

# View para agregar un nuevo producto
def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)
        Product.objects.create(name=name, description=description, price=price, category=category)
        messages.success(request, 'Producto agregado correctamente')
        return redirect('products')
    else:
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'add_product.html', context)

# View para editar un producto existente
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)
        product.category = category
        product.save()
        messages.success(request, 'Producto editado correctamente')
        return redirect('products')
    else:
        categories = Category.objects.all()
        context = {'product': product, 'categories': categories}
        return render(request, 'edit_product.html', context)

# View para eliminar un producto existente
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Producto eliminado correctamente')
    return redirect('products')

# View para agregar un nuevo cliente
def add_customer(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        Customer.objects.create(name=name, email=email, address=address, phone=phone)
        messages.success(request, 'Cliente agregado correctamente')
        return redirect('customers')
    else:
        return render(request, 'add_customer.html')

# View para editar un cliente existente
def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.name = request.POST['name']
        customer.email = request.POST['email']
        customer.address = request.POST['address']
        customer.phone = request.POST['phone']
        customer.save()
        messages.success(request, 'Cliente editado correctamente')
        return redirect('customers')
    else:
        context = {'customer': customer}
        return render(request, 'edit_customer.html', context)

# View para eliminar un cliente existente
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    messages.success(request, 'Cliente eliminado correctamente')
    return redirect('customers')

# View para agregar una nueva mascota
def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'petshop/add_pet.html', {'form': form})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'products': products})

def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    orders = Order.objects.filter(customer=customer)
    return render(request, 'customer_detail.html', {'customer': customer, 'orders': orders})

def order_detail(request, pk):
    order = Order.objects.get(pk=pk)
    cart_items = Cart.objects.filter(order=order)
    return render(request, 'order_detail.html', {'order': order, 'cart_items': cart_items})

def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    return render(request, 'pet_detail.html', {'pet': pet})

def vet_list(request):
    vets = Vet.objects.all()
    return render(request, 'vet_list.html', {'vets': vets})

def vet_detail(request, pk):
    vet = Vet.objects.get(pk=pk)
    return render(request, 'vet_detail.html', {'vet': vet})
