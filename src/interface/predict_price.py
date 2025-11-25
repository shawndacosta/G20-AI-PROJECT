import os, pickle
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
CLEAN_PATH = os.path.join(BASE_DIR, "data", "cleaned", "cleaned_house.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "house_best_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "models", "house_encoder.pkl")
LOOKUP_PATH = os.path.join(BASE_DIR, "data", "cleaned", "city_state_lookup.csv")


class PricePredictor:
    def __init__(self):
        self.df = pd.read_csv(CLEAN_PATH)

        # Load model
        with open(MODEL_PATH, "rb") as f:
            obj = pickle.load(f)

        if isinstance(obj, dict):
            self.model = obj["model"]
            self.features = obj["features"]
        else:
            self.model = obj
            self.features = ["bed", "bath", "acre_lot", "city_encoded",
                             "state_encoded", "zip_code", "house_size"]

        # Load encoder
        with open(ENCODER_PATH, "rb") as f:
            enc = pickle.load(f)

        self.state_to_id = enc["state_to_id"]
        self.city_to_encoded = enc["city_to_encoded"]

        # Lookup table for UI
        self.lookup = pd.read_csv(LOOKUP_PATH)
        self.states = sorted(self.lookup["state"].unique().tolist())

    # ------------------ UI HELPERS ------------------

    def cities_for_state(self, state):
        m = self.lookup["state"] == state
        return sorted(self.lookup.loc[m, "city"].unique().tolist())

    def zips_for_state_city(self, state, city):
        m = (self.lookup["state"] == state) & (self.lookup["city"] == city)
        return sorted(self.lookup.loc[m, "zip_code"].unique().tolist())

    # ------------------ ENCODERS ------------------

    def encode_state(self, state):
        return self.state_to_id.get(state, 0)

    def encode_city(self, city):
        return self.city_to_encoded.get(
            city,
            float(self.df["city_encoded"].mean())
        )

    # ------------------ PREDICTION ------------------

    def predict(self, bed, bath, acre_lot, city, state, zip_code, house_size):

        # Build input
        row = pd.DataFrame([[
            bed,
            bath,
            acre_lot,
            self.encode_city(city),
            self.encode_state(state),
            zip_code,
            house_size
        ]], columns=self.features)

        # Predict price
        y_pred = float(self.model.predict(row)[0])

        # Compute accuracy from dataset
        m = (
            (self.df["state_encoded"] == self.encode_state(state)) &
            (self.df["city_encoded"] == self.encode_city(city)) &
            (self.df["zip_code"] == zip_code)
        )

        local_data = self.df.loc[m, "price"]

        if len(local_data) == 0:
            accuracy = 50.0  # default fallback
        else:
            real_mean = float(local_data.mean())
            rel_error = abs(real_mean - y_pred) / real_mean
            accuracy = max(0, 100 * (1 - rel_error))

        return y_pred, accuracy
