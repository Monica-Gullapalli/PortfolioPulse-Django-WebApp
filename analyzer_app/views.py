import matplotlib
matplotlib.use('Agg')  # Use the Agg backend

import matplotlib.pyplot as plt
import numpy as np
import random
from django.shortcuts import render
from fin_app.models import StockModel, CryptoModel


def stock_graph(request):
    user = request.user
    stocks = StockModel.objects.filter(user=user)

    stock_names = []
    stock_pps = []
    close_prices = []

    for stock in stocks:
        stock_names.append(stock.stock_name)
        stock_pps.append(stock.stock_pps)
        close_prices.append(stock.close_price)

    # Determine the desired size of the plot
    plot_length = len(stock_names) * 0.5  # Adjust the scaling factor as needed

    # Create a figure with the desired size
    fig, ax = plt.subplots(figsize=(6, 6))  # Adjust the height (6) as needed

    # Create an array of indices for the x-axis
    indices = np.arange(len(stock_names))

    # Width of each bar
    bar_width = 0.35

    # Assign light blue color for stock_pps bars
    stock_pps_color = 'lightblue'

    # Assign dark blue color for close price bars
    close_price_color = 'darkblue'

    # Plotting the bars for stock_pps
    ax.bar(indices - bar_width/2, stock_pps, bar_width, color=stock_pps_color, label='Stock PPS')

    # Plotting the bars for close_prices (if available)
    for i in range(len(close_prices)):
        if close_prices[i] is not None:
            ax.bar(indices + bar_width/2, close_prices[i], bar_width, color=close_price_color)

    # Set the x-axis tick labels to be the stock names
    ax.set_xticks(indices)
    ax.set_xticklabels(stock_names, rotation=90)

    ax.set_xlabel('Stock Names')
    ax.set_ylabel('Price')
    ax.set_title('Stock PPS vs Close Price')
    ax.legend(['Stock PPS', 'Close Price'])

    plt.tight_layout()  # Adjust the layout to prevent overlapping of labels

    # Convert the plot to a base64-encoded string
    import io
    import base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_image = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()

    return render(request, 'view_stock_graph.html', {'plot_image': plot_image})


def crypto_graph(request):
    user = request.user
    cryptos = CryptoModel.objects.filter(user=user)

    crypto_names = []
    crypto_ppc = []
    close_prices = []

    for crypto in cryptos:
        crypto_names.append(crypto.crypto_name)
        crypto_ppc.append(crypto.crypto_ppc)
        close_prices.append(crypto.close_price)

    # Determine the desired size of the plot
    plot_length = len(crypto_names) * 0.5  # Adjust the scaling factor as needed

    # Create a figure with the desired size
    fig, ax = plt.subplots(figsize=(6, 6))  # Adjust the height (6) as needed

    # Create an array of indices for the x-axis
    indices = np.arange(len(crypto_names))

    # Width of each bar
    bar_width = 0.35

    # Assign light blue color for stock_pps bars
    stock_pps_color = 'lightblue'

    # Assign dark blue color for close price bars
    close_price_color = 'darkblue'

    # Plotting the bars for stock_pps
    ax.bar(indices - bar_width/2, crypto_ppc, bar_width, color=stock_pps_color, label='Crypto PPC')

    # Plotting the bars for close_prices (if available)
    for i in range(len(close_prices)):
        if close_prices[i] is not None:
            ax.bar(indices + bar_width/2, close_prices[i], bar_width, color=close_price_color)

    # Set the x-axis tick labels to be the stock names
    ax.set_xticks(indices)
    ax.set_xticklabels(crypto_names, rotation=90)

    ax.set_xlabel('Crypto Names')
    ax.set_ylabel('Price')
    ax.set_title('Crypto PPC vs Close Price')
    ax.legend(['Crypto PPC', 'Close Price'])

    plt.tight_layout()  # Adjust the layout to prevent overlapping of labels

    # Convert the plot to a base64-encoded string
    import io
    import base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_image = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()

    return render(request, 'view_crypto_graph.html', {'plot_image': plot_image})