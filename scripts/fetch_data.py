import yfinance as yf
import pandas as pd

#define assets
tickers = ['AAPL', 'MSFT', 'TSLA']

#download data
data = yf.download(tickers,
                   start='2020-01-01',
                   end='2025-01-01',
                   auto_adjust=False,
                   progress=False)

#Save adjusted close prices to csv
adj_close = data['Adj Close']  # This will give you a DataFrame with AAPL, MSFT, TSLA columns
adj_close.to_csv('data/asset_prices.csv')


print("Data Saved to data/asset_prices.csv")