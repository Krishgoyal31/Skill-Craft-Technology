🛍️ K-Means Customer Segmentation
This project uses K-Means clustering to segment customers based on their age, income, and spending score. 📊 Built with Python: pandas, matplotlib, seaborn, scikit-learn.

📝 Table of Contents
Overview

Features

Dataset

Setup

Usage

Process

Visuals

Contribute

License

✨ Overview
Identify distinct customer groups to tailor marketing! 🎯 Applies K-Means for effective customer segmentation.

🚀 Features
Data Prep: 🧹 Cleans Mall_Customers.csv.

Optimal K: 🤔 Uses Elbow Method to find best cluster count.

Clustering: 🧠 K-Means segments customers.

Viz: 📈 Plots elbow curve & customer segments.

💾 Dataset
Expects Mall_Customers.csv with CustomerID, Gender, Age, Annual Income (k$), Spending Score (1-100).

🛠️ Setup
Python required. Install libs:

pip install pandas matplotlib seaborn scikit-learn

🏃 Usage
Get Script: ⬇️ Save customer_segmentation.py and Mall_Customers.csv in same folder.

Run: ▶️

python customer_segmentation.py

See Results: Dataset preview, Elbow plot, and Customer Segments plot will appear! 📊

🧠 Process
Clean: CustomerID dropped, Gender encoded (0/1).

Features: Age, Annual Income, Spending Score selected.

Elbow Method: Finds optimal k (clusters) by plotting inertia.

Cluster: K-Means runs with chosen k (default 5).

🖼️ Visuals
Elbow Method Plot: Helps find the best k (the "elbow" point).

Customer Segments Plot: Scatter plot of Income vs. Spending Score, colored by cluster. See your customer groups! 🌈

🤝 Contribute
Fork, improve, PRs welcome! 🙏

📜 License
MIT License 📄
