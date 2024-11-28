from prettytable import PrettyTable
from ..database.conexion import conectar

#Validaciones para los datos
def validar_nombre(campo, tipo):
    while True:
        try:
            if not campo.isalpha():
                raise ValueError(f"El {tipo} debe contener solo letras.")
            return campo
        except ValueError as e:
            print(f"Error: {e}")
            campo = input(f"Ingrese un {tipo} válido: ")

def validar_apellido(campo, apellido):
    while True:
        try:
            if not campo.isalpha():
                raise ValueError(f"El {apellido} debe contener solo letras.")
            return campo
        except ValueError as e:
            print(f"Error: {e}")
            campo = input(f"Ingrese un {apellido} válido: ")

def validar_telefono(telefono):
    while True:
        try:
            if not telefono.isdigit():
                raise ValueError("El teléfono debe contener solo números.")
            return telefono
        except ValueError as e:
            print(f"Error: {e}")
            telefono = input("Ingrese un teléfono válido: ")

def validar_dni(dni):
    while True:
        try:
            if not dni.isdigit() or len(dni) != 8:
                raise ValueError("El DNI debe ser un número de 8 dígitos.")
            return dni
        except ValueError as e:
            print(f"Error: {e}")
            dni = input("Ingrese un DNI válido: ")

def validar_direccion(direccion):
    while True:
        try:
            if len(direccion.strip()) == 0:
                raise ValueError("La dirección no puede estar vacía.")
            return direccion
        except ValueError as e:
            print(f"Error: {e}")
            direccion = input("Ingrese una dirección válida: ")

def validar_legajo(legajo):
    while True:
        try:
            if not legajo.isdigit() or len(legajo) != 6:
                raise ValueError("El legajo debe ser un número de 6 dígitos.")
            return legajo
        except ValueError as e:
            print(f"Error: {e}")
            legajo = input("Ingrese un legajo válido: ")

#funcion crud: crear alumno
def crear_alumno():
    #solicitar y validar datos
    nombre = validar_nombre(input("Ingrese nombre del alumno: "), "nombre")
    apellido = validar_apellido(input("Ingrese apellido del alumno: "), "apellido")
    telefono = validar_telefono(input("Ingrese teléfono del alumno: "))
    direccion = validar_direccion(input("Ingrese dirección del alumno: "))
    dni = validar_dni(input("Ingrese DNI del alumno: "))

    #conexion y ejecución de consulta
    conn = conectar()
    cursor = conn.cursor()
    query = """
        INSERT INTO Alumnos (Nombre, apellido, Telefono, direccion, dni) 
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nombre, apellido, telefono, direccion, dni))
    conn.commit()
    print("Alumno creado correctamente.")
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
    legajo = validar_legajo("Ingrese el legajo del alumno a modificar: ")
    nombre = validar_nombre("Nuevo nombre del alumno: ")
    apellido = validar_apellido("Nuevo apellido del alumno: ")
    telefono = validar_telefono(input("Nuevo teléfono del alumno: "))
    direccion = validar_direccion(input("Nueva dirección del alumno: "))
    dni = validar_dni("Nuevo DNI del alumno: ")

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
    legajo = validar_legajo("Ingrese el legajo del alumno a eliminar: ")

    
    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "DELETE FROM Alumnos WHERE Legajo=%s"
        cursor.execute(query, (legajo,))
        conn.commit()

        if cursor.rowcount == 0:
            print("No se encontró ningún alumno con el legajo proporcionado.")
        else:
            print("Alumno eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar el alumno: {e}")

    finally:
        cursor.close()
        conn.close()