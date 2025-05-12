import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

def eda_preliminar(dataframe):
    '''Muestra una vista rápida de los datos: muestra 5 filas, info general, nulos, duplicados y conteos de variables categóricas.'''
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

def plot_outliers(dataframe, col):
    '''Muestra histogramas y boxplots para detectar outliers en las columnas numéricas indicadas.'''
    fig, axes = plt.subplots(len(col), 2, figsize=(12, len(col) * 6))
    for i, col in enumerate(col):
        sns.histplot(dataframe[col], kde=True, ax=axes[i, 0])
        axes[i, 0].set_title(f'Histograma de {col}')
        sns.boxplot(x=dataframe[col], ax=axes[i, 1])
        axes[i, 1].set_title(f'Boxplot de {col}')
    plt.tight_layout()
    plt.show()

def subplot_col_cat(dataframe, col_cat):
    '''Muestra gráficos de barras para cada columna categórica.'''
    num_cols = 3
    num_rows = (len(col_cat) // num_cols) + (1 if len(col_cat) % num_cols != 0 else 0)
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, num_rows * 5))
    axes = axes.flatten()
    for i, col in enumerate(col_cat):
        sns.countplot(x=col, data=dataframe, ax=axes[i])
        axes[i].set_title(f'Frecuencia de {col}')
        axes[i].tick_params(axis='x', rotation=45)
    for j in range(i + 1, len(axes)):
        axes[j].axis('off')
    plt.tight_layout()
    plt.show()

def subplot_col_num(dataframe, col):
    '''Muestra histogramas y boxplots para cada columna numérica.'''
    num_graph = len(col)
    num_rows = (num_graph + 2) // 2
    fig, axes = plt.subplots(num_graph, 2, figsize=(15, num_rows*5))
    for i, col in enumerate(col):
        sns.histplot(data=dataframe, x=col, ax=axes[i,0], bins=200)
        axes[i,0].set_title(f'Distribución de {col}')
        sns.boxplot(data=dataframe, x=col, ax=axes[i,1])
        axes[i,1].set_title(f'Boxplot de {col}')
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])
    plt.tight_layout()
    plt.show()

def analisis_temporal(dataframe, col_fecha):
    '''Analiza fechas por año, mes y nombre del día.'''
    for col in col_fecha:
        dataframe[col] = pd.to_datetime(dataframe[col], errors='coerce')
        fig, axes = plt.subplots(3, 1, figsize=(12, 18))
        dataframe[col].dt.year.value_counts().sort_index().plot(kind='line', ax=axes[0], marker='o', color='blue')
        axes[0].set_title(f'{col} por Año')
        dataframe[col].dt.month.value_counts().sort_index().plot(kind='line', ax=axes[1], marker='o', color='green')
        axes[1].set_title(f'{col} por Mes')
        daynames = dataframe[col].dt.day_name()
        daynames.value_counts().sort_index().plot(kind='line', ax=axes[2], marker='o', color='red')
        axes[2].set_title(f'{col} por Día (Nombre)')
        plt.tight_layout()
        plt.show()

def analisis_cancelaciones_cat(dataframe, metrica, col):
    '''Relaciona cancelaciones con variables categóricas mediante gráficos de barras.'''
    num_cols = len(col)
    num_rows = (num_cols + 1) // 2
    fig, axes = plt.subplots(num_rows, 2, figsize=(15, num_rows * 5))
    axes = axes.flatten()
    for i, column in enumerate(col):
        sns.countplot(x=column, hue=metrica, data=dataframe, ax=axes[i])
        axes[i].set_title(f'Relación de {column} con {metrica}')
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])
    plt.tight_layout()
    plt.show()

def analisis_cancelaciones_num(dataframe, métrica, col):
    '''Relaciona cancelaciones con variables numéricas mediante histogramas.'''
    num_cols = len(col)
    num_rows = (num_cols + 1) // 2
    fig, axes = plt.subplots(num_rows, 2, figsize=(15, num_rows * 5))
    axes = axes.flatten()
    for i, column in enumerate(col):
        sns.histplot(data=dataframe, x=column, hue=métrica, kde=True, ax=axes[i], bins=20)
        axes[i].set_title(f'Relación de {column} con {métrica}')
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])
    plt.tight_layout()
    plt.show()

def analizar_cancelacion_temporal(dataframe, target, date_columns):
    '''Analiza la relación entre cancelaciones y fechas por mes.'''
    for col in date_columns:
        plt.figure(figsize=(12, 6))
        sns.countplot(x=col, hue=target, data=dataframe)
        plt.title(f'Relación de {target} con {col} por Mes')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def matriz_correlacion(dataframe, col):
    '''Crea un heatmap con la correlación entre variables numéricas.'''
    df_num = dataframe[col]
    correlation_matrix = df_num.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Matriz de Correlación entre las Variables Numéricas')
    plt.tight_layout()
    plt.show()

def edad_tipo_paquete(dataframe):
    '''Relaciona cancelaciones con tipo de paquete y rango de edad.'''
    bins = [0, 30, 45, 60, 100]
    labels = ['18-30', '31-45', '46-60', '60+']
    dataframe['rango_edad'] = pd.cut(dataframe['edad'], bins=bins, labels=labels, right=False)
    plt.figure(figsize=(12, 6))
    sns.countplot(x='tipo_paquete', hue='rango_edad', data=dataframe, palette='coolwarm')
    plt.title('Cancelaciones por Tipo de Paquete y Rango de Edad')
    plt.tight_layout()
    plt.show()

def promociones_tipo_paquete(dataframe):
    '''Relaciona promociones aplicadas con tipo de paquete y cancelaciones.'''
    plt.figure(figsize=(12, 6))
    sns.countplot(x='tipo_paquete', hue='promocion_aplicada', data=dataframe, palette='coolwarm')
    plt.title('Relación entre Promoción Aplicada, Tipo de Paquete y Cancelaciones')
    plt.tight_layout()
    plt.show()

def promociones_costo(dataframe):
    '''Relaciona promociones con el costo total y cancelaciones mediante boxplot.'''
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='promocion_aplicada', y='costo_total', hue='cancelacion_reserva', data=dataframe, palette='coolwarm')
    plt.title('Eficiencia de las Promociones en Función del Costo Total y Cancelaciones')
    plt.tight_layout()
    plt.show()

def promociones_edad(dataframe):
    '''Relaciona promociones con grupos de edad y cancelaciones.'''
    plt.figure(figsize=(12, 6))
    sns.countplot(x='promocion_aplicada', hue='rango_edad', data=dataframe, palette='coolwarm')
    plt.title('Impacto de las Promociones en la Tasa de Cancelación por Grupo de Edad')
    plt.tight_layout()
    plt.show()

def reserva_calificacion(dataframe):
    '''Relaciona la fuente de reserva con la calificación promedio del usuario.'''
    calificacion_fuente = dataframe.groupby('fuente_reserva')['calificacion_usuario'].mean().reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(x='fuente_reserva', y='calificacion_usuario', data=calificacion_fuente, palette='coolwarm')
    plt.title('Relación entre Fuente de Reserva y Calificación Promedio de Usuario')
    plt.tight_layout()
    plt.show()

def comentarios_reserva(dataframe):
    '''Muestra los comentarios más frecuentes por fuente de reserva.'''
    comentarios_fuente_general = dataframe.groupby('fuente_reserva')['comentarios'].value_counts().reset_index(name='frecuencia')
    comentarios_fuente_general_sorted = comentarios_fuente_general.sort_values(by='frecuencia', ascending=False)
    display(comentarios_fuente_general_sorted.head(10))
