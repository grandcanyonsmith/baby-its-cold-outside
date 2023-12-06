# Python script updated to use human-readable format for dates (e.g., "dec 5 23")
# This code processes historical Tesla (TSLA) stock price data for the past 30 days using yahoo_fin,
# calculates the percentage change, and creates a pandas DataFrame sorted by the change percentage.
# It prefixes positive changes with a plus sign and rounds them to 2 decimals after adding a dollar sign to closing prices.

# Importing necessary libraries
from yahoo_fin import stock_info as si
import pandas as pd
from datetime import datetime, timedelta

# Function to fetch and process historical stock prices
def fetch_process_stock_history(ticker, period="30d"):
    # Calculate start and end dates
    end_date = datetime.now()
    start_date = end_date - timedelta(days=int(period[:-1]))
    # Fetch historical stock data
    stock_data = si.get_data(ticker, start_date=start_date, end_date=end_date)

    # Calculate percentage change from the previous day's closing
    stock_data['prev_close'] = stock_data['close'].shift(1)
    stock_data['percent_change'] = ((stock_data['close'] - stock_data['prev_close']) / stock_data['prev_close']) * 100

    # Convert date index to human-readable format (e.g., "dec 5 23")
    stock_data.index = stock_data.index.strftime('%b %-d %y')
    
    # Round percentage change and closing price to two decimal points
    stock_data = stock_data.round({'percent_change': 2, 'close': 2})
    
    # Format closing price with a dollar sign
    stock_data['close'] = stock_data['close'].apply(lambda x: f'${x}')
    # Format percentage change with a plus sign for positive changes
    stock_data['percent_change'] = stock_data['percent_change'].apply(lambda x: f'+{x}%' if x > 0 else f'{x}%')
    
    # Select and reorder relevant columns
    stock_data = stock_data[['close', 'percent_change']]
    
    # Sort data by percentage change in descending order
    sorted_stock_data = stock_data.sort_values('percent_change', ascending=False)
    
    return sorted_stock_data

# Main function to drive the processing of stock data
def main():
    # Define the ticker symbol for Tesla
    ticker_symbol = 'TSLA'
    
    # Get and process Tesla stock prices for the past 30 days
    processed_tesla_data = fetch_process_stock_history(ticker_symbol)

    # Display the processed and sorted stock data
    print(processed_tesla_data)

# Check if the script is run as the main program
if __name__ == "__main__":
    main()