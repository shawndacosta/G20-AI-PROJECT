# 📘 Installation & Setup Guide  
AI-Powered House Price Prediction System  

This guide explains **exactly how to install, organize, and run the entire project**, from dataset download to model training and interface usage.  
Follow the steps carefully to reproduce the full workflow.

---

# 📂 1. Project Structure

Create the following folder structure **manually** on your computer:

your_project/
│
├── data/
│ ├── raw/
│ └── cleaned/
│
├── models/
│
├── notebooks/
│ ├── 01-project-init.ipynb
│ ├── 02-data-preparation.ipynb
│ ├── 03-train-models.ipynb
│ ├── 04-test-model.ipynb
│ ├── 05-interface.ipynb
│
├── src/
│ ├── prepare/
│ │ └── prepare_house.py
│ ├── train/
│ │ └── train_house.py
│ └── interface/
│ ├── predict_price.py
│ └── build_city_state_lookup.py


✔️ All these files exist in the GitHub repository.  
You only need to **recreate the same folders** and **place each file in the correct folder**.

---

# 🔽 2. Download the Dataset

Download the dataset from Kaggle:

➡️ **https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset**

You will obtain a file named something like:

  realtor-data.zip

Extract its content, and place the resulting CSV into:

  your_project/data/raw/

🎯 Expected final file:

  data/raw/realtor-data.csv  


(If your file name ends differently, simply update the notebook path accordingly.)

---

# ⚙️ 3. Install Dependencies

Create a new Python environment using VS Code or Anaconda:

  conda create -n house_env python=3.10
  conda activate house_env

Then install the required libraries:

  pip install numpy pandas scikit-learn lightgbm ipywidgets matplotlib

Enable widgets inside Jupyter:

  jupyter nbextension enable --py widgetsnbextension

# 🛠️ 4. Update Base Path in Every Notebook & Script

Every notebook begins with:

  base = r"C:\Users\YOUR_NAME\...\house_prediction"

You must update this path to your own project folder.

The same applies to Python scripts inside src/.

# 🧹 5. Prepare the Dataset (Notebook 02)

Run:
  notebooks/02-data-preparation.ipynb






