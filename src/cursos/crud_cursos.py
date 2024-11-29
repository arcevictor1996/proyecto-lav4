# Importación de módulos necesarios
from prettytable import (
    PrettyTable,
)  # Importa PrettyTable, que se utiliza para generar tablas formateadas de manera legible
from ..database.conexion import (
    conectar,
)  # Importa la función conectar desde el módulo de conexión a la base de datos
from ..utils.utils import (
    error_rojo,
    limpiar_pantalla,
)  # Importa las funciones error_rojo y limpiar_pantalla desde un módulo de utilidades

# FUNCIONES DE VALIDACIÓN


# Función para validar un código
def validar_codigo(mensaje):
    """
    Esta función solicita al usuario ingresar un código (número entero) entre 1 y 99.
    Valida que el input sea un número entero dentro del rango especificado.
    Si la entrada es incorrecta, muestra un mensaje de error y vuelve a pedir la entrada.
    """
    while True:  # Repite el proceso hasta que se ingrese una entrada válida
        try:
            # Solicita al usuario el código y elimina los espacios en blanco al principio y al final
            codigo = input(mensaje).strip()

            # Verifica si el código ingresado es un número
            if not codigo.isdigit():
                raise ValueError(
                    "Debe ingresar un número."
                )  # Si no es un número, lanza un error

            # Convierte el código a entero
            codigo = int(codigo)

            # Verifica si el código está dentro del rango válido (entre 1 y 99)
            if 1 <= codigo <= 99:
                return codigo  # Si es válido, retorna el código
            else:
                raise ValueError(
                    "El número debe estar entre 1 y 99."
                )  # Si no está en el rango, lanza un error
        except ValueError as e:
            # En caso de error (por ejemplo, el código no es un número o está fuera del rango), muestra el error
            error_rojo(
                f"Entrada no válida: {e}"
            )  # Llama a la función error_rojo para mostrar el mensaje de error en rojo


# Función para validar un nombre
def validar_nombre(mensaje, permitir_vacio=False, valor_actual=None):
    """
    Esta función valida que el nombre ingresado sea alfanumérico (letras y números) y no supere los 100 caracteres.
    Si el parámetro `permitir_vacio` es True, permite dejar el campo vacío y retornar el `valor_actual`.
    """
    while True:  # Repite el proceso hasta que se ingrese una entrada válida
        entrada = input(
            mensaje
        ).strip()  # Solicita al usuario el nombre y elimina los espacios al principio y al final

        # Si se permite vacío y el usuario no ingresa nada, retorna el valor actual
        if permitir_vacio and entrada == "":
            return valor_actual

        # Verifica si la longitud del nombre es menor o igual a 100 y si solo contiene caracteres alfanuméricos (incluyendo espacios)
        if len(entrada) <= 100 and entrada.replace(" ", "").isalnum():
            return entrada  # Si es válido, retorna el nombre
        else:
            # Si el nombre no es válido, muestra un mensaje de error
            error_rojo(
                "El nombre debe ser alfanumérico y tener hasta 100 caracteres."
            )  # Llama a la función error_rojo para mostrar el mensaje de error en rojo


# Función para validar el monto de la cuota
def validar_cuota(mensaje, permitir_vacio=False, valor_actual=None):
    """
    Esta función valida que el monto de la cuota esté entre 0 y 999,999 (es decir, hasta 6 dígitos).
    Si el parámetro `permitir_vacio` es True, permite que el campo quede vacío y se devuelva el `valor_actual`.
    """
    while True:  # Repite el proceso hasta que se ingrese una entrada válida
        cuota = input(
            mensaje
        ).strip()  # Solicita al usuario el monto de la cuota y elimina los espacios al principio y al final

        # Si se permite vacío y el usuario no ingresa nada, retorna el valor actual
        if permitir_vacio and not cuota:
            return valor_actual

        # Verifica si la cuota es un número
        if cuota.isdigit():
            cuota = int(cuota)  # Convierte la cuota a entero

            # Verifica si la cuota está dentro del rango permitido (0 - 999,999)
            if 0 <= cuota <= 999999:
                return cuota  # Si es válida, retorna la cuota
        # Si la cuota no es válida, muestra un mensaje de error
        error_rojo(
            "El monto debe ser un número entre 0 y 999,999."
        )  # Llama a la función error_rojo para mostrar el mensaje de error en rojo


