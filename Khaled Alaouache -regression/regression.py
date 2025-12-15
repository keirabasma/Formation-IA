import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

print("\n--- Simple Linear Regression (lotsize vs. price) ---")

# Read the Excel file
df = pd.read_excel("homework.xlsx")

# Define features (X) and target (y)
# X must be a 2D array or DataFrame for scikit-learn
X_simple = df[['lotsize']]
y_simple = df['price']

# Split data into training and testing sets
X_train_simple, X_test_simple, y_train_simple, y_test_simple = train_test_split(
    X_simple, y_simple, test_size=0.2, random_state=42
)

# Create and train the model
model_simple = LinearRegression()
model_simple.fit(X_train_simple, y_train_simple)

# Get and print the results
print(f"Intercept: {model_simple.intercept_}")
print(f"Coefficient (lotsize): {model_simple.coef_}")
print(f"R-squared score on test data: {model_simple.score(X_test_simple, y_test_simple)}")
