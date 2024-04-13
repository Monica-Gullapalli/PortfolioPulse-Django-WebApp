from django.db import models
from django.contrib.auth.models import User

class StockModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_id = models.IntegerField(primary_key=True)
    stock_name = models.CharField(max_length=10000000000)
    stock_number = models.IntegerField()
    stock_pps = models.FloatField(default=0.0)
    stock_money = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.stock_money = self.stock_number * self.stock_pps
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