# Función para validar la duración
def validar_duracion(mensaje, permitir_vacio=False, valor_actual=None):
    """
    Esta función valida que la duración de algo (por ejemplo, un contrato) esté entre 1 y 60 meses.
    Si el parámetro `permitir_vacio` es True, permite que el campo quede vacío y se devuelva el `valor_actual`.
    """
    while True:  # Repite el proceso hasta que se ingrese una entrada válida
        duracion = input(
            mensaje
        ).strip()  # Solicita al usuario la duración y elimina los espacios al principio y al final

        # Si se permite vacío y el usuario no ingresa nada, retorna el valor actual
        if permitir_vacio and not duracion:
            return valor_actual

        # Verifica si la duración es un número
        if duracion.isdigit():
            duracion = int(duracion)  # Convierte la duración a entero

            # Verifica si la duración está dentro del rango permitido (1 - 60)
            if 1 <= duracion <= 60:
                return duracion  # Si es válida, retorna la duración
        # Si la duración no es válida, muestra un mensaje de error
        error_rojo(
            "La duración debe ser un número entre 1 y 60."
        )  # Llama a la función error_rojo para mostrar el mensaje de error en rojo


# Función para validar el ID de un instructor
def validar_id_instructor(mensaje, conn, permitir_vacio=False, valor_actual=None):
    """
    Esta función valida que el ID del instructor exista en la base de datos.
    Si el parámetro `permitir_vacio` es True, permite que el campo quede vacío y se devuelva el `valor_actual`.
    """
    cursor = (
        conn.cursor()
    )  # Obtiene un cursor para ejecutar consultas SQL en la base de datos
    while True:  # Repite el proceso hasta que se ingrese una entrada válida
        id_instructor = input(
            mensaje
        ).strip()  # Solicita al usuario el ID del instructor y elimina los espacios al principio y al final

        # Si se permite vacío y el usuario no ingresa nada, retorna el valor actual
        if permitir_vacio and not id_instructor:
            return valor_actual

        # Verifica si el ID del instructor es un número
        if id_instructor.isdigit():
            id_instructor = int(id_instructor)  # Convierte el ID a entero

            # Realiza una consulta a la base de datos para verificar si el ID existe en la tabla de instructores
            query = "SELECT * FROM Instructores WHERE ID = %s"
            cursor.execute(
                query, (id_instructor,)
            )  # Ejecuta la consulta con el ID del instructor
            if (
                cursor.fetchone()
            ):  # Si la consulta devuelve algún resultado, significa que el ID existe
                return id_instructor  # Retorna el ID del instructor
            else:
                # Si el ID no existe, muestra un mensaje de error
                error_rojo(
                    f"El ID {id_instructor} no corresponde a un instructor existente."
                )
        else:
            # Si el ID no es un número, muestra un mensaje de error
            error_rojo(
                "El ID del instructor debe ser un número positivo."
            )  # Llama a la función error_rojo para mostrar el mensaje de error en rojo


# Funciones CRUD de Cursos
# Función para crear un nuevo curso
def crear_curso():
    # Inicialización de las variables de conexión y cursor, necesarias para interactuar con la base de datos
    conn = None
    cursor = None

    try:
        # Conectarse a la base de datos
        conn = conectar()
        cursor = conn.cursor()

        # Solicitar datos al usuario para el nuevo curso, utilizando funciones de validación para garantizar la entrada correcta
        nombre = validar_nombre(
            "Ingrese el nombre del curso: "
        )  # Valida que el nombre sea correcto
        cuota = validar_cuota(
            "Ingrese la cuota del curso: "
        )  # Valida que la cuota sea un número correcto
        duracion = validar_duracion(
            "Ingrese la duración del curso en meses: "
        )  # Valida que la duración sea entre 1 y 60 meses
        id_instructor = validar_id_instructor(  # Valida que el ID del instructor exista en la base de datos
            "Ingrese el ID del instructor responsable del curso: ", conn=conn
        )

        # Comando SQL para insertar el nuevo curso en la base de datos
        query = """
            INSERT INTO Cursos (Nombre, Cuota, Duracion, IDInstructor) 
            VALUES (%s, %s, %s, %s)
        """
        # Ejecución del comando de inserción con los valores validados
        cursor.execute(query, (nombre, cuota, duracion, id_instructor))
        # Confirmar los cambios realizados en la base de datos
        conn.commit()
        # Mensaje de éxito
        print("Curso creado exitosamente.")

    except Exception as e:
        # Manejo de errores en caso de que algo salga mal (por ejemplo, errores de conexión o SQL)
        error_rojo(f"Error al crear el curso: {e}.")
    finally:
        # Asegurarse de cerrar el cursor y la conexión aunque haya errores
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# Función para leer todos los cursos
def leer_cursos():
    try:
        # Conectar a la base de datos y crear el cursor
        conn = conectar()
        cursor = conn.cursor()
        # Consulta para obtener todos los cursos registrados
        query = "SELECT * FROM Cursos ORDER BY Codigo" #ACA lo que pidio el profe ORDENADO POR CODIGO
        cursor.execute(query)
        cursos = cursor.fetchall()  # Recuperar todos los resultados de la consulta

        # Crear una tabla para mostrar los cursos de manera ordenada
        tabla = PrettyTable()
        tabla.field_names = [
            "Código",  # Nombre de la columna para el código del curso
            "Nombre",  # Nombre de la columna para el nombre del curso
            "Cuota",  # Nombre de la columna para la cuota del curso
            "Duración (meses)",  # Nombre de la columna para la duración en meses
            "ID Instructor",  # Nombre de la columna para el ID del instructor
        ]

        # Añadir cada curso como una fila en la tabla
        for curso in cursos:
            tabla.add_row(curso)

        # Imprimir la tabla resultante con los cursos
        print("\nListado de Cursos:")
        print(tabla)

    except Exception as e:
        # Manejo de errores, por ejemplo si hay problemas de conexión a la base de datos
        error_rojo(
            f"Error al leer cursos: {e}. Puede deberse a un problema de conexión o a que no existen registros."
        )
    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()


