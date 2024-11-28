from prettytable import PrettyTable
from ..database.conexion import conectar
from ..utils.utils import error_rojo, limpiar_pantalla


# Funciones de validación
def validar_nombre(campo):
    """
    Valida que un nombre contenga solo letras, espacios y tenga un máximo de 50 caracteres.
    """
    while True:
        try:
            if len(campo) > 50:
                raise ValueError("El nombre no puede tener más de 50 caracteres.")
            if not all(x.isalpha() or x.isspace() for x in campo):
                raise ValueError("El nombre debe contener solo letras y espacios.")
            return campo
        except ValueError as e:
            error_rojo(f"Error de validación: {e}")
            campo = input("Por favor, ingrese un nombre válido: ").strip()


def validar_telefono(campo):
    """
    Valida que un teléfono contenga entre 8 y 12 caracteres numéricos, con o sin espacios.
    """
    while True:
        try:
            campo_sin_espacios = campo.replace(" ", "")
            if not campo_sin_espacios.isdigit():
                raise ValueError("El teléfono debe contener solo números y espacios.")
            if not (8 <= len(campo_sin_espacios) <= 12):
                raise ValueError("El teléfono debe tener entre 8 y 12 dígitos.")
            return campo
        except ValueError as e:
            error_rojo(f"Error de validación: {e}")
            campo = input("Por favor, ingrese un teléfono válido: ").strip()


# Funciones CRUD de Instructores
def crear_instructor():
    nombre = validar_nombre(input("Ingrese el nombre del instructor: ").strip())
    telefono = validar_telefono(input("Ingrese el teléfono del instructor: ").strip())

    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "INSERT INTO Instructores (Nombre, Telefono) VALUES (%s, %s)"
        cursor.execute(query, (nombre, telefono))
        conn.commit()
        print("¡Instructor creado exitosamente!")
    except Exception as e:
        error_rojo(
            f"No se pudo crear el instructor. Verifique la conexión o los datos ingresados. Detalle del error: {e}"
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
            error_rojo(
                "No se encontraron instructores registrados en la base de datos."
            )
            return

        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre", "Teléfono"]

        for instructor in instructores:
            tabla.add_row(instructor)

        print("\nListado de Instructores:")
        print(tabla)
    except Exception as e:
        error_rojo(
            f"Error al leer los instructores. Verifique la conexión o los datos registrados. Detalle del error: {e}"
        )
    finally:
        cursor.close()
        conn.close()


def actualizar_instructor():
    id_instructor = int(input("Ingrese el ID del instructor a modificar: ").strip())

    try:
        conn = conectar()
        cursor = conn.cursor()

        # Verificar si el instructor existe
        query = "SELECT * FROM Instructores WHERE idInstructores=%s"
        cursor.execute(query, (id_instructor,))
        instructor = cursor.fetchone()

        if instructor:
            # Mostrar los datos actuales
            print("\nDatos actuales del instructor:")
            print(f"Nombre: {instructor[1]}")
            print(f"Teléfono: {instructor[2]}")

            # Solicitar nuevos valores, dejando los actuales si los campos están vacíos
            nombre = input(
                f"Nuevo nombre del instructor (dejar vacío para mantener '{instructor[1]}'): "
            ).strip()
            nombre = validar_nombre(nombre or instructor[1])

            telefono = input(
                f"Nuevo teléfono del instructor (dejar vacío para mantener '{instructor[2]}'): "
            ).strip()
            telefono = validar_telefono(telefono or instructor[2])

            # Verificar si hubo cambios
            if nombre == instructor[1] and telefono == instructor[2]:
                print(
                    "No se realizaron cambios. Los datos del instructor permanecen iguales."
                )
            else:
                # Realizar la actualización solo si hubo cambios
                query_update = """
                    UPDATE Instructores 
                    SET Nombre=%s, Telefono=%s 
                    WHERE idInstructores=%s
                """
                cursor.execute(query_update, (nombre, telefono, id_instructor))
                conn.commit()

                print("¡Instructor actualizado exitosamente!")
        else:
            # Si el ID del instructor no existe
            error_rojo(
                f"No existe un instructor con el ID {id_instructor}. Verifique el dato ingresado."
            )
    except Exception as e:
        error_rojo(f"Error al actualizar el instructor. Detalle del error: {e}")
    finally:
        cursor.close()
        conn.close()


def eliminar_instructor():
    id_instructor = int(input("Ingrese el ID del instructor a eliminar: ").strip())

    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "SELECT * FROM Instructores WHERE idInstructores=%s"
        cursor.execute(query, (id_instructor,))
        instructor = cursor.fetchone()

        if instructor:
            print(
                f"\nDatos del instructor a eliminar: ID: {instructor[0]}, Nombre: {instructor[1]}"
            )

            confirmar = (
                input("¿Está seguro de que desea eliminar este instructor? (S/N): ")
                .strip()
                .upper()
            )
            if confirmar == "S":
                query_delete = "DELETE FROM Instructores WHERE idInstructores=%s"
                cursor.execute(query_delete, (id_instructor,))
                conn.commit()

                if cursor.rowcount == 0:
                    error_rojo("No se encontró un instructor con el ID proporcionado.")
                else:
                    print("¡Instructor eliminado exitosamente!")
            else:
                print("Operación cancelada.")
        else:
            error_rojo("No se encontró un instructor con el ID proporcionado.")
    except Exception as e:
        error_rojo(
            f"No se pudo eliminar el instructor. El instructor podría estar referenciado en otra tabla. Detalle del error: {e}"
        )
    finally:
        cursor.close()
        conn.close()
