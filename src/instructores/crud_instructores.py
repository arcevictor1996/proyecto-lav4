# Importa las librerías necesarias
from prettytable import (
    PrettyTable,
)  # Importa la librería PrettyTable para presentar los datos en formato de tabla
from ..database.conexion import (
    conectar,
)  # Importa la función 'conectar' desde el módulo de conexión a la base de datos
from ..utils.utils import (
    error_rojo,
    limpiar_pantalla,
)  # Importa las funciones 'error_rojo' (para mostrar errores en rojo) y 'limpiar_pantalla' (para limpiar la pantalla)


# Función para validar el nombre del instructor
def validar_nombre(campo):
    """
    Valida que un nombre contenga solo letras y espacios, y que tenga un máximo de 50 caracteres.
    """
    while (
        True
    ):  # Inicia un bucle infinito que continuará hasta que se ingrese un nombre válido
        try:
            # Verifica que el nombre no sea mayor a 50 caracteres
            if len(campo) > 50:
                raise ValueError(
                    "El nombre no puede tener más de 50 caracteres."
                )  # Lanza una excepción si el nombre tiene más de 50 caracteres

            # Verifica que el nombre solo contenga letras y espacios, no permite caracteres especiales ni números
            if not all(x.isalpha() or x.isspace() for x in campo):
                raise ValueError(
                    "El nombre debe contener solo letras y espacios."
                )  # Lanza una excepción si hay caracteres no permitidos

            return campo  # Si el nombre es válido, lo retorna
        except ValueError as e:  # Captura cualquier excepción de tipo ValueError
            error_rojo(
                f"Error de validación: {e}"
            )  # Muestra un mensaje de error en rojo en pantalla
            campo = input(
                "Por favor, ingrese un nombre válido: "
            ).strip()  # Solicita nuevamente el nombre del usuario


# Función para validar el teléfono del instructor
def validar_telefono(campo):
    """
    Valida que un teléfono contenga solo dígitos y tenga entre 8 y 12 caracteres, permitiendo o no espacios.
    """
    while (
        True
    ):  # Inicia un bucle infinito que continuará hasta que se ingrese un teléfono válido
        try:
            # Elimina los espacios en blanco del teléfono para facilitar la validación
            campo_sin_espacios = campo.replace(" ", "")

            # Verifica que el teléfono contenga solo dígitos (sin letras ni caracteres especiales)
            if not campo_sin_espacios.isdigit():
                raise ValueError(
                    "El teléfono debe contener solo números y espacios."
                )  # Lanza una excepción si hay caracteres no numéricos

            # Verifica que la longitud del teléfono sea entre 8 y 12 caracteres
            if not (8 <= len(campo_sin_espacios) <= 12):
                raise ValueError(
                    "El teléfono debe tener entre 8 y 12 dígitos."
                )  # Lanza una excepción si el número de dígitos no está en el rango permitido

            return campo  # Si el teléfono es válido, lo retorna
        except ValueError as e:  # Captura cualquier excepción de tipo ValueError
            error_rojo(
                f"Error de validación: {e}"
            )  # Muestra un mensaje de error en rojo en pantalla
            campo = input(
                "Por favor, ingrese un teléfono válido: "
            ).strip()  # Solicita nuevamente el teléfono del usuario


# Función para crear un nuevo instructor en la base de datos
def crear_instructor():
    """
    Crea un nuevo instructor en la base de datos.
    """
    # Solicita y valida el nombre del instructor
    nombre = validar_nombre(input("Ingrese el nombre y apellido del instructor: ").strip())

    # Solicita y valida el teléfono del instructor
    telefono = validar_telefono(input("Ingrese el teléfono del instructor: ").strip())

    try:
        # Establece la conexión con la base de datos utilizando la función 'conectar'
        conn = conectar()
        cursor = conn.cursor()  # Crea un cursor para ejecutar las consultas SQL

        # Define la consulta SQL para insertar un nuevo instructor en la base de datos
        query = "INSERT INTO Instructores (Nombre, Telefono) VALUES (%s, %s)"

        # Ejecuta la consulta de inserción con los valores proporcionados por el usuario
        cursor.execute(query, (nombre, telefono))

        # Confirma la transacción en la base de datos
        conn.commit()

        print(
            "¡Instructor creado exitosamente!"
        )  # Muestra un mensaje de éxito al usuario
    except (
        Exception
    ) as e:  # Captura cualquier excepción durante el proceso de inserción
        error_rojo(
            f"No se pudo crear el instructor. Verifique la conexión o los datos ingresados. Detalle del error: {e}"
        )
    finally:
        # Cierra el cursor y la conexión para liberar los recursos utilizados
        cursor.close()
        conn.close()