# Función para actualizar un curso existente
def actualizar_curso():
    # Solicitar al usuario el código del curso a modificar, validado para que esté entre 1 y 99
    codigo = validar_codigo("Ingrese código del curso a modificar (1 a 99): ")

    conn = None
    cursor = None

    try:
        # Conectarse a la base de datos
        conn = conectar()
        cursor = conn.cursor()
        # Consultar el curso con el código ingresado
        query = "SELECT * FROM Cursos WHERE Codigo=%s"
        cursor.execute(query, (codigo,))
        curso = cursor.fetchone()  # Recuperar un solo curso con ese código

        if curso:
            # Si se encontró el curso, mostrar los datos actuales
            print("\nDatos actuales del curso:")
            print(f"Nombre: {curso[1]}")
            print(f"Cuota: {curso[2]}")
            print(f"Duración: {curso[3]} meses")
            print(f"ID Instructor: {curso[4]}")

            # Validar y pedir los nuevos valores, permitiendo dejar en blanco para mantener el valor actual
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

            # Comando SQL para actualizar el curso con los nuevos valores
            query_update = """
                UPDATE Cursos 
                SET Nombre=%s, Cuota=%s, Duracion=%s, IDInstructor=%s 
                WHERE Codigo=%s
            """
            # Ejecutar la actualización en la base de datos
            cursor.execute(
                query_update, (nombre, cuota, duracion, id_instructor, codigo)
            )
            # Confirmar los cambios en la base de datos
            conn.commit()
            # Mensaje de éxito
            print("Curso actualizado correctamente.")
        else:
            # Si no se encuentra el curso con el código ingresado
            error_rojo(f"El curso con código {codigo} no existe.")

    except Exception as e:
        # Manejo de errores
        error_rojo(f"Error al actualizar el curso: {e}.")
    finally:
        # Cerrar el cursor y la conexión
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# Función para eliminar un curso
def eliminar_curso():
    # Solicitar al usuario el código del curso a eliminar
    codigo = validar_codigo("Ingrese código del curso a eliminar (1 a 99): ")

    try:
        # Conectarse a la base de datos
        conn = conectar()
        cursor = conn.cursor()
        # Buscar el curso por código
        query = "SELECT * FROM Cursos WHERE Codigo=%s"
        cursor.execute(query, (codigo,))
        curso = cursor.fetchone()  # Recuperar el curso con ese código

        if curso:
            # Si el curso existe, mostrar los datos para confirmación
            print("\nDatos del curso a eliminar:")
            print(
                f"Código: {curso[0]}, Nombre: {curso[1]}, Cuota: {curso[2]}, Duración: {curso[3]} meses, ID Instructor: {curso[4]}"
            )

            # Confirmación de la eliminación
            confirmar = (
                input("¿Está seguro de que desea eliminar este curso? (S/N): ")
                .strip()
                .upper()
            )
            if confirmar == "S":
                # Si el usuario confirma, ejecutar la eliminación en la base de datos
                query_delete = "DELETE FROM Cursos WHERE Codigo=%s"
                cursor.execute(query_delete, (codigo,))
                # Confirmar los cambios realizados
                conn.commit()
                # Mensaje de éxito
                print("Curso eliminado correctamente.")
            else:
                # Si el usuario cancela la operación
                print("Operación cancelada.")
        else:
            # Si no se encuentra el curso con ese código
            error_rojo(f"No se encontró ningún curso con el código {codigo}.")
    except Exception as e:
        # Manejo de errores
        error_rojo(f"Error al eliminar el curso: {e}.")
    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
