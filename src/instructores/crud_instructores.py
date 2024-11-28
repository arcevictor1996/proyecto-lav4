from prettytable import PrettyTable
from ..database.conexion import conectar
from ..utils.utils import error_rojo

# Funciones de validación


def validar_nombre(campo, tipo):
    while True:
        try:
            # Permitir solo letras y espacios
            if not all(x.isalpha() or x.isspace() for x in campo):
                raise ValueError(f"El {tipo} debe contener solo letras y espacios.")
            return campo
        except ValueError as e:
            error_rojo(f"Error: {e}")
            campo = input(f"Ingrese un {tipo} válido: ")


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
    nombre = validar_nombre(
        validar_entrada_cadena("Ingrese nombre del instructor: "), "nombre"
    )
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

        if not instructores:
            error_rojo("No se encontraron instructores en la base de datos.")
            return

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


# Función CRUD: Actualizar instructor
def actualizar_instructor():
    id_instructor = validar_entrada_entero("Ingrese el ID del instructor a modificar: ")

    try:
        conn = conectar()
        cursor = conn.cursor()

        # Verificar si el instructor existe
        query = "SELECT * FROM Instructores WHERE idInstructores=%s"
        cursor.execute(query, (id_instructor,))
        instructor = cursor.fetchone()

        if instructor:
            # El instructor existe, mostrar los datos actuales
            print("\nDatos actuales del instructor:")
            print(f"Nombre: {instructor[1]}")
            print(f"Teléfono: {instructor[2]}")

            # Solicitar los nuevos datos o dejar en blanco para mantener los actuales
            nombre = validar_entrada_cadena(
                input(
                    f"Nuevo nombre del instructor (dejar vacío para mantener '{instructor[1]}'): "
                )
                or instructor[1]  # Si se deja vacío, mantiene el actual
            )

            telefono_input = input(
                f"Nuevo teléfono del instructor (dejar vacío para mantener '{instructor[2]}'): "
            ).strip()

            # Si se deja vacío, mantiene el valor actual del teléfono
            telefono = telefono_input if telefono_input else instructor[2]

            # Realizar la actualización en la base de datos
            query_update = """
                UPDATE Instructores 
                SET Nombre=%s, Telefono=%s 
                WHERE idInstructores=%s
            """
            cursor.execute(query_update, (nombre, telefono, id_instructor))
            conn.commit()

            if cursor.rowcount == 0:
                error_rojo("No se encontró ningún instructor con el ID proporcionado.")
            else:
                print("Instructor actualizado correctamente.")
        else:
            # Si el ID del instructor no existe, mostrar un error
            error_rojo(
                f"Error: El ID de instructor {id_instructor} no existe en la base de datos."
            )

    except Exception as e:
        error_rojo(f"Error al actualizar el instructor: {e}")
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
