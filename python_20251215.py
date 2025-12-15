# ===========================================
# Analyse du Dataset Iris - Bechihi Salah
# ===========================================

# 1. Importation des bibliothèques
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from google.colab import files

print("Bibliothèques chargées avec succès - Bechihi Salah")

# 2. Chargement des données
uploaded = files.upload()
file_name = list(uploaded.keys())[0]
irisdf = pd.read_csv(file_name)
print("\nAperçu des données:")
print(irisdf.head())

# 3. Exploration des données
print("\n=== EXPLORATION DES DONNÉES ===")
print(f"Shape du dataset: {irisdf.shape}")
print("\nTypes de données:")
print(irisdf.dtypes)
print("\nValeurs manquantes:")
print(irisdf.isnull().sum())
print("\nEspèces uniques:")
print(irisdf['Species'].unique())

# 4. Séparation par espèces
setosa = irisdf[irisdf['Species'] == 'Iris-setosa']
versicolor = irisdf[irisdf['Species'] == 'Iris-versicolor']
virginica = irisdf[irisdf['Species'] == 'Iris-virginica']

print(f"\nDistribution des espèces:")
print(f"Setosa: {len(setosa)} échantillons")
print(f"Versicolor: {len(versicolor)} échantillons")
print(f"Virginica: {len(virginica)} échantillons")

# 5. Calcul des moyennes par espèce
print("\n=== STATISTIQUES DESCRIPTIVES ===")
print("\nMoyennes par espèce (arrondies à 1 décimale):")

features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
species_dfs = [setosa, versicolor, virginica]
species_names = ['Setosa', 'Versicolor', 'Virginica']

for name, df in zip(species_names, species_dfs):
    print(f"\n{name}:")
    for feature in features:
        mean_val = round(df[feature].mean(), 1)
        print(f"  {feature}: {mean_val}")

# 6. Visualisation des sépales
print("\n=== VISUALISATION 1: SEPAL LENGTH vs SEPAL WIDTH ===")
fig1 = go.Figure()

fig1.add_trace(go.Scatter(
    x=setosa['SepalWidthCm'], y=setosa['SepalLengthCm'],
    mode='markers', name='Setosa',
    marker=dict(color='rgb(52, 152, 219)', symbol='circle', size=10, opacity=0.8),
    hovertemplate="<b>Setosa</b><br>Largeur: %{x}cm<br>Longueur: %{y}cm"
))

fig1.add_trace(go.Scatter(
    x=versicolor['SepalWidthCm'], y=versicolor['SepalLengthCm'],
    mode='markers', name='Versicolor',
    marker=dict(color='rgb(170, 128, 255)', symbol='square', size=10, opacity=0.8),
    hovertemplate="<b>Versicolor</b><br>Largeur: %{x}cm<br>Longueur: %{y}cm"
))

fig1.add_trace(go.Scatter(
    x=virginica['SepalWidthCm'], y=virginica['SepalLengthCm'],
    mode='markers', name='Virginica',
    marker=dict(color='rgb(241, 196, 15)', symbol='diamond', size=10, opacity=0.8),
    hovertemplate="<b>Virginica</b><br>Largeur: %{x}cm<br>Longueur: %{y}cm"
))

fig1.update_layout(
    title='Relation Sepal Length vs Sepal Width - Bechihi Salah',
    xaxis_title='Sepal Width (cm)',
    yaxis_title='Sepal Length (cm)',
    template='plotly_white',
    height=500
)
fig1.show()

# 7. Visualisation des pétales
print("\n=== VISUALISATION 2: PETAL LENGTH vs PETAL WIDTH ===")
fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=setosa['PetalWidthCm'], y=setosa['PetalLengthCm'],
    mode='markers', name='Setosa',
    marker=dict(color='rgb(52, 152, 219)', symbol='circle', size=10, opacity=0.8),
    hovertemplate="<b>Setosa</b><br>Largeur: %{x}cm<br>Longueur: %{y}cm"
))

