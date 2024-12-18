from fastapi import FastAPI #importando la libreria FASTAPI



aplicacion=  FastAPI() # aplicacion == instancia de clase FastApi
#aplicacion sera la base sobre la que definirimeos nuestra ruta y funcionalidad


#definimos una ruta principal que responde a solicitudes GET en '/'
#Esta ruta simplemente devuelve un mensaje de bienvenida para fonfirmar que la API esta funcionando

@aplicacion.get("/")

def leer_inicio():
    #retornamos un diccionario que sera convertido automaticamente en JSON
    return {'mensaje':'API funcionando correctamente'}

#definimos una ruta GET en datos para devolver datos simulados
#esta ruta puede servir como ejemplo para recuperar informacion

@aplicacion.get('/datos')

def obtener_datos():
    #retornamos un ejemplo de datos, representado por un diccionario
    
    return {'datos':'Esto es un ejemplo de datos'}

#definimos una ruta POST en '/datos/ para recibir informacion enviada desde el Frontend
#aqui usamos un paramtro llamado elemento para representar los datos enviados.

@aplicacion.post('/datos')

def enviar_datos(elemento: dict):
    #retornamos los datos recibidos para confirmar su recepcion
    
    return{'recibido': elemento}


'''
Detalle de lo que hace cada sección del código:

Importación de FastAPI:

    Importamos FastAPI de su librería principal. Esto nos permite usar su funcionalidad para crear rutas y gestionar peticiones.
    
Crear la aplicación:

    La variable aplicacion es nuestra API. Aquí registramos las rutas y definimos cómo responderá a diferentes tipos de solicitudes (GET, POST, etc.).
    
Ruta principal (GET "/"):

    Cuando alguien acceda a la raíz de la API (http://127.0.0.1:8000/), verá el mensaje "API funcionando correctamente".
    Esto se hace usando la anotación @aplicacion.get("/").
    
Ruta para obtener datos (GET "/datos"):

    Aquí simulamos la recuperación de datos. Cuando se haga una solicitud GET a "/datos", la API responderá con un ejemplo de datos.
    
Ruta para enviar datos (POST "/datos"):

    En esta ruta recibimos datos del cliente (por ejemplo, del frontend).
    Usamos un parámetro elemento que espera un diccionario, y lo retornamos para confirmar que fue recibido.


'''



