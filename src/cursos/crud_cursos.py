# Funciones de validación
def validar_entrada_entero(mensaje, min_valor=1, max_valor=None):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < min_valor or (max_valor and valor > max_valor):
                raise ValueError(
                    f"El valor debe estar entre {min_valor} y {max_valor}."
                )
            return valor
        except ValueError as e:
            error_rojo(
                f"Entrada no válida: {e}. Se esperaba un número entre {min_valor} y {max_valor}."
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
    codigo = validar_entrada_entero("Ingrese código del curso (1 a 99): ", 1, 99)
    nombre = validar_entrada_cadena("Ingrese nombre del curso: ")
    cuota = validar_entrada_entero("Ingrese cuota del curso (0 a 999,999): ", 0, 999999)
    duracion = validar_entrada_entero(
        "Ingrese duración del curso en meses (1 a 60): ", 1, 60
    )
    id_instructor = validar_entrada_entero(
        "Ingrese ID del instructor (1 a 99): ", 1, 99
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
        "Ingrese código del curso a modificar (1 a 99): ", 1, 99
    )

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

            nombre = validar_entrada_cadena(
                input(
                    f"Nuevo nombre del curso (dejar vacío para mantener '{curso[1]}'): "
                )
                or curso[1]
            )
            cuota = validar_entrada_entero(
                input(
                    f"Nueva cuota del curso (dejar vacío para mantener '{curso[2]}'): "
                )
                or curso[2],
                0,
                999999,
            )
            duracion = validar_entrada_entero(
                input(
                    f"Nueva duración del curso en meses (dejar vacío para mantener '{curso[3]}'): "
                )
                or curso[3],
                1,
                60,
            )
            id_instructor = validar_entrada_entero(
                input(
                    f"Nuevo ID del instructor (dejar vacío para mantener '{curso[4]}'): "
                )
                or curso[4],
                1,
                99,
            )

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
        cursor.close()
        conn.close()


def eliminar_curso():
    codigo = validar_entrada_entero(
        "Ingrese código del curso a eliminar (1 a 99): ", 1, 99
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
