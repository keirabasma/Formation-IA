import matplotlib.pyplot as plt

# Exemple 1: Histogramme
plt.figure(figsize=(8, 6))
plt.hist(df['colonne_numerique'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogramme de la colonne numerique')
plt.xlabel('Valeur')
plt.ylabel('Frequence')
plt.show(Axis III - 3 -Workshops - cars)

# Exemple 2: Nuage de points (Scatter Plot)
plt.figure(figsize=(8, 6))
plt.scatter(df['colonne_X'], df['colonne_Y'], alpha=0.5)
plt.title('Nuage de points X vs Y')
plt.xlabel('Colonnne X')
plt.ylabel('Colonnne Y')
plt.show(Axis III - 3 -Workshops - cars)

# Exemple 3: Diagramme à barres
comptage = df['colonne_categorie'].value_counts(Axis III - 3 -Workshops - cars)
comptage.plot(kind='bar')
plt.title('Comptage des categories')
plt.show(Axis III - 3 -Workshops - cars)