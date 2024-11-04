from ast import Return
from contextlib import nullcontext
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from .models import Product, Transaction
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome!')
            return redirect('mainApp')  # Change 'mainApp' to your actual redirect URL name
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    next_page = '/login/'

@login_required
def index(request):
    product_list = Product.objects.all()
    return render(request, 'index.html', 
    {'products' : product_list})
    #return HttpResponse("Welcome to Inventory Tool")

@login_required
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("A sample Inventory project")

@login_required
def products(request):
    Product_list = Product.objects.all()
    tot = 0
    for Producty in Product_list:
        tot = tot + Producty.quantity
    
    return render(request, 'products.html',
    {'Products' : Product_list, 'tot' : tot})
    #return HttpResponse("List of products")


@login_required
def sub(request):
    val1 = int(request.POST['val']) #quantity to reduce
    val2 = request.POST['cname'] #name of product to reduce
    c1 = Product.objects.get(name = val2)
    
    c1.quantity = c1.quantity - val1
    c1.save()

    # Log the transaction
    transaction = Transaction(
        product=c1,
        username=request.user.username,  # Automatically use the logged-in user's username
        old_quantity=c1.quantity + val1,
        new_quantity=c1.quantity
    )
    transaction.save()

    Product_list = Product.objects.all()
    tot = 0
    for Producty in Product_list:
        tot = tot + Producty.quantity
    
    return render(request, 'purchase.html',
    {'cname1' : val2, 'val': val1, 'tc' :tot})

@login_required
def returnitem(request):
    val1 = int(request.POST['val']) #quantity to reduce
    val2 = request.POST['cname'] #name of product to reduce
    c1 = Product.objects.get(name = val2)
    
    c1.quantity = c1.quantity + val1
    c1.save()

    # Log the transaction
    transaction = Transaction(
        product=c1,
        username=request.user.username,  # Automatically use the logged-in user's username
        old_quantity=c1.quantity - val1,
        new_quantity=c1.quantity
    )
    transaction.save()

    Product_list = Product.objects.all()
    tot = 0
    for Producty in Product_list:
        tot = tot + Producty.quantity
    
    return render(request, 'purchase.html',
    {'cname1' : val2, 'val': val1, 'tc' :tot})
    
@login_required
def additem(request):
    qt = int(request.POST['val'])
    cname = request.POST['cname']
    curl = request.POST['curl']

    
    if(qt > 0):
        c = Product(name=cname, quantity=qt, img=curl)
        c.save()

        # Log the transaction
        transaction = Transaction(
            product=c,
            username=request.user.username,  # Automatically use the logged-in user's username
            old_quantity=0,
            new_quantity=qt
        )
        transaction.save()
    
    
    return redirect('/')
    

@login_required
def delete(request):
    
    cname = request.POST['cname']
    c1 = Product.objects.get(name = cname)
    val1 = c1.quantity
    # Log the transaction
    transaction = Transaction(
        product=c1,
        username=request.user.username,  # Automatically use the logged-in user's username
        old_quantity=c1.quantity,
        new_quantity=0
    )
    transaction.save()

    c1.delete()
    Product_list = Product.objects.all()
    tot = 0
    for Producty in Product_list:
        tot = tot + Producty.quantity
    
    return render(request, 'purchase.html',
    {'cname1' : cname, 'val': val1, 'tc' :tot})

@login_required
def transaction_list(request):
    product_id = request.GET.get('product_id')  # Get the product ID from query parameters
    transactions = Transaction.objects.all()  # Get all transactions
    selected_product = None  # Default to None

    if product_id:
        selected_product = get_object_or_404(Product, id=product_id)  # Get the selected product
        transactions = transactions.filter(product__id=product_id)  # Filter by product ID

    products = Product.objects.all()  # Get all products for the dropdown
    return render(request, 'transactions.html', {
        'transactions': transactions,
        'products': products,
        'selected_product': selected_product,
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    transactions = Transaction.objects.filter(product=product)  # Fetch related transactions
    return render(request, 'product_detail.html', {'product': product, 'transactions': transactions})