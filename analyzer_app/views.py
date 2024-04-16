import matplotlib
matplotlib.use('Agg')  # Set the backend to 'Agg' before importing pyplot
import matplotlib.pyplot as plt
from django.shortcuts import render, redirect
from fin_app.models import StockModel
import yfinance as yf
import io
import urllib, base64

def plot_graph(request):
    stocks = StockModel.objects.all()  # Get all stock entries from the database

    stock_pps = []
    close_prices = []

    for stock in stocks:
        stock_pps.append(stock.stock_pps)
        ticker = yf.Ticker(stock.stock_name)  # Create a Ticker object with the stock name
        history = ticker.history(period="1d")  # Fetch the historical data for the stock
        if not history.empty:
            close_price = history["Close"].iloc[-1]  # Get the most recent close price
            close_prices.append(close_price)

    # Check if the dimensions of stock_pps and close_prices are equal
    if len(stock_pps) != len(close_prices):
        # Handle the case where dimensions are not equal, e.g., by truncating one of the lists to match the shorter one
        min_length = min(len(stock_pps), len(close_prices))
        stock_pps = stock_pps[:min_length]
        close_prices = close_prices[:min_length]

    # Plot the graph
    plt.plot(stock_pps, close_prices, 'o')
    plt.xlabel('Stock Price per Share ($)')
    plt.ylabel('Close Price ($)')
    plt.title('Stock Price per Share vs Close Price')
    plt.grid(True)

    # Save the plot to a file
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graph = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'view_stock_graph.html', {'graph': graph})


 # Create a corresponding HTML template for the graph
    
# matplotlib.use('TkAgg')

# # Create your views here.
# import matplotlib.pyplot as plt
# from fin_app.models import StockModel
# from collector_app.templatetags.yfinance_tags import load_yfinance_data
# from django.shortcuts import render


# from io import BytesIO
# import base64

# from django.http import HttpResponse
# from django.template import loader
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer

# def plot_graph(request):
#     user = request.user
#     stocks = StockModel.objects.filter(user=user)

#     stock_pps_values = [stock.stock_pps for stock in stocks]
#     close_price_values = [float(load_yfinance_data(stock.stock_name)) if load_yfinance_data(stock.stock_name) is not None else 0.0 for stock in stocks]

#     plt.plot(stock_pps_values, close_price_values)
#     plt.xlabel('Stock PPS')
#     plt.ylabel('Close Price')
#     plt.title('Stock PPS vs. Close Price')

#     # Save the plot as a PNG image
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
#     plt.close()  # Close the plot to release resources

#     template = loader.get_template('view_stock_graph.html')
#     context = {'image_base64': image_base64}
#     html_content = template.render(context, request)

#     # Send the rendered HTML content back to the client
#     return HttpResponse(html_content)