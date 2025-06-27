# clean_data.py
import pandas as pd

def clean_hourly_data():
    df = pd.read_csv("data/btc_hourly_ohlc.csv")

    # Rename for consistency
    df.rename(columns={
        "close": "price",
        "volume": "volume_24h"
    }, inplace=True)

    # Create hourly percent changes
    df["price_shift_1"] = df["price"].shift(1)
    df["price_shift_2"] = df["price"].shift(2)
    df["return_1h"] = (df["price"] - df["price_shift_1"]) / df["price_shift_1"]
    df["return_2h"] = (df["price_shift_1"] - df["price_shift_2"]) / df["price_shift_2"]
    df["volume_norm"] = (df["volume_24h"] - df["volume_24h"].mean()) / df["volume_24h"].std()

    # Label: 1 if price goes up next hour
    df["future_price"] = df["price"].shift(-1)
    df["label"] = (df["future_price"] > df["price"]).astype(int)

    df = df.dropna().reset_index(drop=True)
    df.to_csv("data/btc_hourly_cleaned.csv", index=False)
    print("✅ Cleaned data saved to data/btc_hourly_cleaned.csv")

if __name__ == "__main__":
    clean_hourly_data()
