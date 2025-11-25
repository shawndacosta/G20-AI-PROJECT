# Models Folder

This folder contains the machine learning models used for house price prediction.

⚠️ Due to GitHub's file size limits, the trained models cannot be uploaded directly.

## How to regenerate the models

1. Make sure the cleaned dataset is present in:
     data/cleaned/cleaned_house.csv

2. Run the training notebook:
     notebooks/2-train-model.ipynb

3. At the end of the training script, two files will be generated automatically:
    - `house_best_model.pkl`
    - `house_encoder.pkl`

Place the generated files in this folder:
    models/


## Files expected in this directory

- `house_best_model.pkl` — Best performing model (RandomForest)
- `house_encoder.pkl` — Encoders for state and city

These files are required to run:
src/interface/predict_price.py


If they are missing, simply retrain the model using the training notebook.




