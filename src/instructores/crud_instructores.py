from prettytable import PrettyTable
from ..database.conexion import conectar

# Funciones de validación
def validar_entrada_entero(mensaje, min_valor=1):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < min_valor:
                raise ValueError(f"El valor debe ser mayor o igual a {min_valor}.")
            return valor
        except ValueError as e:
            print(f"Entrada no válida: {e}")

def validar_entrada_cadena(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        else:
            print("La entrada no puede estar vacía.")

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
        print(f"Error al crear el instructor: {e}")
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
        print(f"Error al leer instructores: {e}")
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
        print(f"Error al actualizar el instructor: {e}")
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
        print("Instructor eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar el instructor: {e}")
    finally:
        cursor.close()
        conn.close()
