import pandas as pd
import matplotlib.pyplot as plt
from os import path


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


def main():
    # Direccionamiento a la carpeta data
    root =  path.join(path.dirname(path.abspath(__file__)), 'data')
    # Archivo csv
    file_csv = root + '\precios-de-gas-natural.csv'
    # Cargamos nuestro DataFrame
    df_csv = leer_csv(file_csv)
    #print(df_csv)
    # Archivo xlxrd
    file_xlsx = root + '\precios_res1_2018.xlsx'
    # Carga nuestro DataFrame
    df_xlsx = leer_xlsx(file_xlsx)
    #print(df_xlsx)
    # Realizar groupby
    df_csv_group = df_csv.groupby(['cuenca'])['precio_industria'].sum()
    #print(df_csv_group)
    # Realizar melt
    df_csv_melt = pd.melt(df_xlsx, id_vars = 'Cuenca', value_vars = ['Segmento', 'Condición'])
    #print(df_csv_melt)
    # Grafico de barras
    df_csv_group.plot(x='cuenca', y='precio_industria', kind='bar')
    # Impresión del grafico
    #plt.show()

if __name__ == '__main__':
    main()