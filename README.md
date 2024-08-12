# House Pricing Prediction

House Pricing Prediction is Project 5 of predict analytic to help the user to predict of the price of the house, 

The project has been deployed on Heroku in this [link](https://house-prediction-project-ef397f4fe1e6.herokuapp.com/)

## Table of contents

1. [Origin dataset](#1-origin-dataset)

2. [Business requirements](#2-business-requirements)

    + [Epics](#epics)

    + [UserStories](#user-stories)

3. [Hypothesis and how to validate](#3-hypothesis-and-how-to-validate)

4. [The rationale to map the business requirements](#4-the-rationale-to-map-the-business-requirements)

5. [ML Business case](#5-ml-business-case)

6. [Dashboard intended design](#6-dashboard-design)

7. [Unfixed](#7-unfixed-bugs)

8. [Deployment](#8-deployment)

9. [Main data analytics and Machine learning libraries](#9-Main-data-analytics-and-Machine-learning-libraries)

## **1. Origin Dataset**

+ The dataset for this project is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). 
+ User stories are created to give expectation about users
+ Table below showcasing the variable, the description, 

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Mimimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodeling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## **2. Business Requirements**

1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

### Epics

+ Data collecting

+ Data cleaning, train and testing machine learning models

+ Data corralation for bulding accurate models

+ Modeling the data using machine learning method, such as Random forest and Gradient boosting

### User stories

+ As client, I want to be know what features that are corralate with SalePrices, from the most to the least corralated.(Data_Crralation.ipynb)

+ As technical user, I want to know which models performing better and which one performing worst. (Modeling.ipynb)

+ As techincal user, I want to 

+ As client, I want to have a clean datasets that are easy to understand. (Data_Cleaning.ipynb)

+ As user, I want to know the source of the data.

+ As client, I want to

+ As user, I want to see graphs that are simplfied (Data_Cleaning.ipynb)

+ As client, 

+ As

+ As

## **3. Hypothesis and how to validate**



## **4. The rationale to map the business requirements**

## **5. ML business case**

## **6. Dashboard design**

## **7. Unfixed bugs**

## **8. Deployment**

## **9. Main data analytics and Machine learning libraries**

+ Numpy wass used for data preparation for analysis, such as filling the missing data.

+ Pandas was used for data manipulationa and preparation.

+ Matplot-lib was used to create different plots for the  generate different types of plots.

+ Seaborn was used to create statistical graphs for data corralation, and dimension reduction.

+ Scikit-learn was used for the regression such as StandardScaler, LinearRegression, ARDRegression, RandomForestRegressor, GradientBoostingRegressor, and KNeighborsRegressor.

+ JupyterNoteBook was used as virtual environment for data collection, cleaning, corralation and modeling.

+ StreamLit was used for dashboard creation to provide important information.

