from django.db import models
from django.contrib.auth.models import User
import yfinance as yf
import yfinance as yf
from django import template

register = template.Library()



from django.db import models
from django.contrib.auth.models import User
import yfinance as yf

class StockModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_id = models.AutoField(primary_key=True)
    stock_name = models.CharField(max_length=255)
    stock_number = models.IntegerField(null=True)  # Allow null values for stock_number
    stock_pps = models.FloatField(default=0.0)
    stock_money = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    close_price = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        if self.stock_number is not None and self.stock_pps is not None:
            self.stock_money = self.stock_number * self.stock_pps
        elif self.stock_name and not self.close_price:
            self.update_close_price()
        super().save(*args, **kwargs)

    def update_close_price(self):
        try:
            stock = yf.Ticker(self.stock_name)
            data = stock.history(period="1d")
            if not data.empty:
                self.close_price = data['Close'].iloc[-1]
        except Exception as e:
            print(f"Error retrieving data for ticker '{self.stock_name}': {e}")

    def __str__(self):
        return f"{self.stock_name} - {self.stock_number} - {self.stock_pps} - {self.stock_money}"
    
class CryptoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto_id = models.IntegerField(primary_key=True)
    crypto_name = models.CharField(max_length=255)  # Adjust length as needed
    crypto_number = models.IntegerField()
    crypto_ppc = models.FloatField(default=0.0)
    crypto_money = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    close_price = models.FloatField(default=0.0)  # New field to store close price

    def save(self, *args, **kwargs):
        self.crypto_money = self.crypto_number * self.crypto_ppc
        if self.crypto_name and not self.close_price:
            self.update_close_price()
        super().save(*args, **kwargs)

    def update_close_price(self):
        try:
            crypto = yf.Ticker(self.crypto_name)
            data = crypto.history(period="30d")
            if not data.empty:
                self.close_price = data['Close'].iloc[-1]
        except Exception as e:
            print(f"Error retrieving data for ticker '{self.crypto_name}': {e}")

    def __str__(self):
        return f"{self.crypto_name} - {self.crypto_number} - {self.crypto_ppc} - {self.crypto_money}"
