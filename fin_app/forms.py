from django import forms
from .models import StockModel, CryptoModel


class StockForm(forms.ModelForm):
	class Meta:
		model = StockModel
		fields = ['stock_name', 'stock_number','stock_pps']


class CryptoForm(forms.ModelForm):
	class Meta:
		model = CryptoModel
		fields = ['crypto_name', 'crypto_number', 'crypto_ppc']

