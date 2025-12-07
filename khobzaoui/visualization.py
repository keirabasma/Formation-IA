import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df= pd.read_csv("cars.csv")

#To view data (20 row):
print(df.head(20))

#To view the count of each brand:
marque=df["brand"].value_counts()
print(marque)

# Convert column to NumPy array
maxPower = np.array(df['max_power'])

print("\n Max power Numpy array :")
print(maxPower[:10])  # View the  10 first elements

# Scatter Plot visualization

df.plot(kind="scatter", x="model", y="price")
plt.show()