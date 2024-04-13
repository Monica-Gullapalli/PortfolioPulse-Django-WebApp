from django import template
import yfinance as yf

register = template.Library()

@register.simple_tag
def load_yfinance_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        if not data.empty:
            close_price = data['Close'].iloc[-1]
            return float(close_price)
    except Exception as e:
        print(f"Error retrieving data for ticker '{ticker}': {e}")
    return None

@register.simple_tag
def load_yfinance_data(ticker):
    try:
        crypto = yf.Ticker(ticker)
        data = crypto.history(period="30d")
        if not data.empty:
            close_price = data['Close'].iloc[-1]
            return close_price
    except Exception as e:
        print(f"Error retrieving data for ticker '{ticker}': {e}")
    return None