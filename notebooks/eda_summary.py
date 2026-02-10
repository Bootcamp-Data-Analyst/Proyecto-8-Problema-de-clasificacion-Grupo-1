import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración de rutas
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(base_dir, "plots")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Cargar datos
data_path = os.path.join(base_dir, "data", "airline_passenger_satisfaction.csv")
df = pd.read_csv(data_path)

# 1. Información General
print("--- Información General ---")
print(df.info())
print("\n--- Primeras Filas ---")
print(df.head())

# 2. Valores Faltantes
missing = df.isnull().sum()
print("\n--- Valores Faltantes ---")
print(missing[missing > 0])

# 3. Estadísticas Descriptivas
print("\n--- Estadísticas Descriptivas ---")
print(df.describe())

# 4. Distribución de la variable objetivo (satisfaction)
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='satisfaction', palette='viridis')
plt.title('Distribución de Satisfacción del Cliente')
plt.savefig(f"{output_dir}/target_distribution.png")
print(f"Grafico guardado: {output_dir}/target_distribution.png")

# 5. Correlación de variables numéricas
plt.figure(figsize=(12, 10))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=False, cmap='coolwarm')
plt.title('Matriz de Correlación')
plt.savefig(f"{output_dir}/correlation_matrix.png")
print(f"Grafico guardado: {output_dir}/correlation_matrix.png")

# 6. Satisfacción por Clase de Viaje
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Class', hue='satisfaction', palette='magma')
plt.title('Satisfacción por Clase de Viaje')
plt.savefig(f"{output_dir}/satisfaction_by_class.png")
print(f"Grafico guardado: {output_dir}/satisfaction_by_class.png")

# 7. Edad vs Satisfacción
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x='Age', hue='satisfaction', fill=True, common_norm=False)
plt.title('Distribución de Edad por Satisfacción')
plt.savefig(f"{output_dir}/age_vs_satisfaction.png")
print(f"Grafico guardado: {output_dir}/age_vs_satisfaction.png")

print("\nEDA inicial completado.")
