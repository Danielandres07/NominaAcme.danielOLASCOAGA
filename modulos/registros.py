import json
from datetime import datetime

def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
 #guardar datos 
def guardar_datos(archivo, datos):
    with open(archivo, 'w') as f:
        json.dump(datos, f, indent=4)
        
#  registrar un empleado
def registrar_empleado():
    empleados = cargar_datos('empleados.json')
    identificacion = input("Ingrese la identificación del empleado: ")



 # empleado ya existente
    if encontrar_empleado(empleados, identificacion) is not None:
        print("El empleado ya está registrado.")
        return

    nombre = input("Ingrese el nombre del empleado: ")
    cargo = input("Ingrese el cargo del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))

    empleado = {
        'identificacion': identificacion,
        'nombre': nombre,
        'cargo': cargo,
        'salario': salario,
        'inasistencias': [],
        'bonos': []
    }
    empleados.append(empleado)
    guardar_datos('empleados.json', empleados)
    print("Empleado registrado exitosamente.")

# encontrar un empleado por identificación
def encontrar_empleado(empleados, identificacion):
    for empleado in empleados:
        if empleado['identificacion'] == identificacion:
            return empleado
    return None


# inasistencia
def registrar_inasistencia():
    empleados = cargar_datos('empleados.json')
    identificacion = input("Ingrese la identificación del empleado: ")
    
    empleado = encontrar_empleado(empleados, identificacion)
    if not empleado:
        print("Empleado no encontrado.")
        return

    fecha_falta = input("Ingrese la fecha de la falta (dd-mm-yyyy): ")
    try:
        datetime.strptime(fecha_falta, '%d-%m-%Y')  
        empleado['inasistencias'].append(fecha_falta)
        guardar_datos('empleados.json', empleados)
        print("Inasistencia registrada exitosamente.")
    except ValueError:
        print("Formato de fecha inválido. Use dd-mm-yyyy.")

# bono extra-legal
def registrar_bono():
    empleados = cargar_datos('empleados.json')
    identificacion = input("Ingrese la identificación del empleado: ")

    empleado = encontrar_empleado(empleados, identificacion)
    if not empleado:
        print("Empleado no encontrado.")
        return

    fecha_bono = input("Ingrese la fecha del bono (dd-mm-yyyy): ")
    try:
        datetime.strptime(fecha_bono, '%d-%m-%Y')  
        valor_bono = float(input("Ingrese el valor del bono: "))
        concepto_bono = input("Ingrese el concepto del bono: ")

        bono = {'fecha': fecha_bono, 'valor': valor_bono, 'concepto': concepto_bono}
        empleado['bonos'].append(bono)
        guardar_datos('empleados.json', empleados)
        print("Bono registrado exitosamente.")
    except ValueError:
        print("Formato de fecha o valor inválido.")