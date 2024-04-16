"""
URL configuration for financial_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from fin_app.views import home, create, view, delete_stock,usignup, ulogin, ulogout, urnp, delete_crypto, create_crypto, view_crypto
from django.urls import path
from analyzer_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name = "home"),
    path("usignup/", usignup, name = "usignup"),
    path("ulogin/", ulogin, name = "ulogin"),
    path("ulogout/", ulogout, name = "ulogout"),
    path("urnp/", urnp, name = "urnp"),
    path("create/", create, name = "create"),
    path("view/", view, name = "view"),
    path("create_crypto", create_crypto, name = "create_crypto"),
    path("view_crypto", view_crypto, name= "view_crypto"),
    path("delete_stock/<int:id>/", delete_stock, name = "delete_stock"),
    path("delete_crypto/<int:id>/", delete_crypto, name = "delete_crypto"),
    path('stock_graph/', views.stock_graph, name='stock_graph'),
    path('crypto_graph/', views.crypto_graph, name = 'crypto_graph'),
    
]