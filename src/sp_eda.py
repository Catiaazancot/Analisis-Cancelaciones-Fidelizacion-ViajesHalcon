import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

# Hacer un analisis exploratorio de los datos 
def eda_preliminar(dataframe):
  display(dataframe.sample(5))
  print("-----------------")
  print('INFO')
  display(dataframe.info())
  print("-----------------")
  print('NULOS')
  display(round(dataframe.isnull().sum()/dataframe.shape[0]*100,2))
  print("-----------------")
  print('DUPLICADOS')
  print(dataframe.duplicated().sum())
  print("-----------------")
  print('VALUE COUNTS')
  for col in dataframe.select_dtypes(include='O').columns:
    print(dataframe[col].value_counts())
    print("---------------------")
    


# Visualizar outliers mediante histograma y boxplot
def plot_outliers(dataframe, col):
    
    # Crear un subplot con 2 filas y 1 columna
    fig, axes = plt.subplots(len(col), 2, figsize=(12, len(col) * 6))
    
    # Iterar sobre las columnas numéricas
    for i, col in enumerate(col):
        # Histograma
        sns.histplot(dataframe[col], kde=True, ax=axes[i, 0])
        axes[i, 0].set_title(f'Histograma de {col}')
        
        # Boxplot
        sns.boxplot(x=dataframe[col], ax=axes[i, 1])
        axes[i, 1].set_title(f'Boxplot de {col}')
    
    # Ajustar el layout para que no se superpongan los gráficos
    plt.tight_layout()
    plt.show()
