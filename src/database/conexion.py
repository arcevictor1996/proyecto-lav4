import mysql.connector
from mysql.connector import Error
import os


def obtener_configuracion():
    """
    Obtiene la configuración de conexión desde variables de entorno.
    """
    try:
        return {
            "host": os.getenv("DB_HOST", "localhost"),  # valor por defecto 'localhost'
            "user": os.getenv("DB_USER", "root"),  # valor por defecto 'root'
            "password": os.getenv("DB_PASSWORD", "root"),  # valor por defecto 'root'
            "database": os.getenv(
                "DB_NAME", "DB_ACADEMIA"
            ),  # valor por defecto 'DB_ACADEMIA'
        }
    except Exception as e:
        print(
            "\033[31mLa configuración de conexión a la base de datos no es válida.\033[0m"
        )
        return None


def conectar():
    """
    Establece la conexión a la base de datos MySQL usando los parámetros de configuración.
    """
    try:
        config = obtener_configuracion()
        if not config:
            raise ValueError(
                "\033[31mLa configuración de conexión a la base de datos no es válida.\033[0m"
            )

        conexion = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"],
        )

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
            return conexion

    except Error as e:
        print("\033[31mError al intentar entablar conexion a la base de datos.\033[0m")
    except Exception as e:
        print("\033[31mError al intentar entablar conexion a la base de datos.\033[0m")
    return None


def cerrar_conexion(conexion):
    """
    Cierra la conexión con la base de datos de manera segura.
    """
    try:
        if conexion and conexion.is_connected():
            conexion.close()
            print("Conexión cerrada.")
    except Error as e:
        print("\033[31mError al cerrar la conexion con la base de datos.\033[0m")
    except Exception as e:
        print("\033[31mError al cerrar la conexion con la base de datos.\033[0m")
