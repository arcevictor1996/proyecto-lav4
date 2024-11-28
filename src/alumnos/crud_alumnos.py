from prettytable import PrettyTable
from ..database.conexion import conectar
from ..utils.utils import error_rojo


# Validaciones para los datos
def validar_nombre(campo, apellido):
    while True:
        try:
            # Permitir letras y espacios
            if not all(x.isalpha() or x.isspace() for x in campo):
                raise ValueError(f"El {apellido} debe contener solo letras y espacios.")
            return campo
        except ValueError as e:
            error_rojo(f"Error: {e}")
            campo = input(f"Ingrese un {apellido} válido: ")


def validar_apellido(campo, apellido):
    while True:
        try:
            # Permitir letras y espacios
            if not all(x.isalpha() or x.isspace() for x in campo):
                raise ValueError(f"El {apellido} debe contener solo letras y espacios.")
            return campo
        except ValueError as e:
            error_rojo(f"Error: {e}")
            campo = input(f"Ingrese un {apellido} válido: ")


def validar_telefono(telefono):
    while True:
        try:
            if not telefono.isdigit():
                raise ValueError("El teléfono debe contener solo números.")
            return telefono
        except ValueError as e:
            error_rojo(f"Error: {e}")
            telefono = input("Ingrese un teléfono válido: ")


def validar_dni(dni):
    while True:
        try:
            if not dni.isdigit() or len(dni) != 8:
                raise ValueError("El DNI debe ser un número de 8 dígitos.")
            return dni
        except ValueError as e:
            error_rojo(f"Error: {e}")
            dni = input("Ingrese un DNI válido: ")


def validar_direccion(direccion):
    while True:
        try:
            if len(direccion.strip()) == 0:
                raise ValueError("La dirección no puede estar vacía.")
            return direccion
        except ValueError as e:
            error_rojo(f"Error: {e}")
            direccion = input("Ingrese una dirección válida: ")


def validar_legajo(legajo):
    while True:
        try:
            if not legajo.isdigit() or len(legajo) < 1:
                raise ValueError("El legajo debe ser un número positivo.")
            if (
                len(legajo) > 3
            ):  # Aseguramos que el legajo tenga al menos 4 dígitos (si aplica en tu caso)
                raise ValueError("El legajo debe hasta 3 dígitos.")
            return legajo
        except ValueError as e:
            error_rojo(f"Error: {e}")
            legajo = input("Ingrese un legajo válido: ")


