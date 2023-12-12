from yahoo_fin import stock_info as si
import pandas as pd
from datetime import datetime, timedelta

# Function to format the percentage change
def format_change(change):
    sign = "+" if change > 0 else ""
    return f"{sign}{change:.2f}%"

# Function to format the closing price
def format_price(price):
    return f"${price:.2f}"

# Function to fetch and process the stock price data
def get_stock_data(ticker, days="30d"):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=int(days[:-1]))
    data = si.get_data(ticker, start_date=start_date, end_date=end_date)
    
    # Calculate the changes
    data['percent_change'] = data['close'].pct_change() * 100
    
    # Apply formatting to closing price and percentage change
    data['close'] = data['close'].map(format_price)
    data['percent_change'] = data['percent_change'].map(format_change)
    
    # Format the date index and select relevant columns
    data.index = data.index.strftime('%b %d, %Y')
    data = data[['close', 'percent_change']]
    
    # Sort the DataFrame by percentage change in descending order
    return data.sort_values('percent_change', ascending=False)

def main():
    ticker = 'TSLA'
    tesla_data = get_stock_data(ticker)
    print(tesla_data)

if __name__ == "__main__":
    main()