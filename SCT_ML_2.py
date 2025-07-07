import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

# Display first few rows
print("Dataset Preview:\n", df.head())

# Drop CustomerID
data = df.drop(['CustomerID'], axis=1)

# Encode Gender column
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

# Features: Age, Income, Spending Score
X = data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# Elbow Method to find optimal clusters
inertia = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X)
    inertia.append(model.inertia_)

# Plot elbow curve
plt.figure(figsize=(8, 4))
plt.plot(range(1, 11), inertia, marker='o')
plt.title("Elbow Method to find optimal k")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.grid()
plt.show()

# Fit KMeans with k=5 (or from elbow curve)
model = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = model.fit_predict(X)

# Visualize the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', palette='tab10', s=100)
plt.title("Customer Segments")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()
