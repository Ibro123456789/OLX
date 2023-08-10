from time import timezone
from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Chat, Message, Address, Profile
from django.contrib import messages
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')
    
def categories(request):
    categories = Category.objects.all()
    return render (request, 'blog/categories.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'blog/category_detail.html', {'category': category}) 

def register(request):
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('home_page')
    else:
        print('Form is not valid')
        messages.error(request, 'Error Processing Your Request')
        context = {'form': form}
        return render(request, 'register.html', context)
    return render(request, 'register.html', {})

def login_site(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username = email, password = password)
		if user:
			login(request, user)
			return redirect('/seeds/')
		else:
			return redirect('/login/')
	else:	
		return render(request, 'login.html')

def logout_site(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username = email, password = password)
		if user:
			login(request, user)
			return redirect('/farmer_homepage/')
		else:
			return redirect('/login/')

	else:	
		return render(request, 'logout.html')

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST': 
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                profile= Profile()
                profile.user = user
                profile.save()
                login(request, user)
                return redirect('index')
        else:
            form = RegisterForm()
        return render(request , 'register.html' , {'form': form})
    return redirect('index')

@login_required
def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html', {})

def create_product(request, category_id):
    form = Product(request.POST or None, request.FILES or None)
    category = get_object_or_404(Category, pk=category_id)
    if form.is_valid():
        category_product = category.song_set.all()
        for s in category_product:
            if s.name == form.cleaned_data.get("song_title"):
                context = {
                    'category': category,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'create_product.html', context)
            product = form.save(commit=False)
            product.category = category
            product.save()
            return render(request, 'detail.html', {'category': category})
        context = {
            'category': category,
            'form': form,
        }
        return render(request, 'create_product.html', context)

def edit_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == "POST":
        form = Product(request.POST, instance=product)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
        return render(request, 'edit_product.html', {'product': product, 'form':form})
    else:
        form = Product(instance=product)
    return render(request,'edit_product.html', {'form': form})

def delete_product(request, slug):
    products = get_object_or_404(Product, slug=slug)
    cart = Product.objects.get(user = request.user, products=products)
    cart.delete()
    return redirect('cart')

def profile_detail(request, id):
    user = get_object_or_404(Profile, pk=id)
    return render(request, 'profile_detail.html', {'user': user})

def chat(request):
    return render(request, 'room.html')
