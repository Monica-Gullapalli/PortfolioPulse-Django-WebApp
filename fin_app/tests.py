from django.test import TestCase

from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import StockModel, CryptoModel
from .forms import StockForm, CryptoForm
from .views import usignup, ulogin, ulogout, urnp, home, create, delete_stock, view, create_crypto, delete_crypto, view_crypto
from django.test import RequestFactory
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
        
    def test_ulogin_view(self):
        # Create a user for testing authentication
        test_user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        
        # Create a request with session attribute
        request = self.factory.post('/ulogin/', data={'un': 'testuser', 'em': 'test@example.com', 'pw': 'password'})
        request.session = self.client.session
        request.user = test_user

        response = ulogin(request)

        # Check if the user is redirected to the home page upon successful login
        self.assertEqual(response.status_code, 302)
        
        # Check if the response is a redirect
        self.assertTrue(isinstance(response, HttpResponseRedirect))

        # Get the redirect location and check if it matches the expected URL
        redirect_location = response.url
        expected_url = reverse('home')
        self.assertEqual(redirect_location, expected_url)

        # Check if the user is authenticated after login
        self.assertTrue(request.user.is_authenticated)
        
    def test_ulogout_view(self):
        # Create a user for testing logout
        test_user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        
        # Log in the user before testing logout
        self.client.login(username='testuser', password='password')
        
        # Create a request for logging out
        request = self.factory.get('/ulogout/')
        request.user = test_user
        request.session = self.client.session  # Set the session attribute
        
        response = ulogout(request)
        
        # Check if the user is redirected after logout
        self.assertEqual(response.status_code, 302)
        
        # Check if the redirection URL is correct
        self.assertEqual(response.url, reverse('ulogin'))
        
        # Check if the user is no longer authenticated after logout
        self.assertFalse(request.user.is_authenticated)
        
        
    # def test_urnp_view(self):
    #     # Write test cases for the urnp view function
        
    def test_home_view(self):
        # Create a user for testing
        test_user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        
        # Log in the user before accessing the home view
        self.client.login(username='testuser', password='password')
        
        response = self.client.get(reverse('home'))
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the correct template is used for rendering the home view
        self.assertTemplateUsed(response, 'home.html')
                
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

