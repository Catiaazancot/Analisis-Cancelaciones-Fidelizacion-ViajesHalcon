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


# Ver gráficamente las columnas categóricas
def subplot_col_cat(dataframe, col_cat):
  
  num_cols = 3  # Tres gráficos por fila
  num_rows = (len(col_cat) // num_cols) + (1 if len(col_cat) % num_cols != 0 else 0)  # Calcular el número de filas necesarias

# Crear el subplot con el número adecuado de filas y columnas
  fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, num_rows * 5))

# Asegurar que axes sea una matriz 2D incluso si hay menos de 3 columnas en la última fila
  axes = axes.flatten()

# Generar los gráficos de barras
  for i, col in enumerate(col_cat):
      sns.countplot(x=col, data=dataframe, ax=axes[i])
      axes[i].set_title(f'Frecuencia de {col}')
      axes[i].tick_params(axis='x', rotation=45)

  # Eliminar los ejes vacíos en caso de que haya filas incompletas
  for j in range(i + 1, len(axes)):
      axes[j].axis('off')

# Ajustar el layout para evitar solapamientos
  plt.tight_layout()
  plt.show()
  
  
# Ver gráficamente las columnas numéricas
def subplot_col_num(dataframe, col):
  num_graph = len(col)
  num_rows = (num_graph + 2) // 2

  fig, axes = plt.subplots(num_graph, 2, figsize=(15, num_rows*5))

  for i, col in enumerate(col):
      sns.histplot(data=dataframe, x=col, ax=axes[i,0], bins=200)
      axes[i,0].set_title(f'Distribucion de {col}')
      axes[i,0].set_xlabel(col)
      axes[i,0].set_ylabel('Frecuencia')
      
      sns.boxplot(data=dataframe, x=col, ax=axes[i,1])
      axes[i,1].set_title(f'Boxplot de {col}')

  for j in range(i+1, len(axes)):
    fig.delaxes(axes[j])

  plt.tight_layout()
  plt.show()
  

# Analizar las columnas temporales por año, por mes Y por día 
def analisis_temporal(dataframe, col_fecha):
    for col in col_fecha:
        # Convertir la columna a datetime
        dataframe[col] = pd.to_datetime(dataframe[col], errors='coerce')
        
        # Crear el subplot con tres gráficos (por año, por mes y por día con nombre)
        fig, axes = plt.subplots(3, 1, figsize=(12, 18))
        
        # Por año
        dataframe[col].dt.year.value_counts().sort_index().plot(kind='line', ax=axes[0], marker='o', color='blue')
        axes[0].set_title(f'{col} por Año')
        axes[0].set_xlabel('Año')
        axes[0].set_ylabel('Frecuencia')

        # Por mes
        dataframe[col].dt.month.value_counts().sort_index().plot(kind='line', ax=axes[1], marker='o', color='green')
        axes[1].set_title(f'{col} por Mes')
        axes[1].set_xlabel('Mes')
        axes[1].set_ylabel('Frecuencia')

        # Por día con nombre
        daynames = dataframe[col].dt.day_name()
        daynames.value_counts().sort_index().plot(kind='line', ax=axes[2], marker='o', color='red')
        axes[2].set_title(f'{col} por Día (Nombre del Día)')
        axes[2].set_xlabel('Día')
        axes[2].set_ylabel('Frecuencia')

        # Ajustar el layout
        plt.tight_layout()
        plt.show()
        

# Relacionar 'cancelaciones' con cada columna categórica
def analisis_cancelaciones_cat(dataframe, metrica, col):
    # Crear un subplot con un gráfico de barras por cada columna categórica
    num_cols = len(col)
    num_rows = (num_cols + 1) // 2  # Calcular el número de filas necesarias

    fig, axes = plt.subplots(num_rows, 2, figsize=(15, num_rows * 5))

    # Aplanar el arreglo de ejes para manejarlos más fácilmente
    axes = axes.flatten()

    # Iterar sobre las columnas categóricas
    for i, column in enumerate(col):
        sns.countplot(x=column, hue=metrica, data=dataframe, ax=axes[i])
        axes[i].set_title(f'Relación de {column} con {metrica}')
        axes[i].set_xlabel(column)
        axes[i].set_ylabel('Frecuencia')

    # Eliminar los ejes vacíos en caso de que haya filas incompletas
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
    

# Relacionar 'cancelaciones' con las variables numéricas 
def analisis_cancelaciones_num(dataframe, métrica, col):
    # Crear un subplot con un gráfico de barras por cada columna numérica
    num_cols = len(col)
    num_rows = (num_cols + 1) // 2  # Calcular el número de filas necesarias

    fig, axes = plt.subplots(num_rows, 2, figsize=(15, num_rows * 5))

    # Aplanar el arreglo de ejes para manejarlos más fácilmente
    axes = axes.flatten()

    # Iterar sobre las columnas numéricas
    for i, column in enumerate(col):
        sns.histplot(data=dataframe, x=column, hue=métrica, kde=True, ax=axes[i], bins=20)
        axes[i].set_title(f'Relación de {column} con {métrica}')
        axes[i].set_xlabel(column)
        axes[i].set_ylabel('Frecuencia')

    # Eliminar los ejes vacíos en caso de que haya filas incompletas
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
    


