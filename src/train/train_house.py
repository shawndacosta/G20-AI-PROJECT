import os
import time
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from lightgbm import LGBMRegressor

def evaluate(model, X_test, y_test):
    p = model.predict(X_test)
    mae = mean_absolute_error(y_test, p)
    rmse = mean_squared_error(y_test, p) ** 0.5
    r2 = r2_score(y_test, p)
    return mae, rmse, r2

def train_house(base_dir):
    data_path = os.path.join(base_dir, "data", "cleaned", "cleaned_house.csv")
    model_dir = os.path.join(base_dir, "models")
    os.makedirs(model_dir, exist_ok=True)

    df = pd.read_csv(data_path)

    features = ["bed", "bath", "acre_lot", "city_encoded",
                "state_encoded", "zip_code", "house_size"]

    X = df[features]
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "LinearRegression": LinearRegression(),
        "RandomForest_small": RandomForestRegressor(
            n_estimators=150, max_depth=20, n_jobs=-1
        ),
        "LightGBM": LGBMRegressor(
            n_estimators=400, learning_rate=0.05,
            num_leaves=64, subsample=0.8,
            colsample_bytree=0.8, n_jobs=-1
        )
    }

    results = {}

    for name, model in models.items():
        print("\n--- Training", name, "---")
        start = time.time()
        model.fit(X_train, y_train)
        mae, rmse, r2 = evaluate(model, X_test, y_test)
        results[name] = {
            "MAE": mae,
            "RMSE": rmse,
            "R2": r2,
            "Train_time": time.time() - start
        }
        print(f"{name}: MAE={mae:.2f} | RMSE={rmse:.2f} | R2={r2:.4f}")

    best_name = min(results, key=lambda x: results[x]["MAE"])
    best_model = models[best_name]

    save_path = os.path.join(model_dir, "house_best_model.pkl")
    with open(save_path, "wb") as f:
        pickle.dump({"model": best_model, "features": features}, f)

    return results, best_name, save_path
