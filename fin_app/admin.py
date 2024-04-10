from django.contrib import admin
from .models import StockModel, CryptoModel

# Register your models here.
admin.site.register(StockModel)
admin.site.register(CryptoModel)