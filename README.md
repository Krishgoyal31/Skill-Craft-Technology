House Price Prediction Model
This project implements a simple linear regression model to predict house prices based on key features: area, number of bedrooms, and number of washrooms. It's built using Python with numpy, scikit-learn, and matplotlib.

Table of Contents
Project Overview

Features

Installation

Usage

Model Evaluation

Plots

Contributing

License

Project Overview
The goal of this project is to demonstrate a basic machine learning workflow for predicting continuous values (house prices). A linear regression model is trained on a small dataset of house features and their corresponding prices. The model's performance is then evaluated using common regression metrics, and the results are visualized.

Features
Linear Regression Model: Utilizes sklearn.linear_model.LinearRegression for price prediction.

Input Features:

Area (in square feet)

Number of Bedrooms

Number of Washrooms

Price Prediction: Predicts the price of a new house based on user-provided features.

Model Evaluation: Calculates and displays:

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

Root Mean Squared Error (RMSE)

R-squared (R 
2
 ) Score

Data Visualization:

Scatter plot comparing actual vs. predicted prices.

Residual plot showing prediction errors.

Installation
To run this project, you need Python installed on your system. You can then install the required libraries using pip:

pip install numpy scikit-learn matplotlib

Usage
Clone the repository (or save the script):
If you're uploading this to a new repository, you'll simply place the Python script (house_price_predictor.py or similar) in your repository.

Run the script:
Navigate to the directory containing the script in your terminal and execute it:

python house_price_predictor.py

Provide Input:
The script will prompt you to enter the details for a new house you want to predict the price for:

Enter area of NewHouse:

Enter NO of Bedrooms in NewHouse:

Enter No of Washrooms in NewHouse:

View Results:
After inputting the details, the script will print:

The predicted price for the new house.

Model coefficients and intercept.

Evaluation metrics (MAE, RMSE, R² Score).

Two plots will pop up: "Actual vs Predicted House Prices" and "Residual Plot (Error for Each House)".

Model Evaluation
The script outputs the following metrics to assess the model's performance:

Coefficients: These values indicate the weight or importance of each feature in predicting the price. For example, a positive coefficient for 'Area' means that as the area increases, the price tends to increase.

Intercept: This is the predicted price when all features are zero (though this might not be practically meaningful in this context).

MAE (Mean Absolute Error): The average absolute difference between the actual and predicted values. It gives an idea of the typical magnitude of errors.

RMSE (Root Mean Squared Error): The square root of the average of the squared differences between actual and predicted values. It penalizes larger errors more heavily than MAE.

R² Score: Represents the proportion of the variance in the dependent variable (price) that is predictable from the independent variables (features). A higher R 
2
  (closer to 1) indicates a better fit.

Plots
The script generates two plots:

Actual vs Predicted House Prices:
This plot shows the actual house prices (blue dots) against the prices predicted by the model (red line) for the training data. Ideally, the red line should closely follow the blue dots.

Residual Plot (Error for Each House):
This plot displays the difference between actual and predicted prices (residuals) for each house. A good model will have residuals randomly scattered around the zero line, indicating that the model is not systematically over- or under-predicting.

Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Any contributions are welcome!

License
This project is open-source and available under the MIT License.
