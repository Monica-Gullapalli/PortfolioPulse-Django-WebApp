from django.db import models
from django.contrib.auth.models import User
import yfinance as yf

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
    created = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.crypto_money = self.crypto_number * self.crypto_ppc
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.crypto_name} - {self.crypto_number} - {self.crypto_ppc} -  {self.crypto_money}"