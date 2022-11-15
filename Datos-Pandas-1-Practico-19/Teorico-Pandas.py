import pandas as pd
import matplotlib.pyplot as plt

def leer_csv(file: str) -> pd.DataFrame:
    """Realiza la lectura de un archivo .csv
    :param file: Ruta del archivo a leer
    :type file: str
    :return df: DataFrame generado apartir del csv
    :type df: DataFrame"""
    # Sintaxis
    # pd.read_csv(filepath, sep=, header=, names=, skiprows=, na_values= ... )
    df=pd.read_csv(file, encoding="utf-8")
    return df


def leer_xlsx(file: str) -> pd.DataFrame:
    """Realiza la lectura de un archivo .xlsx
    :param file: Ruta del archivo a leer
    :type file: str
    :return df: DataFrame generado apartir del xlsx
    :type df: DataFrame"""
    try:
        # Sintaxis
        # pd.read_excel('mi-excel.xlsx', 'hoja1')
        df=pd.read_excel(file)
    except Exception:
        print('''Verifique haber instalado la biblioteca xlrd en caso contrario
                ejecute el siguiente comando en su terminal: pip install xlrd''')
    return df


def crear_df_conjunto() -> pd.DataFrame:
    """Realiza la creación de un DataFrame apartir de un conjunto
    :return df: DataFrame generado
    :type df: DataFrame"""
    df = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                      'value': [1, 2, 3,5]})
    return df


def crear_df_escalar() -> pd.DataFrame:
    """Realiza la creación de un DataFrame apartir de un escalar
    :return df: DataFrame generado
    :type df: DataFrame"""
    df = pd.Series (7, index = ['Enero','Febrero','Marzo'])
    return df


def crear_df_array() -> pd.DataFrame:
    """Realiza la creación de un DataFrame apartir de un array
    :return df: DataFrame generado
    :type df: DataFrame"""
    mi_array = {'col1': 1.0, 'col2':2.0, 'col3': 3.0}
    df = pd.DataFrame([mi_array])
    return df


def df_tips() -> str:
    """Impresión de tips de acciones simples de un DataFrame
    :return tips: Guía-Tips
    :type: str"""
    tips = f"""
    1. Mostrar las primeras 10 filas del CSV: print(df.head(10))
    2. Contar la cantidad de filas: print(len(df)
    3. Contar la cantidad de filas 2: print(«Cant. filas: %i» % len(df1))
    ---> El %i indica que ahí va una variable de tipo integer.
    ---> Al cerrar comillas dobles, el % indica qué es lo que debe reemplazar a %i
    4. Splicing de la data:
        4.1 print(df[:10]) muestra las primeras 10 filas
        4.2 print(df[5:])  muestra todo salvo las primeras 5 filas
        4.3 print(df[-3:]) muestra las últimas 3 filas
        4.4 print(df[:-2]) muestra todo salvo las últimas 2 filas
        4.5 print(df[-5:-2]) muestra desde la 5ta desde el final hasta 2 desde el final
    5. Pasar el campo str a minúscula: df = df['Keyword'].str.lower()
    6. Cómo ver las columnas de un DataFrame en Pandas: print(df.columns)
    7. Cómo ver el contenido de una columna en Pandas: print(df['CTR']) la columna se llama CTR
    8. Cómo sacar el promedio de los valores de una columna en Pandas: print(df['CTR'].mean())
    9. Posicionamiento: df.loc[0,:'nombre_columna']
    """
    return tips


def df_merger(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """Merge de dos DataFrame
    :param df1: DataFrame #1
    :type df1: DataFrame
    :param df2: DataFrame #2
    :type df2: DataFrame
    :return df: Resultado del Merge
    :type df: DataFrame"""
    # Modificar “how” según la necesidad
    df = df1.merge(df2, how='left', on=None, left_on='lkey',
                        right_on='rkey', left_index=False, right_index=False, sort=False,
                        suffixes=('_left', '_rigth'), copy=True, indicator=False, validate=None)
    return df


def df_resharping() -> pd.DataFrame:
    """Resharping de un DataFrame
    :return df: DataFrame transpuesto
    :type df: DataFrame"""
    df = pd.DataFrame({'equipo': ['A', 'B', 'C', 'D'], 'goles': [100, 200, 300, 400], 
                     'faltas': [1000, 190, 999, 888], 'amonestaciones': [232, 218, 310, 311]})
    df = pd.melt(df, id_vars='equipo', value_vars=['goles', 'faltas', 'amonestaciones'])
    return df


def df_scatter_plot():
    """Genera un diagrama de dispersión"""
    # Data
    data = {'tasa_desempleo': [6.1, 5.8, 5.7, 5.7,
                               5.8, 5.6, 5.5, 5.3, 5.2, 5.2],
            'indice_precio_stock': [1500, 1520, 1525, 1523, 1515, 1540,
                                    1545, 1560, 1555, 1565]}
    # DataFrame
    df = pd.DataFrame(data,columns=['tasa_desempleo','indice_precio_stock'])
    # Generación del diagrama
    df.plot(x ='tasa_desempleo', y='indice_precio_stock', kind = 'scatter')
    # Imprimir el diagrama
    plt.show()


def df_line_plot():
    """Genera un diagrama de linea"""
    # Data
    data = {'anio': [1920, 1930, 1940, 1950, 1960,
                     1970, 1980, 1990, 2000, 2010],
            'tasa_desempleo': [9.8, 12, 8, 7.2, 6.9, 7,
                               6.5, 6.2, 5.5, 6.3]}
    # DataFrame
    df = pd.DataFrame(data,columns=['anio','tasa_desempleo'])
    # Generacion del diagrama
    df.plot(x ='anio', y='tasa_desempleo', kind = 'line')
    # Imprimir digrama
    plt.show()

def df_bar_plot():
    """Genera un diagrama de barra"""
    # Data
    data = {'pais': ['USA', 'Canada', 'Germany', 'UK', 'France'], 
            'PBI_per_capita': [45000, 42000, 52000, 49000, 47000]}
    # DataFrame
    df = pd.DataFrame(data,columns=['pais','PBI_per_capita'])
    # Generacion del diagrama
    df.plot(x ='pais', y='PBI_per_capita', kind = 'bar')
    # Imprimir digrama
    plt.show()