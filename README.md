# 🏗️ Gurgaon-Real-Estate-Recommendation-System

## 📌 Overview

The Gurgaon Real Estate Recommendation System is a web-based application built using Python and Streamlit to provide insights, predictions, and recommendations for real estate properties in Gurgaon, India. This project empowers users—whether buyers, sellers, investors, or market researchers—with tools to explore property data, predict prices, visualize trends, and discover similar apartments based on location and preferences.


## 🌟 Features

##### 1. Price Predictor
Predicts property prices based on inputs like property type, sector, number of bedrooms, bathrooms, built-up area, and more.
Provides an estimated price range for informed decision-making.



##### 2. Visual Analytics Dashboard
Interactive visualizations including:
Price per Sqft Geomap: Displays average price per square foot across sectors in Gurgaon.

     1. Features Word Cloud: Visualizes key property features for selected sectors.
     
     2. Area vs Price Scatter Plot: Compares property prices against built-up area by bedroom count.
     
     3. BHK Distribution Pie Chart: Shows the distribution of bedroom configurations.
     
     4. Price Range Box Plot: Illustrates price ranges for different BHK configurations.
     
     5. Price Distribution KDE Plot: Compares price distributions for houses and flats.



##### 3. Apartment Recommender
- Recommends similar apartments based on a selected property using cosine similarity.
  
- Allows filtering of properties within a specified radius from a chosen location.



## 🧱 Project structure
```
project/
├── Home.py                          
├── 1_Price_Predictor.py             
├── 2_Analytics_Module.py            
├── 3_Recommend_Apartments.py        
└── Datasets/                        
    ├── data_viz1.csv                
    ├── df.pkl                       
    ├── pipeline.pkl                
    ├── feature_text.pkl             
    ├── location_distance.pkl        
    ├── cosine_sim1.pkl              
    ├── cosine_sim2.pkl              
    └── cosine_sim3.pkl              
```

## 🛠️ Libraries Used

- `Python`: Core programming language.

- `Streamlit`: Framework for building the web application.

- `Pandas`: Data manipulation and analysis.

- `Matplotlib & Plotly & Seaborn`: Interactive and static visualizations.

- `WordCloud`: For generating word cloud visualizations.

- `Pickle`: For loading pre-trained models and datasets.

- `NumPy`: Numerical computations for recommendation algorithms.

- `Scikit-learn` : For Model selection and evaluation algorithm.


## 📂 Datasets

The datasets used in this project are stored in the Datasets/ folder and include property details such as sector, price, built-up area, and features, along with precomputed distance and similarity matrices for recommendations.
