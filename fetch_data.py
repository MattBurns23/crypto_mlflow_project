# fetch_data.py
import yfinance as yf
import pandas as pd

def fetch_btc_hourly():
    print("Fetching hourly BTC/USD data from Yahoo Finance...")

    # Bitcoin ticker symbol from Yahoo
    btc = yf.Ticker("BTC-USD")

    # Fetch hourly data for the last 7 days
    df = btc.history(interval="1h", period="7d")

    # Reset index to move datetime into a column
    df = df.reset_index()

    # Keep only relevant columns
    df = df[["Datetime", "Open", "High", "Low", "Close", "Volume"]]
    df.columns = ["datetime", "open", "high", "low", "close", "volume"]

    # Save to CSV
    df.to_csv("data/btc_hourly_ohlc.csv", index=False)
    print("✅ Saved hourly BTC data to data/btc_hourly_ohlc.csv")

if __name__ == "__main__":
    fetch_btc_hourly()
