from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import StockModel, CryptoModel
from .forms import StockForm, CryptoForm
from .views import usignup, ulogin, ulogout, urnp, home, create, delete_stock, view, create_crypto, delete_crypto, view_crypto
from django.test import RequestFactory

class FinAppViewsTestCase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        
    def test_usignup_view(self):
        request = self.factory.post('/usignup/', data={'un': 'testuser', 'em': 'test@example.com', 'pw1': 'password', 'pw2': 'password'})
        response = usignup(request)
        self.assertEqual(response.status_code, 302)  # Check if the user is redirected after signup
        
        # Add more assertions based on the expected behavior of the view
        
    # def test_ulogin_view(self):
    #     # Write test cases for the ulogin view function
        
    # def test_ulogout_view(self):
    #     # Write test cases for the ulogout view function
        
    # def test_urnp_view(self):
    #     # Write test cases for the urnp view function
        
    # def test_home_view(self):
    #     # Write test cases for the home view function
        
    # def test_create_view(self):
    #     # Write test cases for the create view function
        
    # def test_delete_stock_view(self):
    #     # Write test cases for the delete_stock view function
        
    # def test_view_view(self):
    #     # Write test cases for the view view function
        
    # def test_create_crypto_view(self):
    #     # Write test cases for the create_crypto view function
        
    # def test_delete_crypto_view(self):
    #     # Write test cases for the delete_crypto view function
        
    # def test_view_crypto_view(self):
    #     # Write test cases for the view_crypto view function

