import json
from datetime import datetime
from modulos.registros import *
from modulos.nomina import *
import time
# Menú principal
def menu():
    while True:
        time.sleep(1) 
        print("____________NOMINA__________") 
        print("")
        print("1. Registrar empleado")
        print("2. Registrar inasistencia")
        print("3. Registrar bono extra-legal")
        print("4. Calcular nómina")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            registrar_inasistencia()
        elif opcion == "3":
            registrar_bono()
        elif opcion == "4":
            calcular_nomina()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
menu()