# Crear función para analizar cancelaciones por mes y nombre del día
def analizar_cancelacion_temporal(dataframe, target, date_columns):
    for col in date_columns:
        # Agrupar por mes y nombre del día
        plt.figure(figsize=(12, 6))
        
        # Por mes
        sns.countplot(x=col, hue=target, data=dataframe)
        plt.title(f'Relación de {target} con {col} por Mes')
        plt.xlabel(col)
        plt.ylabel('Frecuencia')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        

# Crear una matriz de correlación entre las variables numéricas
def matriz_correlacion(dataframe, col):
    # Seleccionar solo las columnas numéricas del dataframe
    df_num = dataframe[col]

    # Calcular la matriz de correlación
    correlation_matrix = df_num.corr()

    # Crear un heatmap para visualizar la matriz de correlación
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Matriz de Correlación entre las Variables Numéricas')
    plt.tight_layout()
    plt.show()
    
    
# Relacionar la edad con el tipo de paquete y las cancelaciones
def edad_tipo_paquete(dataframe):
  # Crear los rangos de edad
  bins = [0, 30, 45, 60, 100]  # Rango de edades
  labels = ['18-30', '31-45', '46-60', '60+']  # Etiquetas para los rangos de edad
  dataframe['rango_edad'] = pd.cut(dataframe['edad'], bins=bins, labels=labels, right=False)

  # Graficar la relación entre 'cancelaciones', 'rango_edad' y 'tipo_paquete'
  plt.figure(figsize=(12, 6))
  sns.countplot(x='tipo_paquete', hue='rango_edad', data=dataframe, palette='coolwarm')
  plt.title('Cancelaciones por Tipo de Paquete y Rango de Edad')
  plt.xlabel('Tipo de Paquete')
  plt.ylabel('Frecuencia')
  plt.tight_layout()
  plt.show()
  
  
# Relacionar las promociones con los tipos de paquete y las cancelaciones
def promociones_tipo_paquete(dataframe):
  
  plt.figure(figsize=(12, 6))
  sns.countplot(x='tipo_paquete', hue='promocion_aplicada', data=dataframe, palette='coolwarm')
  plt.title('Relación entre Promoción Aplicada, Tipo de Paquete y Cancelaciones')
  plt.xlabel('Tipo de Paquete')
  plt.ylabel('Frecuencia de Cancelaciones')
  plt.tight_layout()
  plt.show()
  
  
# Relacionar las promociones, con el costo total y las cancelaciones
def promociones_costo(dataframe):
  plt.figure(figsize=(12, 6))
  sns.boxplot(x='promocion_aplicada', y='costo_total', hue='cancelacion_reserva', data=dataframe, palette='coolwarm')
  plt.title('Eficiencia de las Promociones en Función del Costo Total y Cancelaciones')
  plt.xlabel('Promoción Aplicada')
  plt.ylabel('Costo Total')
  plt.tight_layout()
  plt.show()
  
  
# Relacionar las promociones con los grupos de edad y las cancelaciones
def promociones_edad(dataframe):
  plt.figure(figsize=(12, 6))
  sns.countplot(x='promocion_aplicada', hue='rango_edad', data=dataframe, palette='coolwarm')
  plt.title('Impacto de las Promociones en la Tasa de Cancelación por Grupo de Edad')
  plt.xlabel('Promoción Aplicada')
  plt.ylabel('Frecuencia de Cancelaciones')
  plt.tight_layout()
  plt.show()
  

# Relacionar la fuente de reserva con la calificación del usuario
def reserva_calificacion(dataframe):
  # Agrupar por 'fuente_reserva' y calcular la media de las calificaciones
  calificacion_fuente = dataframe.groupby('fuente_reserva')['calificacion_usuario'].mean().reset_index()

  # Graficar la relación entre 'fuente_reserva' y la calificación promedio
  plt.figure(figsize=(12, 6))
  sns.barplot(x='fuente_reserva', y='calificacion_usuario', data=calificacion_fuente, palette='coolwarm')
  plt.title('Relación entre Fuente de Reserva y Calificación Promedio de Usuario')
  plt.xlabel('Fuente de Reserva')
  plt.ylabel('Calificación Promedio')
  plt.tight_layout()
  plt.show()
  
  
# Relacionar los comentarios con la fuente de reserva
def comentarios_reserva(dataframe):
  # Contar la frecuencia de los comentarios por fuente de reserva (sin filtrar por motivos específicos)
  comentarios_fuente_general = dataframe.groupby('fuente_reserva')['comentarios'].value_counts().reset_index(name='frecuencia')

  # Mostrar los 10 comentarios más frecuentes por fuente de reserva
  comentarios_fuente_general_sorted = comentarios_fuente_general.sort_values(by='frecuencia', ascending=False)