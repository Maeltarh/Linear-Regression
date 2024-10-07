import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

# Données fournies
file_path = 'data.csv'
df = pd.read_csv(file_path)
actual_values = dict(zip(df['km'], df['price']))
kilometrages = list(actual_values.keys())
prix = list(actual_values.values())

# Coefficients destandardisés pour la régression
file_path = 'data.json'
with open(file_path, 'r') as file:
    data = json.load(file)
theta0_destandardise = data['data']['theta0']
theta1_destandardise = data['data']['theta1']

# Préparation de la ligne de régression
x = np.linspace(0, 250000, 400)
y = theta0_destandardise + (theta1_destandardise * x)

# Création du graphique
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Modèle de régression linéaire', color='blue')
plt.scatter(kilometrages, prix, color='red', label='Données réelles')
plt.title('Régression linéaire du prix par rapport au kilométrage')
plt.xlabel('Kilométrage')
plt.ylabel('Prix')
plt.legend()
plt.show()
