import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # type: ignore
import plotly.express as px # type: ignore
import os

# Pour Windows
os.system("cls")

########################### Importer du CSV
df = pd.read_csv('car.csv')


# Trier par par car_name
df.sort_values("car_name",  ascending=True, inplace=True)

# selectionner que  fuel type Petrol et marque Audi 

df = df.loc[df['fuel_type'] == 'Petrol']
df = df.loc[df['brand'] == 'Audi']
print("Les voitures Audi qui marchent avec Petrol sont:") 
print(df)

# la moyenne de max power

Moy = np.average(df['max_power'])
print("La moyenne de max power est : ",  Moy )

# ancienne voiture 
anc = np.min(df['engine'])
dg = df.loc[df['engine']== anc]

print("Les voitures les plus anciennes sont:") 
print (dg)

# Visualier les PRix en hitogramme 

plt.hist(df['num'].dropna(), bins=20)
plt.xlabel("num")
plt.ylabel("price")
plt.title("Histogramme de la colonne Prix")
plt.show()

# Visualiser en Histogramme les quantités de chaque modèle
 
fig = px.histogram(df, x="model", nbins=20, title="Histogramme des models", labels={"max_power":"max_power"})

fig.show()

