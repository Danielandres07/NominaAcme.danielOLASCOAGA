import json
from datetime import datetime

SALARIO_MINIMO = 1000000
AUXILIO_TRANSPORTE = 0.10
DESCUENTO_SALUD = 0.04
DESCUENTO_PENSION = 0.04
VALOR_DIA_TRABAJO = 30

def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Función para calcular la nómina y generar archivos
def calcular_nomina():
    empleados = cargar_datos('empleados.json')
    
    for empleado in empleados:
        salario_base = empleado['salario']
        faltas = len(empleado['inasistencias'])
        total_bonos = sum(b['valor'] for b in empleado['bonos'])


        # Generar archivo de nómina para el empleado
        nombre_archivo = f"{empleado['identificacion']}."
        with open(nombre_archivo, 'w') as f:
            print(f"Identificación: {empleado['identificacion']}\n")
            print(f"Nombre: {empleado['nombre']}\n")
            print(f"Cargo: {empleado['cargo']}\n")
            print(f"Salario Base: {salario_base}\n")
            print(f"Descuento Salud (4%): {descuento_salud}\n")
            print(f"Descuento Pensión (4%): {descuento_pension}\n")
            print(f"Descuento por faltas: {descuento_faltas}\n")
            print(f"Auxilio de transporte: {auxilio_transporte}\n")
            print(f"Bonos extra-legales: {total_bonos}\n")
            print(f"Total a pagar: {total_pagar}\n")
        print(f"Nómina generada para {empleado['nombre']} ({empleado['identificacion']})")

        # Descuentos por salud y pensión
        descuento_salud = salario_base * DESCUENTO_SALUD
        descuento_pension = salario_base * DESCUENTO_PENSION

        # Descuento por inasistencias
        descuento_faltas = (salario_base / VALOR_DIA_TRABAJO) * faltas

        # Auxilio de transporte si el salario es menor a 2 salarios mínimos
        auxilio_transporte = salario_base * AUXILIO_TRANSPORTE if salario_base < 2 * SALARIO_MINIMO else 0

        # Cálculo del salario final
        total_pagar = salario_base - descuento_salud - descuento_pension - descuento_faltas + auxilio_transporte + total_bonos