import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # type: ignore
import plotly.express as px # type: ignore
import os

# Pour Windows
os.system("cls")

########################### Importer du CSV
df = pd.read_csv('iot2.csv')

 


# Trier par label 
df.sort_values("label",  ascending=True, inplace=True)

# selectionner que  type d'intrusion Backdoor_Malware 

dg: pd.DataFrame = df.loc[df['label'] == 'Backdoor_Malware']

# filtrer Wheight = 105

df: pd.DataFrame = df.loc[df['Weight'] == 105 ]

print(df)

# la moyenne de Magnitue 

Moy = np.average(df['Magnitue'])
print("La moyenne de Magnitue est : ",  Moy )

# Visualier les Magnitue en hitogramme 

plt.hist(df['label'].dropna(), bins=20)
plt.xlabel("label")
plt.ylabel("Magnitue")
plt.title("Histogramme de la colonne Magnitue")
plt.show()

fig = px.histogram(df, x="label", nbins=20, title="Histogramme des Magnitue", labels={"Magnitue":"Magnitue"})

fig.show()

