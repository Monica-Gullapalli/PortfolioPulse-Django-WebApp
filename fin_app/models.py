from django.db import models
from django.contrib.auth.models import User

class StockModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_id = models.IntegerField(primary_key=True)
    stock_name = models.CharField(max_length=10000000000)
    stock_number = models.IntegerField()
    stock_money = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stock_name} - {self.stock_number} - {self.stock_money}"
    
    
class CryptoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto_id = models.IntegerField(primary_key=True)
    crypto_name = models.CharField(max_length=10000000000)
    crypto_number = models.IntegerField()
    crypto_money = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crypto_name} - {self.crypto_number} - {self.crypto_money}"


