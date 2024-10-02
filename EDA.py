import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport

# Carga de datos
def cargar_datos(ruta_archivo):
    try:
        datos = pd.read_csv(ruta_archivo)
        print(f"Datos cargados exitosamente con {datos.shape[0]} filas y {datos.shape[1]} columnas.")
        return datos
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

# Análisis descriptivo
def analisis_descriptivo(datos):
    print("\nEstadísticas descriptivas")
    print(datos.describe())

# Visualización de datos
def visualizacion(datos):
    sns.pairplot(datos)
    plt.show()

# Informe automatizado
def informe_automatizado(datos, nombre_informe):
    informe = ProfileReport(datos, title="Informe EDA", explorative=True)
    informe.to_file(f"{nombre_informe}.html")
    print(f"Informe generado: {nombre_informe}.html")

# Función principal
def main(ruta_archivo, nombre_informe):
    datos = cargar_datos(ruta_archivo)
    if datos is not None:
        analisis_descriptivo(datos)
        visualizacion(datos)
        informe_automatizado(datos, nombre_informe)

if __name__ == "__main__":
    ruta_archivo = "C:\\Users\\juana\\OneDrive\\Documentos\\Algo_trading\\BTC_strats\\BTCUSDT_historical_data.csv"
    nombre_informe = "Informe EDA"
    main(ruta_archivo, nombre_informe)
