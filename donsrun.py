import yfinance as yf 
import pandas as pd 
import matplotlib.pyplot as plt
# Define the ticker symbol for the Dow Jones Industrial Average
ticker_symbol = '^DJI'
# Retrieve historical data for the past two years
data = yf.download(ticker_symbol, start='2022-08-16', end='2024-08-16')
# Calculate the daily percent change
data['Percent Change'] = data['Adj Close'].pct_change () * 100
# Drop the first row since it will have
# NaN values due to the pot_change calculation
data = data.dropna()
# Plot the daily percent change
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Percent Change'], color='blue', lw=0.75)
plt.title('Daily Percent Change of the Dow Jones Industrial Average (Past 2 Years) ')
plt.xlabel('Date')
plt.ylabel('Percent Change (%) ')
plt.grid (True)
plt.show()