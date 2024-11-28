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


# Funciones CRUD de Cursos
def crear_curso():
    codigo = validar_entrada_entero("Ingrese código del curso (número positivo): ")
    nombre = validar_entrada_cadena("Ingrese nombre del curso: ")
    cuota = validar_entrada_entero("Ingrese cuota del curso (número positivo): ")
    duracion = validar_entrada_entero(
        "Ingrese duración del curso en meses (número positivo): "
    )
    id_instructor = validar_entrada_entero(
        "Ingrese ID del instructor (número positivo): "
    )

    try:
        conn = conectar()
        cursor = conn.cursor()
        query = """
            INSERT INTO Cursos (Codigo, Nombre, Cuota, Duracion, IDInstructor) 
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (codigo, nombre, cuota, duracion, id_instructor))
        conn.commit()
        print("Curso creado correctamente.")
    except Exception as e:
        error_rojo(
            f"Error al crear el curso: {e}. Puede deberse a un problema de conexión o a una entrada de datos duplicada."
        )
    finally:
        cursor.close()
        conn.close()


def leer_cursos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "SELECT * FROM Cursos"
        cursor.execute(query)
        cursos = cursor.fetchall()

        # Crear la tabla con encabezados
        tabla = PrettyTable()
        tabla.field_names = [
            "Código",
            "Nombre",
            "Cuota",
            "Duración (meses)",
            "ID Instructor",
        ]

        # Añadir las filas con los datos de los cursos
        for curso in cursos:
            tabla.add_row(curso)

        # Imprimir la tabla
        print("\nListado de Cursos:")
        print(tabla)

    except Exception as e:
        error_rojo(
            f"Error al leer cursos: {e}. Puede deberse a un problema de conexión o a que no existen registros."
        )
    finally:
        cursor.close()
        conn.close()


def actualizar_curso():
    codigo = validar_entrada_entero(
        "Ingrese código del curso a modificar (número positivo): "
    )
    nombre = validar_entrada_cadena("Nuevo nombre del curso: ")
    cuota = validar_entrada_entero("Nueva cuota del curso (número positivo): ")
    duracion = validar_entrada_entero(
        "Nueva duración del curso en meses (número positivo): "
    )
    id_instructor = validar_entrada_entero(
        "Nuevo ID del instructor (número positivo): "
    )

    try:
        conn = conectar()
        cursor = conn.cursor()
        query = """
            UPDATE Cursos 
            SET Nombre=%s, Cuota=%s, Duracion=%s, IDInstructor=%s 
            WHERE Codigo=%s
        """
        cursor.execute(query, (nombre, cuota, duracion, id_instructor, codigo))
        conn.commit()
        print("Curso actualizado correctamente.")
    except Exception as e:
        error_rojo(
            f"Error al actualizar el curso: {e}. Puede deberse a un problema de conexión o a un código inexistente."
        )
    finally:
        cursor.close()
        conn.close()


def eliminar_curso():
    codigo = validar_entrada_entero(
        "Ingrese código del curso a eliminar (número positivo): "
    )

    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "DELETE FROM Cursos WHERE Codigo=%s"
        cursor.execute(query, (codigo,))
        conn.commit()

        if cursor.rowcount == 0:
            error_rojo("No se encontró ningún curso con el código proporcionado.")
        else:
            print("Curso eliminado correctamente.")
    except Exception as e:
        error_rojo(
            f"Error al eliminar el curso: {e}. Puede deberse a un problema de conexión o a que el curso está referenciado en otra tabla."
        )
    finally:
        cursor.close()
        conn.close()
