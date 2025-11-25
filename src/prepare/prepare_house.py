import os
import pandas as pd
import pickle


def prepare_house(base_dir: str):
    raw_path = os.path.join(base_dir, "data", "raw", "realtor-data.zip.csv")
    cleaned_dir = os.path.join(base_dir, "data", "cleaned")
    models_dir = os.path.join(base_dir, "models")
    os.makedirs(cleaned_dir, exist_ok=True)
    os.makedirs(models_dir, exist_ok=True)

    df = pd.read_csv(raw_path)

    cols = ["price", "bed", "bath", "acre_lot", "city", "state", "zip_code", "house_size"]
    df = df[cols]

    df = df.dropna()

    df = df[(df["price"] > 10000) & (df["price"] < 5_000_000)]
    df = df[(df["bed"] >= 1) & (df["bed"] <= 15)]
    df = df[(df["bath"] >= 1) & (df["bath"] <= 15)]
    df = df[(df["acre_lot"] >= 0) & (df["acre_lot"] < 50)]
    df = df[(df["house_size"] >= 100) & (df["house_size"] <= 10000)]

    df["zip_code"] = df["zip_code"].astype(int)

    states = sorted(df["state"].unique())
    state_to_id = {s: i for i, s in enumerate(states)}
    df["state_encoded"] = df["state"].map(state_to_id).astype(int)

    city_mean_price = df.groupby("city")["price"].mean()
    city_to_encoded = city_mean_price.to_dict()
    df["city_encoded"] = df["city"].map(city_to_encoded)

    df_final = df[[
        "price",
        "bed",
        "bath",
        "acre_lot",
        "city_encoded",
        "state_encoded",
        "zip_code",
        "house_size"
    ]].copy()

    cleaned_path = os.path.join(cleaned_dir, "cleaned_house.csv")
    df_final.to_csv(cleaned_path, index=False)

    encoder = {
        "state_to_id": state_to_id,
        "city_to_encoded": city_to_encoded
    }
    enc_path = os.path.join(models_dir, "house_encoder.pkl")
    with open(enc_path, "wb") as f:
        pickle.dump(encoder, f)

    return df_final.shape, cleaned_path, enc_path
