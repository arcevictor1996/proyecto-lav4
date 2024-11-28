# Importación de las librerías necesarias
import mysql.connector  # Permite la conexión y la interacción con bases de datos MySQL.
from mysql.connector import (
    Error,
)  # Importa la clase Error para manejar excepciones específicas de MySQL.
import os  # Importa la librería os para interactuar con el sistema operativo y obtener variables de entorno.


# Función para obtener la configuración de la base de datos desde las variables de entorno
def obtener_configuracion():
    """
    Obtiene la configuración de conexión desde variables de entorno.
    Se establecen valores por defecto en caso de que las variables no estén configuradas.
    """
    try:
        # Obtiene la configuración de la base de datos desde las variables de entorno, con valores por defecto.
        return {
            "host": os.getenv(
                "DB_HOST", "localhost"
            ),  # Dirección del servidor de la base de datos, por defecto 'localhost'.
            "user": os.getenv(
                "DB_USER", "root"
            ),  # Usuario de la base de datos, por defecto 'root'.
            "password": os.getenv(
                "DB_PASSWORD", "root"
            ),  # Contraseña del usuario de la base de datos, por defecto vacía.
            "database": os.getenv(
                "DB_NAME", "DB_ACADEMIA"
            ),  # Nombre de la base de datos, por defecto 'DB_ACADEMIA'.
        }
    except Exception as e:
        # Si ocurre algún error al obtener la configuración, muestra un mensaje de error.
        print(
            "\033[31mLa configuración de conexión a la base de datos no es válida.\033[0m"  # Mensaje de error en color rojo.
        )
        return None  # Retorna None en caso de error.


# Función para establecer la conexión con la base de datos
def conectar():
    """
    Establece la conexión a la base de datos MySQL usando los parámetros de configuración obtenidos.
    Si la conexión es exitosa, retorna el objeto de conexión.
    """
    try:
        # Llama a la función obtener_configuracion() para obtener la configuración de conexión.
        config = obtener_configuracion()

        # Si la configuración no es válida (es None), lanza un error.
        if not config:
            raise ValueError(
                "\033[31mLa configuración de conexión a la base de datos no es válida.\033[0m"  # Mensaje de error en color rojo.
            )

        # Intenta establecer la conexión con la base de datos MySQL utilizando los parámetros obtenidos.
        conexion = mysql.connector.connect(
            host=config["host"],  # Dirección del servidor de base de datos.
            user=config["user"],  # Usuario para la base de datos.
            password=config["password"],  # Contraseña para la base de datos.
            database=config[
                "database"
            ],  # Nombre de la base de datos a la que se conectará.
        )

        # Verifica si la conexión fue exitosa.
        if conexion.is_connected():
            print(
                "Conexión exitosa a la base de datos."
            )  # Mensaje informativo si la conexión es exitosa.
            return conexion  # Retorna el objeto de conexión.

    except Error as e:
        # Si ocurre un error de conexión específico de MySQL, muestra un mensaje de error.
        print(
            "\033[31mError al intentar entablar conexion a la base de datos.\033[0m"
        )  # Mensaje de error en rojo.
    except Exception as e:
        # Si ocurre cualquier otro tipo de error, muestra un mensaje genérico.
        print(
            "\033[31mError al intentar entablar conexion a la base de datos.\033[0m"
        )  # Mensaje de error en rojo.

    return None  # Si la conexión falla, retorna None.


# Función para cerrar la conexión a la base de datos de manera segura
def cerrar_conexion(conexion):
    """
    Cierra la conexión con la base de datos de manera segura.
    Verifica si la conexión está activa antes de intentar cerrarla.
    """
    try:
        # Verifica si la conexión existe y está activa.
        if conexion and conexion.is_connected():
            conexion.close()  # Cierra la conexión a la base de datos.
            print(
                "Conexión cerrada."
            )  # Mensaje informativo de que la conexión fue cerrada exitosamente.
    except Error as e:
        # Si ocurre un error al cerrar la conexión, muestra un mensaje de error específico de MySQL.
        print(
            "\033[31mError al cerrar la conexion con la base de datos.\033[0m"
        )  # Mensaje de error en rojo.
    except Exception as e:
        # Si ocurre cualquier otro tipo de error, muestra un mensaje genérico.
        print(
            "\033[31mError al cerrar la conexion con la base de datos.\033[0m"
        )  # Mensaje de error en rojo.
