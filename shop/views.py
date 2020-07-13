from django.shortcuts import render, HttpResponse, redirect
from .models import Category, ProductGroup, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from cart.cart import Cart
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def cart_add(request):
    id = request.GET['add_cart']
    quantity = request.GET['count']
    cart = Cart(request)
    product = Product.objects.get(id=int(id))
    cart.add(product=product, quantity=int(quantity))
    return redirect("cart_detail")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'cart_detail.html')


def register_page(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Неверное имя пользователя или пароль!')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return render(request, 'base_shop.html')


def personal_page(request):
    return render(request, 'personal_page.html')


def index(request):
    return render(request, 'base_shop.html')


def de_scripts(request):
    des_date = request.GET['id']
    id_group, id_id = des_date.split(';')
    date = Product.objects.filter(parent__group=id_group, id=int(id_id))
    return render(request, 'bases_description.html', context={'date': date})


def search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        date = Product.objects.filter(title__icontains=search_query)
        return render(request, 'bases.html', context={'date': date})
    else:
        return render (request, 'base_shop.html')


# Упаковка
def cake(request):
    date = Product.objects.filter(parent__group='cakes')
    return render(request, 'bases.html', context={'date': date})


def cupcake(request):
    date = Product.objects.filter(parent__group='cupcakes')
    return render(request, 'bases.html', context={'date': date})


def candy_chock(request):
    date = Product.objects.filter(parent__group='candy_chocolate')
    return render(request, 'bases.html', context={'date': date})


