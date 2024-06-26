from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from random import randrange
from django.core.mail import send_mail
from .models import StockModel
from .forms import StockForm
from .models import CryptoModel
from .forms import CryptoForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
import redis
import json
from django.core.cache import cache



# Create your views here.
def usignup(request):
    if request.method == "POST":
        un = request.POST.get("un")
        em = request.POST.get("em")
        pw1 = request.POST.get("pw1")
        pw2 = request.POST.get("pw2")
        if pw1 == pw2:
            try:
                usr = User.objects.get(username=un)
                return render(request, "usignup.html", {"msg": "Already registered"})
            except User.DoesNotExist:
                usr = User.objects.create_user(username=un, email=em, password=pw1)
                usr.save()
                return redirect("ulogin")
        else:
            return render(request, "usignup.html", {"msg": "Passwords did not match"})
    else:
        return render(request, "usignup.html")
		

def ulogin(request):
    if request.method == "POST":
        un = request.POST.get("un")
        em = request.POST.get("em")
        pw = request.POST.get("pw")
        usr = authenticate(username=un, email=em, password=pw)
        if usr is not None:
            login(request, usr)
            return redirect("home")
        else:
            return render(request, "ulogin.html", {"msg": "Invalid login"})
    else:
        return render(request, "ulogin.html")




def ulogout(request):
	logout(request)
	return redirect("ulogin")

def urnp(request):
	if request.method == "POST":
		un = request.POST.get("un")
		em = request.POST.get("em")
		try:
			usr = User.objects.get(email = em)
			pw = ""	
			text = "0123456789"
			for i in range(6):
				pw = pw + text[randrange(len(text))]
			print (pw)
			subject = "Hello again from Financial Portfolio Manager"
			msg = "Hi again, we've noticed you've requested for "  + str(pw)
			host = 'monicadjango10@gmail.com'
			recepient = [em]
			send_mail(subject, msg, host, recepient)
			usr.set_password(pw)
			usr.save()
			return redirect("ulogin")
		except User.DoesNotExist:
			return render(request, "urnp.html", {"msg": "email not registered"})
	else:
		return render(request, "urnp.html")


# Create your views here.
def home(request):
	if request.user.is_authenticated:
		return render(request, "home.html")
	else:
		return redirect("usignup")

def create(request):
	if request.user.is_authenticated:
		user = request.user
		print(user)			
		form = StockForm(request.POST)
		if request.method == "POST":
			if form.is_valid():
				todo = form.save(commit = False)
				todo.user = user
				todo.save()
				fm = StockForm()
				return render(request, "create.html", {"fm": fm, "msg": "Stock Investment Added "})
			else:
				return render(request, "create.html", {"fm": form, "msg": "check issue"})
		else:
			fm = StockForm()
			return render(request, "create.html", {"fm":fm})

def save_stock_data(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            stock_instance = form.save(commit=False)
            stock_instance.user = request.user
            stock_instance.save()
            
            # Save relevant data to Redis
            stock_data = {
                'stock_name': stock_instance.stock_name,
                'stock_number': stock_instance.stock_number,
                'stock_pps': stock_instance.stock_pps,
                # Add more fields as needed
            }
            key = f'stock_data_{request.user.id}'  # Using user ID as part of the key
            cache.set(key, stock_data)
            
            return redirect('home')  # Redirect to home page or any other page as needed
    else:
        form = StockForm()
    return render(request, 'save_stock_data.html', {'form': form})

def delete_stock(request, id):
	dd = StockModel.objects.get(stock_id=id)
	dd.delete()
	return redirect("view")

def view(request):
    if request.user.is_authenticated:
        user = request.user
        form = StockForm()
        todos = StockModel.objects.filter(user=user)
        return render(request, "view.html", {"form": form, "todos": todos})
		
def create_crypto(request):
	if request.user.is_authenticated:
		user = request.user
		print(user)			
		form = CryptoForm(request.POST)
		if request.method == "POST":
			if form.is_valid():
				todo = form.save(commit = False)
				todo.user = user
				todo.save()
				print(todo)
				fm = CryptoForm()
				return render(request, "create_crypto.html", {"fm": fm, "msg": "Crytpo Investment Added "})
			else:
				return render(request, "create_crypto.html", {"fm": form, "msg": "check issue"})
		else:
			fm = CryptoForm()
			return render(request, "create_crypto.html", {"fm":fm})

def delete_crypto(request, id):
	dd = CryptoModel.objects.get(crypto_id=id)
	dd.delete()
	return redirect("view_crypto")

def view_crypto(request):
    if request.user.is_authenticated:
        user = request.user
        form = CryptoForm()
        todos = CryptoModel.objects.filter(user=user)
        return render(request, "view_crypto.html", {"form": form, "todos": todos})


		