fig2.add_trace(go.Scatter(
    x=versicolor['PetalWidthCm'], y=versicolor['PetalLengthCm'],
    mode='markers', name='Versicolor',
    marker=dict(color='rgb(170, 128, 255)', symbol='square', size=10, opacity=0.8),
    hovertemplate="<b>Versicolor</b><br>Largeur: %{x}cm<br>Longueur: %{y}cm"
))

fig2.add_trace(go.Scatter(
    x=virginica['PetalWidthCm'], y=virginica['PetalLengthCm'],
    mode='markers', name='Virginica',
    marker=dict(color='rgb(241, 196, 15)', symbol='diamond', size=10, opacity=0.8),
    hovertemplate="<b>Virginica</b><br>Largeur: %{x}cm<br>Longueur: %{y}cm"
))

fig2.update_layout(
    title='Relation Petal Length vs Petal Width - Bechihi Salah',
    xaxis_title='Petal Width (cm)',
    yaxis_title='Petal Length (cm)',
    template='plotly_white',
    height=500
)
fig2.show()

# 8. Visualisation combinée (subplots)
print("\n=== VISUALISATION 3: COMPARAISON SÉPALES & PÉTALES ===")
fig3 = make_subplots(
    rows=1, cols=2,
    subplot_titles=('Sépales', 'Pétales')
)

# Sépales
fig3.add_trace(go.Scatter(
    x=setosa['SepalWidthCm'], y=setosa['SepalLengthCm'],
    mode='markers', name='Setosa',
    marker=dict(color='rgb(52, 152, 219)', symbol='circle', size=8)
), row=1, col=1)

fig3.add_trace(go.Scatter(
    x=versicolor['SepalWidthCm'], y=versicolor['SepalLengthCm'],
    mode='markers', name='Versicolor',
    marker=dict(color='rgb(170, 128, 255)', symbol='square', size=8)
), row=1, col=1)

fig3.add_trace(go.Scatter(
    x=virginica['SepalWidthCm'], y=virginica['SepalLengthCm'],
    mode='markers', name='Virginica',
    marker=dict(color='rgb(241, 196, 15)', symbol='diamond', size=8)
), row=1, col=1)

# Pétales
fig3.add_trace(go.Scatter(
    x=setosa['PetalWidthCm'], y=setosa['PetalLengthCm'],
    mode='markers', name='Setosa',
    marker=dict(color='rgb(52, 152, 219)', symbol='circle', size=8),
    showlegend=False
), row=1, col=2)

fig3.add_trace(go.Scatter(
    x=versicolor['PetalWidthCm'], y=versicolor['PetalLengthCm'],
    mode='markers', name='Versicolor',
    marker=dict(color='rgb(170, 128, 255)', symbol='square', size=8),
    showlegend=False
), row=1, col=2)

fig3.add_trace(go.Scatter(
    x=virginica['PetalWidthCm'], y=virginica['PetalLengthCm'],
    mode='markers', name='Virginica',
    marker=dict(color='rgb(241, 196, 15)', symbol='diamond', size=8),
    showlegend=False
), row=1, col=2)

fig3.update_xaxes(title_text="Largeur (cm)", row=1, col=1)
fig3.update_xaxes(title_text="Largeur (cm)", row=1, col=2)
fig3.update_yaxes(title_text="Longueur (cm)", row=1, col=1)
fig3.update_yaxes(title_text="Longueur (cm)", row=1, col=2)

fig3.update_layout(
    title='Analyse comparative des caractéristiques florales - Bechihi Salah',
    height=500,
    template='plotly_white'
)
fig3.show()

# 9. Diagramme parallèle
print("\n=== VISUALISATION 4: DIAGRAMME PARALLÈLE ===")

# Conversion des espèces en codes numériques
species_codes = pd.Categorical(irisdf['Species']).codes

