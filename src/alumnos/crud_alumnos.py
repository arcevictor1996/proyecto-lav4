from prettytable import PrettyTable
from ..database.conexion import conectar

# Funciones de validación
def validar_entrada_cadena(mensaje, min_length=1):
    while True:
        entrada = input(mensaje).strip()
        if len(entrada) >= min_length:
            return entrada
        else:
            print(f"La entrada debe tener al menos {min_length} caracteres.")

def validar_entrada_entero(mensaje, min_valor=1):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < min_valor:
                raise ValueError(f"El valor debe ser mayor o igual a {min_valor}.")
            return valor
        except ValueError as e:
            print(f"Entrada no válida: {e}")

def validar_entrada_dni(mensaje):
    while True:
        dni = input(mensaje).strip()
        if len(dni) == 8 and dni.isdigit():
            return dni
        else:
            print("DNI inválido. Debe tener 8 dígitos numéricos.")

# Funciones CRUD de Alumnos
def crear_alumno():
    nombre = validar_entrada_cadena("Ingrese nombre del alumno: ")
    apellido = validar_entrada_cadena("Ingrese apellido del alumno: ")
    telefono = input("Ingrese teléfono del alumno: ")
    direccion = input("Ingrese dirección del alumno: ")
    dni = validar_entrada_dni("Ingrese DNI del alumno: ")

    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "INSERT INTO Alumnos (Nombre, Apellido, Telefono, Direccion, DNI) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (nombre, apellido, telefono, direccion, dni))
        conn.commit()
        print("Alumno creado correctamente.")
    except Exception as e:
        print(f"Error al crear el alumno: {e}")
    finally:
        cursor.close()
        conn.close()

def leer_alumnos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "SELECT * FROM Alumnos"
        cursor.execute(query)
        alumnos = cursor.fetchall()

        # Crear la tabla con encabezados
        tabla = PrettyTable()
        tabla.field_names = ["Legajo", "Apellido", "Nombre", "Teléfono", "Dirección", "DNI"]

        # Añadir las filas con los datos de los alumnos
        for alumno in alumnos:
            tabla.add_row(alumno)

        # Imprimir la tabla
        print("\nListado de Alumnos:")
        print(tabla)

    except Exception as e:
        print(f"Error al leer alumnos: {e}")
    finally:
        cursor.close()
        conn.close()

def actualizar_alumno():
    legajo = validar_entrada_entero("Ingrese el legajo del alumno a modificar: ")
    nombre = validar_entrada_cadena("Nuevo nombre del alumno: ")
    apellido = validar_entrada_cadena("Nuevo apellido del alumno: ")
    telefono = input("Nuevo teléfono del alumno: ")
    direccion = input("Nueva dirección del alumno: ")
    dni = validar_entrada_dni("Nuevo DNI del alumno: ")

    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "UPDATE Alumnos SET Nombre=%s, Apellido=%s, Telefono=%s, Direccion=%s, DNI=%s WHERE Legajo=%s"
        cursor.execute(query, (nombre, apellido, telefono, direccion, dni, legajo))
        conn.commit()
        print("Alumno actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar el alumno: {e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_alumno():
    legajo = validar_entrada_entero("Ingrese el legajo del alumno a eliminar: ")

    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "DELETE FROM Alumnos WHERE Legajo=%s"
        cursor.execute(query, (legajo,))
        conn.commit()
        print("Alumno eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar el alumno: {e}")
    finally:
        cursor.close()
        conn.close()
