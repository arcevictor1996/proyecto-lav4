from prettytable import PrettyTable
from ..database.conexion import conectar
from ..utils.utils import error_rojo, limpiar_pantalla


# FUNCIONES DE VALIDACION
def validar_codigo(mensaje):
    """Valida que el usuario ingrese un número entre 1 y 99."""
    while True:
        try:
            codigo = input(mensaje).strip()
            if not codigo.isdigit():
                raise ValueError("Debe ingresar un número.")
            codigo = int(codigo)
            if 1 <= codigo <= 99:
                return codigo
            else:
                raise ValueError("El número debe estar entre 1 y 99.")
        except ValueError as e:
            error_rojo(f"Entrada no válida: {e}")


def validar_nombre(mensaje, permitir_vacio=False, valor_actual=None):
    """
    Valida que el nombre sea alfanumérico y tenga hasta 100 caracteres.
    Si `permitir_vacio` es True, permite devolver el `valor_actual` cuando el usuario deja el campo vacío.
    """
    while True:
        entrada = input(mensaje).strip()

        if permitir_vacio and entrada == "":
            return valor_actual  # Mantener el valor actual

        if len(entrada) <= 100 and entrada.replace(" ", "").isalnum():
            return entrada
        else:
            error_rojo("El nombre debe ser alfanumérico y tener hasta 100 caracteres.")


def validar_cuota(mensaje, permitir_vacio=False, valor_actual=None):
    """
    Valida que el monto sea mayor a 0 y no supere los 6 dígitos.
    Si `permitir_vacio` es True, devuelve el `valor_actual` cuando se deja vacío.
    """
    while True:
        cuota = input(mensaje).strip()
        if permitir_vacio and not cuota:
            return valor_actual  # Mantener el valor actual
        if cuota.isdigit():
            cuota = int(cuota)
            if 0 <= cuota <= 999999:
                return cuota
        error_rojo("El monto debe ser un número entre 0 y 999,999.")


def validar_duracion(mensaje, permitir_vacio=False, valor_actual=None):
    """
    Valida que la duración esté entre 1 y 60 meses.
    Si `permitir_vacio` es True, devuelve el `valor_actual` cuando se deja vacío.
    """
    while True:
        duracion = input(mensaje).strip()
        if permitir_vacio and not duracion:
            return valor_actual  # Mantener el valor actual
        if duracion.isdigit():
            duracion = int(duracion)
            if 1 <= duracion <= 60:
                return duracion
        error_rojo("La duración debe ser un número entre 1 y 60.")


def validar_id_instructor(mensaje, conn, permitir_vacio=False, valor_actual=None):
    """
    Valida que el ID del instructor exista en la base de datos.
    Si `permitir_vacio` es True, devuelve `valor_actual` cuando se deja vacío.
    """
    cursor = conn.cursor()
    while True:
        id_instructor = input(mensaje).strip()
        if permitir_vacio and not id_instructor:
            return valor_actual  # Mantener el valor actual

        if id_instructor.isdigit():
            id_instructor = int(id_instructor)
            query = "SELECT * FROM Instructores WHERE ID = %s"
            cursor.execute(query, (id_instructor,))
            if cursor.fetchone():
                return id_instructor
            else:
                error_rojo(
                    f"El ID {id_instructor} no corresponde a un instructor existente."
                )
        else:
            error_rojo("El ID del instructor debe ser un número positivo.")


# Funciones CRUD de Cursos
def crear_curso():
    conn = None
    cursor = None

    try:
        conn = conectar()
        cursor = conn.cursor()

        # Solicitar datos para el nuevo curso
        nombre = validar_nombre("Ingrese el nombre del curso: ")
        cuota = validar_cuota("Ingrese la cuota del curso: ")
        duracion = validar_duracion("Ingrese la duración del curso en meses: ")
        id_instructor = validar_id_instructor(
            "Ingrese el ID del instructor responsable del curso: ", conn=conn
        )

        # Insertar el curso en la base de datos
        query = """
            INSERT INTO Cursos (Nombre, Cuota, Duracion, IDInstructor) 
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (nombre, cuota, duracion, id_instructor))
        conn.commit()
        print("Curso creado exitosamente.")

    except Exception as e:
        error_rojo(f"Error al crear el curso: {e}.")
    finally:
        if cursor:
            cursor.close()
        if conn:
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
    codigo = validar_codigo("Ingrese código del curso a modificar (1 a 99): ")

    conn = None
    cursor = None

    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "SELECT * FROM Cursos WHERE Codigo=%s"
        cursor.execute(query, (codigo,))
        curso = cursor.fetchone()

        if curso:
            print("\nDatos actuales del curso:")
            print(f"Nombre: {curso[1]}")
            print(f"Cuota: {curso[2]}")
            print(f"Duración: {curso[3]} meses")
            print(f"ID Instructor: {curso[4]}")

            # Validaciones para los campos
            nombre = validar_nombre(
                f"Nuevo nombre del curso (dejar vacío para mantener '{curso[1]}'): ",
                permitir_vacio=True,
                valor_actual=curso[1],
            )
            cuota = validar_cuota(
                f"Nueva cuota del curso (dejar vacío para mantener '{curso[2]}'): ",
                permitir_vacio=True,
                valor_actual=curso[2],
            )
            duracion = validar_duracion(
                f"Nueva duración del curso en meses (dejar vacío para mantener '{curso[3]}'): ",
                permitir_vacio=True,
                valor_actual=curso[3],
            )
            id_instructor = validar_id_instructor(
                f"Nuevo ID del instructor (dejar vacío para mantener '{curso[4]}'): ",
                conn=conn,
                permitir_vacio=True,
                valor_actual=curso[4],
            )

            # Actualización en la base de datos
            query_update = """
                UPDATE Cursos 
                SET Nombre=%s, Cuota=%s, Duracion=%s, IDInstructor=%s 
                WHERE Codigo=%s
            """
            cursor.execute(
                query_update, (nombre, cuota, duracion, id_instructor, codigo)
            )
            conn.commit()
            print("Curso actualizado correctamente.")
        else:
            error_rojo(f"El curso con código {codigo} no existe.")

    except Exception as e:
        error_rojo(f"Error al actualizar el curso: {e}.")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def eliminar_curso():
    codigo = validar_codigo("Ingrese código del curso a eliminar (1 a 99): ")

    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "SELECT * FROM Cursos WHERE Codigo=%s"
        cursor.execute(query, (codigo,))
        curso = cursor.fetchone()

        if curso:
            print("\nDatos del curso a eliminar:")
            print(
                f"Código: {curso[0]}, Nombre: {curso[1]}, Cuota: {curso[2]}, Duración: {curso[3]} meses, ID Instructor: {curso[4]}"
            )

            confirmar = (
                input("¿Está seguro de que desea eliminar este curso? (S/N): ")
                .strip()
                .upper()
            )
            if confirmar == "S":
                query_delete = "DELETE FROM Cursos WHERE Codigo=%s"
                cursor.execute(query_delete, (codigo,))
                conn.commit()
                print("Curso eliminado correctamente.")
            else:
                print("Operación cancelada.")
        else:
            error_rojo(f"No se encontró ningún curso con el código {codigo}.")
    except Exception as e:
        error_rojo(f"Error al eliminar el curso: {e}.")
    finally:
        cursor.close()
        conn.close()