# Función CRUD: Crear alumno
def crear_alumno():
    try:
        # Solicitar y validar datos
        nombre = validar_nombre(input("Ingrese nombre del alumno: "), "nombre")
        apellido = validar_apellido(input("Ingrese apellido del alumno: "), "apellido")
        telefono = validar_telefono(input("Ingrese teléfono del alumno: "))
        direccion = validar_direccion(input("Ingrese dirección del alumno: "))
        dni = validar_dni(input("Ingrese DNI del alumno: "))

        # Conexión y ejecución de consulta
        conn = conectar()
        cursor = conn.cursor()
        query = """
            INSERT INTO Alumnos (Nombre, Apellido, Telefono, Direccion, DNI) 
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nombre, apellido, telefono, direccion, dni))
        conn.commit()
        print("Alumno creado correctamente.")
    except Exception as e:
        error_rojo(f"Error al crear alumno: {e}")
    finally:
        cursor.close()
        conn.close()


# Leer alumnos
def leer_alumnos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "SELECT * FROM Alumnos"
        cursor.execute(query)
        alumnos = cursor.fetchall()

        # Crear la tabla con encabezados
        tabla = PrettyTable()
        tabla.field_names = [
            "Legajo",
            "Apellido",
            "Nombre",
            "Teléfono",
            "Dirección",
            "DNI",
        ]

        # Añadir las filas con los datos de los alumnos
        for alumno in alumnos:
            tabla.add_row(alumno)

        # Imprimir la tabla
        print("\nListado de Alumnos:")
        print(tabla)

    except Exception as e:
        error_rojo(f"Error al leer alumnos: {e}")
    finally:
        cursor.close()
        conn.close()


# Función CRUD: Actualizar alumno
def actualizar_alumno():
    legajo = validar_legajo(input("Ingrese el legajo del alumno a modificar: "))

    try:
        conn = conectar()
        cursor = conn.cursor()

        # Verificar si el legajo existe
        query = "SELECT * FROM Alumnos WHERE Legajo=%s"
        cursor.execute(query, (legajo,))
        alumno = cursor.fetchone()

        if alumno:
            # El legajo existe, mostrar los datos actuales
            print("\nDatos actuales del alumno:")
            print(f"Nombre: {alumno[1]}")
            print(f"Apellido: {alumno[2]}")
            print(f"Teléfono: {alumno[3]}")
            print(f"Dirección: {alumno[4]}")
            print(f"DNI: {alumno[5]}")

            # Solicitar los nuevos datos o dejar en blanco para mantener los actuales
            nombre = validar_nombre(
                input(
                    f"Nuevo nombre del alumno (dejar vacío para mantener '{alumno[1]}'): "
                )
                or alumno[1],  # Si se deja vacío, mantiene el actual
                "nombre",
            )
            apellido = validar_apellido(
                input(
                    f"Nuevo apellido del alumno (dejar vacío para mantener '{alumno[2]}'): "
                )
                or alumno[2],  # Si se deja vacío, mantiene el actual
                "apellido",
            )
            telefono = validar_telefono(
                input(
                    f"Nuevo teléfono del alumno (dejar vacío para mantener '{alumno[3]}'): "
                )
                or alumno[3]  # Si se deja vacío, mantiene el actual
            )
            direccion = validar_direccion(
                input(
                    f"Nueva dirección del alumno (dejar vacío para mantener '{alumno[4]}'): "
                )
                or alumno[4]  # Si se deja vacío, mantiene el actual
            )
            dni = validar_dni(
                input(
                    f"Nuevo DNI del alumno (dejar vacío para mantener '{alumno[5]}'): "
                )
                or alumno[5]  # Si se deja vacío, mantiene el actual
            )

            # Realizar la actualización en la base de datos
            query_update = """
                UPDATE Alumnos 
                SET Nombre=%s, Apellido=%s, Telefono=%s, Direccion=%s, DNI=%s 
                WHERE Legajo=%s
            """
            cursor.execute(
                query_update, (nombre, apellido, telefono, direccion, dni, legajo)
            )
            conn.commit()
            print("Alumno actualizado correctamente.")
        else:
            # Si el legajo no existe, mostrar un error
            error_rojo(f"Error: El legajo {legajo} no existe en la base de datos.")

    except Exception as e:
        error_rojo(f"Error al actualizar el alumno: {e}")
    finally:
        cursor.close()
        conn.close()


# Eliminar alumno
def eliminar_alumno():
    legajo = validar_legajo(input("Ingrese el legajo del alumno a eliminar: "))

    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "SELECT * FROM Alumnos WHERE Legajo=%s"
        cursor.execute(query, (legajo,))
        alumno = cursor.fetchone()

        if alumno:
            print(
                f"\nDatos del alumno a eliminar: Legajo: {alumno[0]}, Nombre: {alumno[1]}"
            )

            confirmar = (
                input("¿Está seguro de que desea eliminar este alumno? (S/N): ")
                .strip()
                .upper()
            )
            if confirmar == "S":
                query_delete = "DELETE FROM Alumnos WHERE Legajo=%s"
                cursor.execute(query_delete, (legajo,))
                conn.commit()

                if cursor.rowcount == 0:
                    print("No se encontró ningún alumno con el legajo proporcionado.")
                else:
                    print("Alumno eliminado correctamente.")
            else:
                print("Operación cancelada.")
        else:
            print("No se encontró ningún alumno con el legajo proporcionado.")
    except Exception as e:
        error_rojo(f"Error al eliminar el alumno: {e}")
    finally:
        cursor.close()
        conn.close()
