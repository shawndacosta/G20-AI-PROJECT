# 🏡 AI Powered House Price Prediction System

## Members:
 - ADNANI Sirine, Computer Science, ECE Paris, sirine.adnani@edu.ece.fr
 - DA COSTA Shawn, Computer Science, Ece Paris, shawn.dacosta@edu.ece.fr
 - OUBOUSSAD Camille-Lina, Computer Science, ECE Paris, camillelina.ouboussad@edu.ece.fr

# Predicting real estate prices using machine learning

This project aims to design an AI-powered system capable of estimating the market value of houses across the United States using historical real estate data. Based on a machine learning model trained on a large dataset of property listings, the system predicts selling prices from key characteristics such as location, house size, number of bedrooms, number of bathrooms, and land area.

The system uses AI techniques within an interactive interface where the user can select the state, city, ZIP code, and property features through a guided menu. Once the inputs are provided, the program summarizes the selected property profile and delivers a predicted price along with a local accuracy score computed from similar houses in the same area.

This prototype demonstrates how artificial intelligence can enhance decision-making in the real estate sector by transforming extensive housing data into a clear, accessible, and intelligent prediction tool.

# 📑 Table of Contents

1. [Introduction](#i-introduction)
2. [Datasets](#ii-datasets)
3. [Methodology](#iii-methodology)
4. [Evaluation & Analysis](#iv-evaluation--analysis)
5. [Related Work](#v-related-work)
6. [Conclusion](#vi-conclusion)

# I. Introduction 

## 🎯 Motivation

Estimating the market value of a house is a central challenge in real estate. Prices fluctuate depending on location, property characteristics, and evolving market trends. For buyers, sellers, and professionals, having a quick and reliable estimation tool can significantly improve decision-making.

Our motivation was to design an accessible AI-powered system capable of predicting house prices across the United States using historical real estate data. By relying on machine learning, the system can capture hidden patterns in property listings and provide consistent estimations, even in regions where prices vary widely.

## 🎯 Objective

The goal of this project is to develop:

- A *cleaned and structured dataset* from large-scale real estate data  
- A *machine learning model* capable of predicting house prices  
- An *interactive interface* where the user selects:
  - the state  
  - the city  
  - the ZIP code  
  - basic property features (bedrooms, bathrooms, house size, land size)

The system then returns:
- a *predicted price*, and  
- a *local accuracy score* based on similar houses in the same area.

This introduction summarises the motivation behind the project and the expected outcome: a clear, functional, and intelligent price prediction tool.

# II. Datasets 

## 📥 Source of the data

The project is based on a large real estate dataset containing more than *2.2 million property listings* across the United States.  
The raw file includes information such as:

- 🏷 listing price  
- 🛏 number of bedrooms 
- 🚿 number of bathrooms 
- 🌱 lot size (acre_lot) 
- 📐 house size (square feet)  
- 📍 city, state, ZIP code
- 🗓 historical sale dates 

This dataset covers a wide geographic range and includes both rural and urban areas, making it suitable for building a general prediction model.

## 🧹 Data cleaning process

Since the raw data contained missing values, inconsistent entries, and redundant information, we performed several preprocessing steps:

- ❌ *Removal of incomplete rows* (e.g., missing price, missing key features)  
- 🔢 *Numerical conversion* of relevant fields  
- ✂️ *Filtering out extreme outliers* (e.g., absurd house sizes or unrealistic acre_lot values)  
- 🔄 *Encoding of categorical features*:
  - State → numeric label  
  - City → target encoding based on average property prices  

This allowed us to reduce the dataset from *2,226,382 rows* to *1,341,789 clean and usable entries*, improving both model performance and training time.

## 🧱 Final dataset structure

After cleaning, the dataset used for training contains the following columns:

- price — target variable  
- bed — number of bedrooms  
- bath — number of bathrooms  
- acre_lot — land size  
- city_encoded — encoded version of the city  
- state_encoded — encoded version of the state  
- zip_code — geographical ZIP code  
- house_size — interior area in square feet  

These features were selected because they capture both *location factors* and *property characteristics*, which are the two main determinants of real estate prices.

# III. Methodology  

## ⚙ Choice of Algorithms  
To build an accurate price prediction system, we evaluated several machine learning models and compared their performance. Our approach combined *interpretability, **computational efficiency, and **predictive accuracy*.

The following models were tested:

- *Linear Regression* — simple baseline, fast but limited for non-linear price variations  
- *Random Forest Regressor* — robust, captures non-linear relationships, performs well on mixed data  
- *LightGBM Regressor* — gradient boosting model optimized for large datasets, very fast and able to detect complex patterns  

After evaluation, *Random Forest* provided the best overall balance between stability, accuracy, and generalization on our cleaned dataset.

---

## 🧩 Feature Engineering  
To maximize model performance, categorical attributes such as city and state required specific transformations:

- *Label Encoding* for states → each U.S. state receives a unique numeric ID  
- *Target Encoding* for cities → each city is encoded using the average property price observed in the dataset  

This encoding strategy helps the model capture geographical price differences while avoiding excessive dimensionality.

We kept the most relevant property features:

- number of bedrooms  
- number of bathrooms  
- house size (square feet)  
- land size (acres)  
- ZIP code  
- encoded city and state identifiers  

These features were selected because they strongly influence real estate prices, both structurally and geographically.

---

## 🧠 Model Training Pipeline  
The training process followed a clear and reproducible workflow:

1. *Load the cleaned dataset*  
2. *Split* the data into training and testing sets  
3. *Train each model* using the same feature set  
4. *Evaluate performance* using  
   - MAE (Mean Absolute Error)  
   - RMSE (Root Mean Squared Error)  
   - R² score  
5. *Select the best model* based on global accuracy  
6. *Save the model* and encoders (city/state) for later inference  

Thanks to this structured pipeline, the system ensures reproducibility and reliable comparison between algorithms.

---

## 🖥 Interactive User Interface  
To make the system intuitive and accessible, we developed an interactive *Jupyter Notebook interface* using ipywidgets.  
The user can select:

- State ➝ filtered list of valid states  
- City ➝ dynamically filtered by the chosen state  
- ZIP code ➝ filtered by both state and city  
- Property features ➝ bedrooms, bathrooms, lot size, house size  

The interface then returns:

- 💰 *Predicted price*  
- 🎯 *Local accuracy score* based on similar nearby houses  

This interactive step transforms the model from a purely technical tool into a user-friendly assistant for real estate estimation.

# IV. Evaluation & Analysis  

## 📊 Model Performance Overview  
To evaluate our machine learning models, we used three standard regression metrics:

- *MAE (Mean Absolute Error)* — average absolute difference between predicted and real prices  
- *RMSE (Root Mean Squared Error)* — penalizes large errors, useful for detecting price overestimation  
- *R² Score* — measures how well the model explains price variability  

These metrics were computed on the test set (20% of the cleaned data).

Below is a summary of the results:

| Model                 | MAE (↓)     | RMSE (↓)    | R² (↑)  |
|----------------------|-------------|-------------|---------|
| Linear Regression     | ~173,431    | ~300,203    | 0.64    |
| LightGBM Regressor    | ~119,379    | ~228,385    | 0.79    |
| *Random Forest*     | ~106,415| ~214,083| 0.82 |

➡ *Random Forest achieved the best balance of stability and accuracy*, making it the model selected for the final system.

---

## 📈 Error Behavior Analysis  
Several important observations emerged during evaluation:

### 🔹 1. Small to medium-priced homes are predicted very accurately  
For houses priced between *$100k and $500k*, the model often achieves  
*10–20% precision*, sometimes even better.

### 🔹 2. Higher-priced homes increase prediction difficulty  
For luxury properties (+$1M), variability becomes much larger:

- wider architectural diversity  
- unique features not captured in our dataset  
- fewer training examples in these ranges  

This leads to occasional *$150k–$300k prediction gaps*, which is expected for this market segment.

---

## 🧭 Local Accuracy Indicator  
To improve interpretability during user testing, we added a *local accuracy score*:

- It measures how close the prediction is to real prices of *similar houses in the same geographic area*.
- It is calculated by comparing the predicted price with the mean price of nearby properties.

This helps users understand whether their specific prediction is within a reasonable range for the region.

---

## 🧪 Real-World Testing  
Using 10 randomly sampled houses from the dataset, the system produced:

- very accurate predictions for common homes  
- stable behavior across states  
- understandable deviations for atypical or luxury properties  

This confirms that the model generalizes well across the U.S. market while still reflecting local price patterns.

# V. Related Work  

## 📚 Existing Studies & Approaches  
Real estate price prediction has been widely explored in data science and machine learning.  
Most existing studies focus on:

- *Hedonic pricing models*, which analyze how each feature (size, location, rooms…) affects price  
- *Tree-based algorithms* such as Random Forest or Gradient Boosting, recognized for their robustness on tabular data  
- *Geographical modeling*, emphasizing the strong influence of location on housing prices  
- *Large-scale regression systems*, similar to Zillow’s Zestimate or Redfin’s valuation engine  

Our project follows this line of research by applying ML techniques to a nationwide dataset and using geographic-dependent encoding methods.

---

## 🛠 Tools, Libraries & Documentation Used  

*Machine Learning & Data Processing*
- pandas — data loading, cleaning, preprocessing  
- scikit-learn — model training (Linear Regression, Random Forest)  
- lightgbm — gradient boosting model  
- numpy — numerical operations  

*Interface Development*
- ipywidgets — interactive menus inside Jupyter Notebook  
- pickle — saving/loading trained models and encoders  

*Project Workflow & Version Control*
- GitHub — hosting code, notebooks, and documentation  
- Python 3.11 — main programming language  

*Documentation Consulted*
- Official *scikit-learn documentation*  
- LightGBM user guide  
- Python and pandas official docs  
- Various academic articles on housing price prediction models  

These resources guided our choices, helped validate preprocessing steps, and supported model selection.

# VI. Conclusion  

## 🏁 Summary of the Project  
This project demonstrates how machine learning can be used to predict real estate prices based on both *property characteristics* and *geographical features*.  
By cleaning and structuring a large-scale dataset, building several ML models, and designing an interactive prediction interface, we developed a system capable of generating reliable price estimates across the United States.

## 🔍 Key Takeaways  
- The *Random Forest* model provided the best performance, achieving strong accuracy on most price ranges.  
- Location remains the most influential factor in price prediction, justifying the use of state encoding and city target encoding.  
- The *interactive interface* greatly improves usability, enabling real-time predictions without requiring direct interaction with the model or code.

## 📉 Model Accuracy Across Price Ranges

One important insight from our experiments is that prediction accuracy varies depending on house price range.

### ✅ Good accuracy on affordable and mid-range houses  
- These houses are *much more common* in the dataset  
- The model has thousands of similar examples to learn from  
- Their features (size, location, bedrooms, etc.) follow *more stable patterns*  
- Prices vary within a smaller range, making errors less significant  

### ⚠ Lower precision for luxury or unique properties  
- Luxury properties represent *less than 1% of the dataset*  
- They are extremely diverse (unique architecture, huge land, premium locations)  
- Prices fluctuate widely even within the same city  
- Small mistakes in features can lead to large errors in final price  
- The model cannot learn rare or unique cases as well as common ones  

As a result:  
- A *±15,000$ error* on a 200,000$ house is normal and quite good  
- But a *±150,000$ error* on a 2,000,000$ house is also expected  
  because the variability of luxury markets is naturally much higher  

This behavior is typical of real estate models and reflects the underlying distribution of the data, not a flaw in the algorithm.

## 🚧 Limitations  
While effective, the system still faces challenges:  
- High-end or atypical properties can be harder to predict due to the lack of comparable data.  
- Target encoding for cities captures average price behavior but may smooth out very localized variations.  
- Real estate markets evolve rapidly, making periodic dataset updates essential.

## 🚀 Future Improvements  
Potential extensions include:  
- Using *deep learning models* to capture nonlinear patterns  
- Incorporating additional features (crime rate, school ratings, neighborhood trends)  
- Training state-specific or region-specific models  
- Deploying the interface as a web application for broader use  

Overall, this project highlights the potential of AI to support decision-making in the real estate sector, transforming large datasets into a *practical, accessible, and intelligent prediction tool*.