fig4 = go.Figure(data=go.Parcoords(
    line=dict(
        color=species_codes,
        colorscale=[[0, 'rgb(52, 152, 219)'],
                   [0.5, 'rgb(170, 128, 255)'],
                   [1, 'rgb(241, 196, 15)']],
        showscale=True,
        colorbar=dict(
            title='Espèces',
            tickvals=[0, 1, 2],
            ticktext=['Setosa', 'Versicolor', 'Virginica']
        )
    ),
    dimensions=[
        dict(
            label='Sepal Length',
            values=irisdf['SepalLengthCm']
        ),
        dict(
            label='Sepal Width',
            values=irisdf['SepalWidthCm']
        ),
        dict(
            label='Petal Length',
            values=irisdf['PetalLengthCm']
        ),
        dict(
            label='Petal Width',
            values=irisdf['PetalWidthCm']
        )
    ]
))

fig4.update_layout(
    title='Diagramme parallèle des caractéristiques - Bechihi Salah',
    height=500
)
fig4.show()

# 10. Analyse des quartiles et outliers
print("\n=== ANALYSE DES QUARTILES ET OUTLIERS ===")

def calculate_quartiles(df, species_name):
    print(f"\n{species_name}:")
    for feature in features:
        q1 = round(df[feature].quantile(0.25), 1)
        q3 = round(df[feature].quantile(0.75), 1)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        outliers = df[(df[feature] < lower_bound) | (df[feature] > upper_bound)]
        print(f"  {feature}: Q1={q1}, Q3={q3}, IQR={iqr}, Outliers={len(outliers)}")

calculate_quartiles(setosa, "Setosa")
calculate_quartiles(versicolor, "Versicolor")
calculate_quartiles(virginica, "Virginica")

# 11. Matrice de corrélation
print("\n=== MATRICE DE CORRÉLATION ===")
numeric_cols = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
correlation_matrix = irisdf[numeric_cols].corr()

fig5, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
ax.set_title('Matrice de corrélation - Bechihi Salah', fontsize=14)
plt.tight_layout()
plt.show()

# 12. Boxplots par espèce
print("\n=== BOXPLOTS PAR ESPÈCE ===")
fig6, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for idx, feature in enumerate(features):
    data = [setosa[feature], versicolor[feature], virginica[feature]]
    axes[idx].boxplot(data, labels=['Setosa', 'Versicolor', 'Virginica'])
    axes[idx].set_title(f'Distribution de {feature}', fontsize=12)
    axes[idx].set_ylabel('cm')
    axes[idx].grid(True, alpha=0.3)

fig6.suptitle('Boxplots des caractéristiques par espèce - Bechihi Salah', fontsize=16)
plt.tight_layout()
plt.show()

# 13. Distribution des caractéristiques
print("\n=== DISTRIBUTION DES CARACTÉRISTIQUES ===")
fig7, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

colors = ['#3498db', '#aa80ff', '#f1c40f']
species_list = [setosa, versicolor, virginica]
labels = ['Setosa', 'Versicolor', 'Virginica']

for idx, feature in enumerate(features):
    for sp_df, color, label in zip(species_list, colors, labels):
        axes[idx].hist(sp_df[feature], alpha=0.6, color=color, label=label, density=True)
    
    axes[idx].set_title(f'Distribution de {feature}', fontsize=12)
    axes[idx].set_xlabel('cm')
    axes[idx].set_ylabel('Densité')
    axes[idx].legend()
    axes[idx].grid(True, alpha=0.3)

fig7.suptitle('Distribution des caractéristiques par espèce - Bechihi Salah', fontsize=16)
plt.tight_layout()
plt.show()

# 14. Résumé statistique complet
print("\n=== RÉSUMÉ STATISTIQUE COMPLET ===")
print("\nStatistiques descriptives pour toutes les espèces:")
print(irisdf[numeric_cols].describe())

print("\nStatistiques par espèce:")
for name, df in zip(['Setosa', 'Versicolor', 'Virginica'], species_dfs):
    print(f"\n{name}:")
    print(df[numeric_cols].describe().loc[['mean', 'std', 'min', 'max']])

print("\n" + "="*50)
print("ANALYSE TERMINÉE - BECHIHI SALAH")
print("="*50)