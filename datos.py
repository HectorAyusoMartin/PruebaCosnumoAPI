import pandas as pd

def cargar_datos():
    
    """
    Carga un DataFrame de ejemplo. Este DataFrame se puede reemplazar por datos de un archivo o fuente externa.
    
    """
    
    datos = {
        
        'id': [1,2,3],                                   #OJO: KEY: columnas, VALUE: filas ..(en listas de 3, porque habra 3 filas)
        'nombre':['Juan','Alberto','Reyes'],
        'edad':[28,60,59],
        'profesion':['Cartero','Profesor','Farmaceutica']
        
    
    }
    
    dataframe  = pd.DataFrame(datos) #convertimos diccionario en DF con pandas
    
    return dataframe 





#funcion para filtrar datos por algun criterio

def filtrar_datos_edad(df,edad_minima):
    """
    Filtra las filas del DataFrame donde la edad sea mayor o igual a la edad mínima.
    
    :param df: DataFrame a filtrar
    :param edad_minima: Edad mínima para incluir en el resultado
    :return: DataFrame filtrado
    
    """
    
    df_filtrado = df[ df['edad'] >= edad_minima ]
    return df_filtrado





#funcion convertir un dataframe en un JSON para la Api
 
def convertir_json(df):
    """
    Convierte un DataFrame a un formato JSON para enviarlo desde la API.
    
    :param df: DataFrame a convertir
    :return: Diccionario en formato JSON
    """
    
    return df.to_dict(orient='records')


##############################################################################################

'''
Detalle de cada función:



cargar_datos:

Simula un DataFrame con datos de ejemplo (puedes reemplazarlo por datos reales en el futuro).
Utiliza un diccionario para crear columnas como id, nombre, edad y profesion.



filtrar_datos_por_edad:

Recibe un DataFrame y filtra las filas donde la edad sea mayor o igual a un valor mínimo.
Útil para casos donde necesites devolver datos con un criterio específico.



convertir_a_json:

Convierte el DataFrame a un formato JSON compatible con la API.
Usa to_dict(orient="records"), que convierte cada fila en un diccionario.


'''


##############################################################################################


'''


'''