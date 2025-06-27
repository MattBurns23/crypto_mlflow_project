# 🪙 Bitcoin Price Movement Prediction (Hourly) – MLflow + Docker

This project uses **Docker and MLflow** to build a full machine learning pipeline that predicts whether Bitcoin's price will go UP or DOWN in the next hour based on historical OHLC data.

Everything runs in **containers** — data fetching, preprocessing, model training, and experiment tracking. No API keys needed. Just clone, run Docker, and go.
This project predicts the hourly price movement of Bitcoin (BTC/USD) using historical OHLC data fetched from Yahoo Finance. The pipeline includes data fetching, preprocessing, model training with MLflow logging, and future movement prediction.

---

## 📦 Features
- Fetches hourly OHLC data from Yahoo Finance (no API key needed)
- Cleans and processes data for ML model training
- Trains a Random Forest classifier to predict next-hour BTC direction
- Logs model metrics and artifacts using MLflow
- Dockerized workflow for scalable and reproducible experiments

---

## 📁 Project Structure

```
crypto_mlflow_project/
├── data/                         # Local CSV data files
│   └── btc_hourly_ohlc.csv
│   └── btc_hourly_cleaned.csv
├── mlruns/                       # MLflow logs and models
├── fetch_data.py                 # Fetches hourly BTC data from Yahoo Finance
├── clean_data.py                 # Cleans and processes the data
├── train_model.py                # Trains model, logs to MLflow, prints prediction
├── Dockerfile.mlflow             # MLflow tracking server Dockerfile
├── Dockerfile.fetcher            # Dockerfile for fetch_data.py
├── Dockerfile.cleaner            # Dockerfile for clean_data.py
├── Dockerfile.training           # Dockerfile for train_model.py
├── docker-compose.yml            # Orchestrates the services
└── README.txt                    # This file
```

---

## ⚙️ How It Works

1. **Fetch Hourly BTC Data**
   - Source: Yahoo Finance (no API key required)
   - Output: `data/btc_hourly_ohlc.csv`

2. **Clean and Feature Engineer**
   - Adds returns, normalized volume, and a directional label.
   - Output: `data/btc_hourly_cleaned.csv`

3. **Train Model**
   - Uses a RandomForestClassifier to predict whether BTC will go UP or DOWN next hour.
   - Logs metrics and model to MLflow.
   - Prints the latest prediction.

---

## 🐳 Run with Docker

1. **Build and Start All Services**  
```bash
docker-compose up --build
```
- This spins up **3 containers**:
  - `fetcher` – downloads hourly BTC OHLC data from Yahoo
  - `cleaner` – preprocesses the data into model-ready format
  - `trainer` – trains a RandomForest model and logs it to MLflow

2. **Access MLflow UI**  
- Visit MLflow UI at: [http://localhost:5000](http://localhost:5000)

---

## ✅ Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

**requirements.txt**
```
pandas
requests
scikit-learn
mlflow
yfinance
```

---

## 🧠 Model

- **Algorithm**: RandomForestClassifier
- **Features**: 1h return, 2h return, normalized volume
- **Target**: Binary direction (1 = UP, 0 = DOWN)
- **MLflow logging**: model, accuracy metric, and parameters

---


## 📈 Output Example

After training, you'll see something like:

```
Model accuracy: 0.622  
Latest model prediction: BTC will go DOWN next hour
```

---

## 🧼 Notes

- No API keys needed — uses Yahoo Finance
- MLflow logs are stored in the `mlruns/` folder by default
- Customize Dockerfiles if switching exchanges, features, or models