from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from fin_app.models import StockModel
from .views import stock_graph

class StockGraphViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='monicagullapalli', password='1234')

    def test_stock_graph_no_stocks(self):
        # Test case: No stocks available
        request = self.factory.get('/stock-graph/')
        request.user = self.user
        response = stock_graph(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Stock A')
        self.assertNotContains(response, '100.0')
        self.assertNotContains(response, '150.0')

    # def test_stock_graph_one_stock(self):
    #     # Test case: One stock with close price available
    #     stock = StockModel.objects.create(user=self.user, stock_name='Stock A', stock_pps=100.0, close_price=150.0)
    #     request = self.factory.get('/stock-graph/')
    #     request.user = self.user
    #     response = stock_graph(request)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, stock.stock_name)
    #     self.assertContains(response, str(stock.stock_pps))
    #     self.assertContains(response, str(stock.close_price))

    # def test_stock_graph_multiple_stocks(self):
    #     # Test case: Multiple stocks with close prices available
    #     stocks = [
    #         StockModel.objects.create(user=self.user, stock_name='Stock A', stock_pps=100.0, close_price=150.0),
    #         StockModel.objects.create(user=self.user, stock_name='Stock B', stock_pps=200.0, close_price=250.0),
    #         StockModel.objects.create(user=self.user, stock_name='Stock C', stock_pps=300.0, close_price=350.0),
    #     ]
    #     request = self.factory.get('/stock-graph/')
    #     request.user = self.user
    #     response = stock_graph(request)
    #     self.assertEqual(response.status_code, 200)
    #     for stock in stocks:
    #         self.assertContains(response, stock.stock_name)
    #         self.assertContains(response, str(stock.stock_pps))
    #         self.assertContains(response, str(stock.close_price))

    # def test_invalid_user_access(self):
    #     # Test case: User without access trying to view the stock graph
    #     unauthorized_user = User.objects.create_user(username='unauthorized_user', password='5678')
    #     request = self.factory.get('/stock-graph/')
    #     request.user = unauthorized_user
    #     response = stock_graph(request)
    #     self.assertEqual(response.status_code, 403)  # Expecting a forbidden access response

    def test_invalid_stock_data(self):
        # Test case: Creating a stock with invalid data
        invalid_stock = StockModel.objects.create(user=self.user, stock_name='Invalid Stock', stock_pps=-10.0, close_price=50.0)
        request = self.factory.get('/stock-graph/')
        request.user = self.user
        response = stock_graph(request)
        self.assertNotContains(response, invalid_stock.stock_name)  # Expecting the invalid stock not to be displayed