# Función para leer e imprimir todos los instructores registrados en la base de datos
def leer_instructores():
    """
    Lee e imprime todos los instructores registrados en la base de datos.
    """
    try:
        # Establece la conexión con la base de datos
        conn = conectar()
        cursor = conn.cursor()  # Crea un cursor para ejecutar las consultas SQL

        # Define la consulta SQL para obtener todos los instructores registrados
        query = "SELECT * FROM Instructores ORDER BY ID"#pidio el profe ordenamiento


        # Ejecuta la consulta
        cursor.execute(query)

        # Obtiene todos los resultados de la consulta
        instructores = cursor.fetchall()

        if not instructores:  # Si no se encuentran instructores registrados
            error_rojo(
                "No se encontraron instructores registrados en la base de datos."
            )
            return

        # Crea una tabla para mostrar los resultados con la librería PrettyTable
        tabla = PrettyTable()

        # Define los nombres de las columnas de la tabla
        tabla.field_names = ["ID", "Nombre", "Teléfono"]

        # Añade cada registro de instructor a la tabla
        for instructor in instructores:
            tabla.add_row(instructor)

        print("\nListado de Instructores:")  # Imprime un encabezado
        print(tabla)  # Imprime la tabla con los datos de los instructores
    except Exception as e:  # Captura cualquier excepción durante el proceso de lectura
        error_rojo(
            f"Error al leer los instructores. Verifique la conexión o los datos registrados. Detalle del error: {e}"
        )
    finally:
        # Cierra el cursor y la conexión para liberar los recursos
        cursor.close()
        conn.close()


# Función para actualizar los datos de un instructor en la base de datos
def actualizar_instructor():
    """
    Actualiza los datos de un instructor existente en la base de datos.
    """
    # Solicita el ID del instructor que se desea modificar
    id_instructor = int(input("Ingrese el ID del instructor a modificar: ").strip())

    try:
        # Establece la conexión con la base de datos
        conn = conectar()
        cursor = conn.cursor()  # Crea un cursor para ejecutar las consultas

        # Verifica si el instructor existe en la base de datos con el ID proporcionado
        query = "SELECT * FROM Instructores WHERE idInstructores=%s"
        cursor.execute(query, (id_instructor,))
        instructor = cursor.fetchone()  # Obtiene el primer resultado coincidente

        if instructor:  # Si se encuentra el instructor
            print("\nDatos actuales del instructor:")
            print(f"Nombre: {instructor[1]}")
            print(f"Teléfono: {instructor[2]}")

            # Solicita nuevos datos para el nombre y teléfono, manteniendo los valores actuales si no se proporcionan nuevos
            nombre = input(
                f"Nuevo nombre del instructor (dejar vacío para mantener '{instructor[1]}'): "
            ).strip()
            nombre = validar_nombre(
                nombre or instructor[1]
            )  # Si no se ingresa un nuevo nombre, mantiene el anterior

            telefono = input(
                f"Nuevo teléfono del instructor (dejar vacío para mantener '{instructor[2]}'): "
            ).strip()
            telefono = validar_telefono(
                telefono or instructor[2]
            )  # Lo mismo para el teléfono

            # Si no hay cambios, informa al usuario
            if nombre == instructor[1] and telefono == instructor[2]:
                print(
                    "No se realizaron cambios. Los datos del instructor permanecen iguales."
                )
            else:
                # Si hay cambios, realiza la actualización con la nueva información
                query_update = """
                    UPDATE Instructores 
                    SET Nombre=%s, Telefono=%s 
                    WHERE idInstructores=%s
                """
                cursor.execute(query_update, (nombre, telefono, id_instructor))
                conn.commit()  # Confirma la actualización en la base de datos

                print("¡Instructor actualizado exitosamente!")
        else:  # Si no se encuentra el instructor con el ID ingresado
            error_rojo(
                f"No existe un instructor con el ID {id_instructor}. Verifique el dato ingresado."
            )
    except (
        Exception
    ) as e:  # Captura cualquier excepción durante el proceso de actualización
        error_rojo(f"Error al actualizar el instructor. Detalle del error: {e}")
    finally:
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()


# Función para eliminar un instructor de la base de datos
def eliminar_instructor():
    """
    Elimina un instructor de la base de datos.
    """
    # Solicita el ID del instructor a eliminar
    id_instructor = int(input("Ingrese el ID del instructor a eliminar: ").strip())

    try:
        # Establece la conexión con la base de datos
        conn = conectar()
        cursor = conn.cursor()  # Crea un cursor para ejecutar las consultas SQL

        # Verifica si el instructor existe en la base de datos
        query = "SELECT * FROM Instructores WHERE idInstructores=%s"
        cursor.execute(query, (id_instructor,))
        instructor = cursor.fetchone()  # Obtiene el primer resultado coincidente

        if instructor:  # Si se encuentra el instructor
            # Pide confirmación para eliminar
            confirmacion = (
                input(
                    f"¿Está seguro de que desea eliminar el instructor {instructor[1]}? (s/n): "
                )
                .strip()
                .lower()
            )
            if confirmacion == "s":  # Si la respuesta es afirmativa
                # Elimina el instructor de la base de datos
                query_delete = "DELETE FROM Instructores WHERE idInstructores=%s"
                cursor.execute(query_delete, (id_instructor,))
                conn.commit()  # Confirma la eliminación en la base de datos

                print("¡Instructor eliminado exitosamente!")
            else:
                print(
                    "Eliminación cancelada."
                )  # Si el usuario no confirma la eliminación
        else:  # Si no se encuentra el instructor
            error_rojo(
                f"No existe un instructor con el ID {id_instructor}. Verifique el dato ingresado."
            )
    except (
        Exception
    ) as e:  # Captura cualquier excepción durante el proceso de eliminación
        error_rojo(f"Error al eliminar el instructor. Detalle del error: {e}")
    finally:
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
