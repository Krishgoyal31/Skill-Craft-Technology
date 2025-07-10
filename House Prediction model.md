🏠 House Price Prediction Model
This project uses a simple linear regression model to predict house prices based on area, bedrooms, and washrooms. Built with Python, numpy, scikit-learn, and matplotlib.

📖 Table of Contents
Project Overview

Features

Installation

Usage

Model Evaluation

Plots

Contributing

License

✨ Project Overview
Predict house prices using a basic machine learning workflow. A linear regression model is trained on house features, then evaluated and visualized.

🚀 Features
Linear Regression: sklearn.linear_model.LinearRegression for predictions.

Input Features: 📏 Area (sq. ft.), 🛏️ Bedrooms, 🚿 Washrooms.

Price Prediction: Get price for new houses based on your input.

Model Evaluation: Displays:

MAE (Mean Absolute Error)

MSE (Mean Squared Error)

RMSE (Root Mean Squared Error)

R² Score

Data Visualization:

📈 Actual vs. Predicted Price scatter plot.

📉 Residual plot for prediction errors.

🛠️ Installation
Requires Python. Install libraries via pip:

pip install numpy scikit-learn matplotlib

🏃 Usage
Get the script: Clone the repo or save the Python script (e.g., house_price_predictor.py).

Run: Execute from your terminal:

python house_price_predictor.py

Input: Enter new house details when prompted:

Enter area of NewHouse:

Enter NO of Bedrooms in NewHouse:

Enter No of Washrooms in NewHouse:

View Results: Predicted price, model stats, and two plots will appear.

📊 Model Evaluation
Outputs to assess performance:

Coefficients: Feature importance.

Intercept: Base predicted price.

MAE: Average prediction error.

RMSE: Penalizes larger errors.

R² Score: How well the model fits the data (closer to 1 is better).

🖼️ Plots
Two plots are generated:

Actual vs Predicted House Prices: Blue dots (actual) vs. red line (predicted).

Residual Plot: Errors (actual - predicted) scattered around zero.

🤝 Contributing
Fork, improve, and submit pull requests! All contributions welcome.

📜 License
This project is open-source under the MIT License.
