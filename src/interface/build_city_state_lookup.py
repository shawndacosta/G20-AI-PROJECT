import os, pickle
import pandas as pd

def build_city_state_lookup(base_dir):
    raw_path = os.path.join(base_dir, "data", "raw", "realtor-data.zip.csv")
    enc_path = os.path.join(base_dir, "models", "house_encoder.pkl")
    out_path = os.path.join(base_dir, "data", "cleaned", "city_state_lookup.csv")

    df = pd.read_csv(raw_path, usecols=["city", "state", "zip_code"])
    df = df.dropna(subset=["city", "state", "zip_code"])
    df["zip_code"] = df["zip_code"].astype(int)
    df = df.drop_duplicates(subset=["state", "city", "zip_code"])

    with open(enc_path, "rb") as f:
        enc = pickle.load(f)
    state_to_id = enc["state_to_id"]
    city_to_encoded = enc["city_to_encoded"]

    df["state_encoded"] = df["state"].map(state_to_id)
    df["city_encoded"] = df["city"].map(city_to_encoded)
    df = df.dropna(subset=["state_encoded", "city_encoded"])

    df.to_csv(out_path, index=False)
    return df.shape, out_path
