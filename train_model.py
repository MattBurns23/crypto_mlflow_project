# train_model.py
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from mlflow.models.signature import infer_signature

mlflow.set_tracking_uri("http://mlflow:5000")

# Load cleaned hourly data
df = pd.read_csv("data/btc_hourly_cleaned.csv")

features = ["return_1h", "return_2h", "volume_norm"]
X = df[features].astype("float64")
y = df["label"].astype("float64")

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

# Log to MLflow
input_example = X_test[:1]
signature = infer_signature(X_test, clf.predict(X_test))

with mlflow.start_run():
    mlflow.sklearn.log_model(
        sk_model=clf,
        name="btc_hourly_direction_model",
        input_example=input_example,
        signature=signature
    )
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_param("features", features)
    mlflow.log_param("model_type", "RandomForest")

print(f"Model accuracy: {accuracy:.3f}")

# Predict next hour
latest_features = X.tail(1)
latest_prediction = clf.predict(latest_features)[0]
direction = "UP" if latest_prediction == 1 else "DOWN"
print(f"Latest model prediction: BTC will go {direction} next hour")
