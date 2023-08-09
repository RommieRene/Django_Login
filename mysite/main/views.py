from django.shortcuts import render, redirect
from .forms import NewUserForm, ContactFrom
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Cart, Category, Product, Contact
from django.contrib.auth.models import User
# Create your views here.
user_id = None

def index(request):
	category_list = Category.objects.all()
	cart_list = Cart.objects.filter(user=user_id)

	return render(request,'main/index.html', context={
        'category_list':category_list,
		'cart_list':cart_list
    })

def cart(request):
    cart_list = Cart.objects.filter(user=user_id)
    return render(request, 'main/cart.html', context={
        'cart_list':cart_list
    })

def product(request, id):
    product_list = Category.objects.filter(pk=id)
    cart_list = Cart.objects.filter(user=user_id)
    return render(request,'main/product.html', context={
        'product_list':product_list,
		'cart_list':cart_list
    })

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	global user_id
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			user_id=user.id	
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")

def contact(request):
	if request.method == 'POST':
		form = ContactFrom(request.POST)
		if form.is_valid():
			Contact.objects.create(**form.cleaned_data)
			return redirect('index')
	else:
		form = ContactFrom()
	return render(request,'main/contact.html', context={
        'contact_form':form
    })
def add_to_cart(request):
	if request.method == 'POST':
		prod_id = request.POST.get('prod_id')
		my_prod = Product.objects.get(id=prod_id)
		my_user = User.objects.get(pk=user_id)
		Cart.objects.create(product=my_prod, user=my_user)
		return redirect('index')
	
def delete_to_cart(request):
	if request.method == 'POST':
		prod_id = request.POST.get('prod_id')
		Cart.objects.get(pk=prod_id).delete()
		return redirect('cart')
