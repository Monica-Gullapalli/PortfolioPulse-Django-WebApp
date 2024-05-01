from django.db import models
from django.contrib.auth.models import User
import yfinance as yf
import yfinance as yf
from django import template


register = template.Library()



# models.py

from django.db import models
from django.contrib.auth.models import User
import yfinance as yf
import redis
import json

class StockModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_id = models.IntegerField(primary_key=True)
    stock_name = models.CharField(max_length=10000000000)
    stock_number = models.IntegerField()
    stock_pps = models.FloatField(default=0.0)
    stock_money = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    close_price = models.FloatField(default=0.0)  # New field to store close price

    def save(self, *args, **kwargs):
        self.stock_money = self.stock_number * self.stock_pps
        if self.stock_name and not self.close_price:
            # Retrieve and update close price if it's not set
            try:
                stock = yf.Ticker(self.stock_name)
                data = stock.history(period="1d")
                if not data.empty:
                    self.close_price = data['Close'].iloc[-1]
            except Exception as e:
                print(f"Error retrieving data for ticker '{self.stock_name}': {e}")
        elif self.stock_name and self.close_price:
            # Update close price if it's already set
            try:
                stock = yf.Ticker(self.stock_name)
                data = stock.history(period="1d")
                if not data.empty:
                    updated_close_price = data['Close'].iloc[-1]
                    if self.close_price != updated_close_price:
                        self.close_price = updated_close_price
            except Exception as e:
                print(f"Error retrieving data for ticker '{self.stock_name}': {e}")
        
        r = redis.Redis(host='localhost', port=6379, db=0)
        form_data = {
           'stock_name': self.stock_name,
           'stock_number': self.stock_number,
           'stock_pps': self.stock_pps,
           'stock_money': self.stock_money,
           'close_price': self.close_price,
       }
        r.set(f'{self.__class__.__name__}_{self.pk}', json.dumps(form_data))
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.stock_name} - {self.stock_number} - {self.stock_pps} - {self.stock_money}"


class CryptoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto_id = models.IntegerField(primary_key=True)
    crypto_name = models.CharField(max_length=10000000000)
    crypto_number = models.IntegerField()
    crypto_ppc = models.FloatField(default=0.0)
    crypto_money = models.FloatField(default = 0.0)
    crypto_money = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)

    close_price = models.FloatField(default=0.0)  # New field to store close price

    def save(self, *args, **kwargs):
        self.crypto_money = self.crypto_number * self.crypto_ppc
        if self.crypto_name and not self.close_price:
            # Retrieve and update close price if it's not set
            try:
                crypto = yf.Ticker(self.crypto_name)
                data = crypto.history(period="30d")
                if not data.empty:
                    self.close_price = data['Close'].iloc[-1]
            except Exception as e:
                print(f"Error retrieving data for ticker '{self.crypto_name}': {e}")
        elif self.crypto_name and self.close_price:
            # Update close price if it's already set
            try:
                crypto = yf.Ticker(self.crypto_name)
                data = crypto.history(period="30d")
                if not data.empty:
                    updated_close_price = data['Close'].iloc[-1]
                    if self.close_price != updated_close_price:
                        self.close_price = updated_close_price
            except Exception as e:
                print(f"Error retrieving data for ticker '{self.crypto_name}': {e}")
        r = redis.Redis(host='localhost', port=6379, db=0)
        form_data = {
           'crypto_name': self.crypto_name,
           'crypto_number': self.crypto_number,
           'crypto_ppc': self.crypto_ppc,
           'crypto_money': self.crypto_money,
           'close_price': self.close_price,
       }
        r.set(f'{self.__class__.__name__}_{self.pk}', json.dumps(form_data))
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.crypto_name} - {self.crypto_number} - {self.crypto_ppc} - {self.crypto_money}"
