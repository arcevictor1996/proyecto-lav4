from prettytable import (PrettyTable,)  # Importamos la librería PrettyTable para crear tablas de texto formateadas
from ..database.conexion import ( conectar,)  # Importamos la función conectar para la conexión a la base de datos
from ..utils.utils import (error_rojo,)  # Importamos la función error_rojo para mostrar mensajes de error en rojo

# **Validaciones de los campos**
# Estas funciones validan los datos que se ingresan para asegurar que tengan el formato correcto.


# Función para validar el nombre
def validar_nombre(campo, apellido):
    while True:  # Bucle infinito hasta que el dato sea válido
        try:
            # Verifica que todos los caracteres en el campo sean letras o espacios
            if not all(x.isalpha() or x.isspace() for x in campo):
                raise ValueError(f"El {apellido} debe contener solo letras y espacios.")
            return campo  # Si la validación es correcta, devuelve el campo
        except ValueError as e:
            error_rojo(f"Error: {e}")  # Muestra el mensaje de error en rojo
            campo = input(
                f"Ingrese un {apellido} válido: "
            )  # Solicita al usuario que ingrese un nuevo valor


# Función similar para validar el apellido
def validar_apellido(campo, apellido):
    while True:
        try:
            # Verifica que todos los caracteres en el campo sean letras o espacios
            if not all(x.isalpha() or x.isspace() for x in campo):
                raise ValueError(f"El {apellido} debe contener solo letras y espacios.")
            return campo  # Si la validación es correcta, devuelve el campo
        except ValueError as e:
            error_rojo(f"Error: {e}")  # Muestra el mensaje de error en rojo
            campo = input(f"Ingrese un {apellido} válido: ")  # Solicita un nuevo valor


# Función para validar el teléfono
def validar_telefono(telefono):
    while True:
        try:
            # Verifica que el teléfono esté compuesto solo de números
            if not telefono.isdigit():
                raise ValueError("El teléfono debe contener solo números.")
            return telefono  # Si es válido, devuelve el teléfono
        except ValueError as e:
            error_rojo(f"Error: {e}")  # Muestra el mensaje de error en rojo
            telefono = input("Ingrese un teléfono válido: ")  # Solicita un nuevo valor


# Función para validar el DNI
def validar_dni(dni):
    while True:
        try:
            # Verifica que el DNI tenga exactamente 7 dígitos
            if not dni.isdigit() or len(dni) < 7:
                raise ValueError("El DNI debe ser un número mayor de 7 dígitos.")
            return dni  # Si es válido, devuelve el DNI
        except ValueError as e:
            error_rojo(f"Error: {e}")  # Muestra el mensaje de error en rojo
            dni = input("Ingrese un DNI válido: ")  # Solicita un nuevo valor


# Función para validar la dirección
def validar_direccion(direccion):
    while True:
        try:
            # Verifica que la dirección no esté vacía
            if len(direccion.strip()) == 0:
                raise ValueError("La dirección no puede estar vacía.")
            return direccion  # Si es válida, devuelve la dirección
        except ValueError as e:
            error_rojo(f"Error: {e}")  # Muestra el mensaje de error en rojo
            direccion = input(
                "Ingrese una dirección válida: "
            )  # Solicita un nuevo valor


# Función para validar el legajo
def validar_legajo(legajo):
    while True:
        try:
            # Verifica que el legajo sea un número positivo y que no tenga más de 5 dígitos
            if not legajo.isdigit() or len(legajo) < 1:
                raise ValueError("El legajo debe ser un número positivo.")
            if len(legajo) > 5:  # Limita el legajo a un máximo de 5 dígitos
                raise ValueError("El legajo debe hasta 5 dígitos.")
            return legajo  # Si es válido, devuelve el legajo
        except ValueError as e:
            error_rojo(f"Error: {e}")  # Muestra el mensaje de error en rojo
            legajo = input("Ingrese un legajo válido: ")  # Solicita un nuevo valor


# **Funciones CRUD (Crear, Leer, Actualizar, Eliminar alumnos)**
# Estas funciones permiten gestionar los datos de los alumnos en la base de datos.


