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
				print(todo)
				fm = StockForm()
				return render(request, "create.html", {"fm": fm, "msg": "Stock Investment Added "})
			else:
				return render(request, "create.html", {"fm": form, "msg": "check issue"})
		else:
			fm = StockForm()
			return render(request, "create.html", {"fm":fm})

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


		
