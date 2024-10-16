# Housing Price Prediction

## Project Overview

This project aims to predict housing prices using various features of properties. The dataset contains information about different attributes of houses and their corresponding prices.

## Dataset Description

The dataset includes the following features:

- `price`: The target variable, representing the price of the house
- `area`: Total area of the house in square feet
- `bedrooms`: Number of bedrooms
- `bathrooms`: Number of bathrooms
- `stories`: Number of stories in the house
- `mainroad`: Whether the house is connected to the main road (yes/no)
- `guestroom`: Presence of a guest room (yes/no)
- `basement`: Presence of a basement (yes/no)
- `hotwaterheating`: Availability of hot water heating (yes/no)
- `airconditioning`: Presence of air conditioning (yes/no)
- `parking`: Number of parking spaces
- `prefarea`: Whether the house is in a preferred area (yes/no)
- `furnishingstatus`: The furnishing status of the house (furnished/semi-furnished/unfurnished)

## Data Preprocessing

1. **Handling Missing Values**: Check for any missing values in the dataset and handle them appropriately.
2. **Encoding Categorical Variables**: Convert categorical variables (like 'mainroad', 'furnishingstatus', etc.) into numerical format using techniques like one-hot encoding or label encoding.
3. **Feature Scaling**: Apply Min-Max scaling to normalize the numerical features.

## Feature Selection

Analyze the importance of each feature in predicting the house price. Consider using techniques like correlation analysis or feature importance from tree-based models to select the most relevant features.

## Model Development

Develop and compare multiple regression models, such as:
- Linear Regression
- Random Forest Regression
- Gradient Boosting Regression

## Model Evaluation

Evaluate the models using metrics such as:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared (R²) score



