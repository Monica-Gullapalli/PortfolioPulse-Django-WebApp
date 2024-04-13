# import matplotlib
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