# Función para crear un nuevo alumno en la base de datos
def crear_alumno():
    try:
        # Solicita los datos al usuario y los valida mediante las funciones anteriores
        nombre = validar_nombre(input("Ingrese nombre del alumno: "), "nombre")
        apellido = validar_apellido(input("Ingrese apellido del alumno: "), "apellido")
        telefono = validar_telefono(input("Ingrese teléfono del alumno: "))
        direccion = validar_direccion(input("Ingrese dirección del alumno: "))
        dni = validar_dni(input("Ingrese DNI del alumno: "))

        # Conexión a la base de datos
        conn = conectar()  # Establece la conexión con la base de datos
        cursor = conn.cursor()  # Crea un cursor para ejecutar las consultas SQL

        # Consulta SQL para insertar un nuevo alumno
        query = """
            INSERT INTO Alumnos (Nombre, Apellido, Telefono, Direccion, DNI) 
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(
            query, (nombre, apellido, telefono, direccion, dni)
        )  # Ejecuta la consulta con los datos proporcionados
        conn.commit()  # Guarda los cambios realizados en la base de datos
        print("Alumno creado correctamente.")
    except Exception as e:
        error_rojo(
            f"Error al crear alumno: {e}"
        )  # Si ocurre un error, muestra el mensaje de error
    finally:
        cursor.close()  # Cierra el cursor
        conn.close()  # Cierra la conexión a la base de datos


# Función para leer todos los alumnos de la base de datos y mostrarlos en una tabla
def leer_alumnos():
    try:
        conn = conectar()  # Establece la conexión con la base de datos
        cursor = conn.cursor()  # Crea un cursor para ejecutar las consultas SQL

        # Consulta SQL para obtener todos los alumnos
        query = "SELECT * FROM Alumnos ORDER BY Apellido" #oRDENADO POR LEGAJO
        cursor.execute(query)  # Ejecuta la consulta
        alumnos = cursor.fetchall()  # Obtiene todos los resultados

        # Crear la tabla con encabezados
        tabla = PrettyTable()
        tabla.field_names = [
            "Legajo",
            "Nombre",
            "Apellido",
            "Teléfono",
            "Dirección",
            "DNI",
        ]

        # Añadir las filas con los datos de los alumnos
        for alumno in alumnos:
            tabla.add_row(alumno)

        # Imprimir la tabla con los alumnos
        print("\nListado de Alumnos:")
        print(tabla)

    except Exception as e:
        error_rojo(
            f"Error al leer alumnos: {e}"
        )  # Si ocurre un error, muestra el mensaje de error
    finally:
        cursor.close()  # Cierra el cursor
        conn.close()  # Cierra la conexión a la base de datos


# Función para actualizar los datos de un alumno existente
def actualizar_alumno():
    legajo = validar_legajo(
        input("Ingrese el legajo del alumno a modificar: ")
    )  # Solicita y valida el legajo

    try:
        conn = conectar()  # Establece la conexión con la base de datos
        cursor = conn.cursor()  # Crea un cursor para ejecutar las consultas SQL

        # Consulta SQL para verificar si el legajo existe
        query = "SELECT * FROM Alumnos WHERE Legajo=%s"
        cursor.execute(query, (legajo,))
        alumno = cursor.fetchone()  # Obtiene un solo alumno con el legajo dado

        if alumno:
            # Si el legajo existe, muestra los datos actuales del alumno
            print("\nDatos actuales del alumno:")
            print(f"Nombre: {alumno[1]}")
            print(f"Apellido: {alumno[2]}")
            print(f"Teléfono: {alumno[3]}")
            print(f"Dirección: {alumno[4]}")
            print(f"DNI: {alumno[5]}")

            # Solicita los nuevos datos, permitiendo dejar en blanco para mantener los actuales
            nombre = validar_nombre(
                input(
                    f"Nuevo nombre del alumno (dejar vacío para mantener '{alumno[1]}'): "
                )
                or alumno[1],
                "nombre",
            )
            apellido = validar_apellido(
                input(
                    f"Nuevo apellido del alumno (dejar vacío para mantener '{alumno[2]}'): "
                )
                or alumno[2],
                "apellido",
            )
            telefono = validar_telefono(
                input(
                    f"Nuevo teléfono del alumno (dejar vacío para mantener '{alumno[3]}'): "
                )
                or alumno[3]
            )
            direccion = validar_direccion(
                input(
                    f"Nueva dirección del alumno (dejar vacío para mantener '{alumno[4]}'): "
                )
                or alumno[4]
            )
            dni = validar_dni(
                input(
                    f"Nuevo DNI del alumno (dejar vacío para mantener '{alumno[5]}'): "
                )
                or alumno[5]
            )

            # Consulta SQL para actualizar los datos del alumno
            update_query = """
                UPDATE Alumnos
                SET Nombre=%s, Apellido=%s, Telefono=%s, Direccion=%s, DNI=%s
                WHERE Legajo=%s
            """
            cursor.execute(
                update_query, (nombre, apellido, telefono, direccion, dni, legajo)
            )  # Ejecuta la consulta de actualización
            conn.commit()  # Guarda los cambios realizados
            print("Alumno actualizado correctamente.")

        else:
            print("Legajo no encontrado.")

    except Exception as e:
        error_rojo(
            f"Error al actualizar alumno: {e}"
        )  # Si ocurre un error, muestra el mensaje de error
    finally:
        cursor.close()  # Cierra el cursor
        conn.close()  # Cierra la conexión a la base de datos


# Función para eliminar un alumno de la base de datos
def eliminar_alumno():
    legajo = validar_legajo(
        input("Ingrese el legajo del alumno a eliminar: ")
    )  # Solicita y valida el legajo

    try:
        conn = conectar()  # Establece la conexión con la base de datos
        cursor = conn.cursor()  # Crea un cursor para ejecutar las consultas SQL

        # Consulta SQL para verificar si el legajo existe
        query = "SELECT * FROM Alumnos WHERE Legajo=%s"
        cursor.execute(query, (legajo,))
        alumno = cursor.fetchone()  # Obtiene un solo alumno con el legajo dado

        if alumno:
            # Si el alumno existe, muestra sus datos
            print("\nDatos del alumno a eliminar:")
            print(f"Nombre: {alumno[1]}")
            print(f"Apellido: {alumno[2]}")
            print(f"Teléfono: {alumno[3]}")
            print(f"Dirección: {alumno[4]}")
            print(f"DNI: {alumno[5]}")

            confirmacion = input("¿Está seguro de eliminar este alumno? (sí/no): ")
            if confirmacion.lower() == "sí":
                # Si el usuario confirma, elimina el alumno
                delete_query = "DELETE FROM Alumnos WHERE Legajo=%s"
                cursor.execute(
                    delete_query, (legajo,)
                )  # Ejecuta la consulta de eliminación
                conn.commit()  # Guarda los cambios realizados
                print("Alumno eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
        else:
            print("Legajo no encontrado.")

    except Exception as e:
        error_rojo(
            f"Error al eliminar alumno: {e}"
        )  # Si ocurre un error, muestra el mensaje de error
    finally:
        cursor.close()  # Cierra el cursor
        conn.close()  # Cierra la conexión a la base de datos
