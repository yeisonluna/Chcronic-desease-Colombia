import pandas as pd

# Carga de datos
df = pd.read_csv('C:/Users/capir/OneDrive/Escritorio/Chronic-deseases-Colombia/data/raw_data.csv')

# Limpieza básica
df.dropna(inplace=True)  # Eliminación de valores nulos
df.to_csv('C:/Users/capir/OneDrive/Escritorio/Chronic-deseases-Colombia/data/cleaned_data.csv', index=False)
