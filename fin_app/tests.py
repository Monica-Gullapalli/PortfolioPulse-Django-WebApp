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
                
    def test_create_view(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client.force_login(user)

        response = self.client.post(reverse('create'), {
            'stock_name': 'Test Stock',
            'stock_number': 10,
            'stock_pps': 100.00,
    })

        self.assertEqual(response.status_code, 200)  # Assuming successful creation returns HTTP 200

    # Print the response content for debugging
        print(response.content.decode())

    # Retrieve the created StockModel object and check its existence
        stock = StockModel.objects.filter(stock_name='Test Stock').first()
        self.assertIsNotNone(stock)
        
        
    # def test_delete_stock_view(self):
    # # Create a stock for testing
    #     stock = StockModel.objects.create(stock_name='Test Stock', stock_number=10, stock_pps=100.00)

    # # Ensure the stock exists before deletion
    #     stock_exists = StockModel.objects.filter(stock_name='Test Stock').exists()
    #     self.assertTrue(stock_exists)

    # # Get the URL for the delete_stock view using the stock ID
    #     url = reverse('delete', args=[stock.id])

    # # Send a POST request to delete the stock
    #     response = self.client.post(url)

    # # Check that the stock is deleted
    #     stock_exists = StockModel.objects.filter(stock_name='Test Stock').exists()
    #     self.assertFalse(stock_exists)

    # # Check the response status code and redirect
    #     self.assertEqual(response.status_code, 302)  # Assuming successful deletion redirects with HTTP 302
    #     self.assertRedirects(response, reverse('home'))  # Assuming successful deletion redirects to the home page
    
  
    def test_view_view(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client.force_login(user)
        
        response = self.client.get(reverse('view'))
        
        self.assertEqual(response.status_code, 200)  # Assuming successful view returns HTTP 200
        self.assertTemplateUsed(response, 'view.html')  # Assuming the template used is 'vi
        
    def test_create_crypto_view(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client.force_login(user)
        
        response = self.client.post(reverse('create_crypto'), {
            'crypto_name': 'Test Crypto',
            'quantity': 1.5,
            'price': 5000.00,
        })
        
        self.assertEqual(response.status_code, 200)  # Assuming successful creation returns HTTP 200
        
        # Print the response content for debugging
        print(response.content.decode())
        
        # Retrieve the created CryptoModel object and check its existence
        crypto = CryptoModel.objects.filter(crypto_name='Test Crypto').first()
        
        # Check if the CryptoModel object is created successfully
        self.assertIsNotNone(crypto, "CryptoModel object with name 'Test Crypto' should exist in the database")
        
        # Additional assertions for specific attributes of the created CryptoModel object
        self.assertEqual(crypto.quantity, 1.5, "Quantity should be 1.5")
        self.assertEqual(crypto.price, 5000.00, "Price should be 5000.00")
        
    
                  
    # def test_delete_crypto_view(self):
    #     # Write test cases for the delete_crypto view function
        
    # def test_view_crypto_view(self):
    #     # Write test cases for the view_crypto view function

