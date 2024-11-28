from prettytable import PrettyTable
from ..database.conexion import conectar
from ..utils.utils import error_rojo


# Funciones de validación
def validar_entrada_entero(mensaje, min_valor=1):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < min_valor:
                raise ValueError(f"El valor debe ser mayor o igual a {min_valor}.")
            return valor
        except ValueError as e:
            error_rojo(
                f"Entrada no válida: {e}. Se esperaba un número mayor o igual a {min_valor}."
            )


def validar_entrada_cadena(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        else:
            error_rojo(
                "La entrada no puede estar vacía. Por favor, ingrese un valor válido."
            )


# Funciones CRUD de Instructores
def crear_instructor():
    nombre = validar_entrada_cadena("Ingrese nombre del instructor: ")
    telefono = validar_entrada_cadena("Ingrese teléfono del instructor: ")

    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "INSERT INTO Instructores (Nombre, Telefono) VALUES (%s, %s)"
        cursor.execute(query, (nombre, telefono))
        conn.commit()
        print("Instructor creado correctamente.")
    except Exception as e:
        error_rojo(
            f"Error al crear el instructor: {e}. Puede deberse a un problema de conexión o a una entrada de datos duplicada."
        )
    finally:
        cursor.close()
        conn.close()


def leer_instructores():
    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "SELECT * FROM Instructores"
        cursor.execute(query)
        instructores = cursor.fetchall()

        # Crear la tabla con encabezados
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre", "Teléfono"]

        # Añadir las filas con los datos de los instructores
        for instructor in instructores:
            tabla.add_row(instructor)

        # Imprimir la tabla
        print("\nListado de Instructores:")
        print(tabla)
    except Exception as e:
        error_rojo(
            f"Error al leer instructores: {e}. Puede deberse a un problema de conexión o a que no existen registros."
        )
    finally:
        cursor.close()
        conn.close()


def actualizar_instructor():
    id_instructor = validar_entrada_entero("Ingrese el ID del instructor a modificar: ")
    nombre = validar_entrada_cadena("Nuevo nombre del instructor: ")
    telefono = validar_entrada_cadena("Nuevo teléfono del instructor: ")

    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "UPDATE Instructores SET Nombre=%s, Telefono=%s WHERE idInstructores=%s"
        cursor.execute(query, (nombre, telefono, id_instructor))
        conn.commit()
        print("Instructor actualizado correctamente.")
    except Exception as e:
        error_rojo(
            f"Error al actualizar el instructor: {e}. Puede deberse a un problema de conexión o a que el ID proporcionado no existe."
        )
    finally:
        cursor.close()
        conn.close()


def eliminar_instructor():
    id_instructor = validar_entrada_entero("Ingrese el ID del instructor a eliminar: ")

    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "DELETE FROM Instructores WHERE idInstructores=%s"
        cursor.execute(query, (id_instructor,))
        conn.commit()

        if cursor.rowcount == 0:
            error_rojo("No se encontró ningún instructor con el ID proporcionado.")
        else:
            print("Instructor eliminado correctamente.")
    except Exception as e:
        error_rojo(
            f"Error al eliminar el instructor: {e}. Puede deberse a un problema de conexión o a que el instructor está referenciado en otra tabla."
        )
    finally:
        cursor.close()
        conn.close()
