ADNANI Sirine /
DA COSTA Shawn /
OUBOUSSAD Camille-Lina

# 🏡 AI Powered House Price Prediction System
Predicting real estate prices using machine learning

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

# ⭐ I. Introduction

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

# 📊 II. Dataset

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

