import json
def menu_ruta(opcion):
    while True : 
        if opcion == 1:
            crear_nueva_ruta()
            break
        elif opcion == 2:
            agregar_modulo_a_ruta_existente()
            break
        elif opcion == 3:
            consultar_estado_camper()
            print ("\n")
            break
        elif opcion == 4:
            asignar_nota_prueba_inicial()
            break
        elif opcion == 5:
            print("\nVolviendo al menú principal...")
            break
        else:
            print("\nOpción inválida. Por favor, ingrese una opción válida.")
    return

def crear_nueva_ruta():
    while True:
        with open("Rutas.json", "r") as file:
            data = json.load(file)
        nombre_ruta = input("\nIngrese el nombre de la nueva ruta: ")
        modulos = input("\nIngrese los módulos de la nueva ruta separados por comas: ").split(",")
        nueva_ruta = {
            "nombre": nombre_ruta,
            "modulos": modulos
        }
        data["rutas_entrenamiento"].append(nueva_ruta)
        with open("Rutas.json", "w") as file:
            json.dump(data, file, indent=4)
        print("\nNueva ruta creada exitosamente.")
        continuar = input("¿Desea agregar otra ruta? (s/n): ")
        if continuar.lower() != "s":
            break

def agregar_modulo_a_ruta_existente():
    while True:
        with open("Rutas.json", "r") as file:
            data = json.load(file)
        print("\nRutas de entrenamiento existentes:")
        for index, ruta in enumerate(data["rutas_entrenamiento"], start=1):
            print(f"{index}. {ruta['nombre']}")
        ruta_index = int(input("\nSeleccione el número de la ruta a la que desea agregar un módulo (0 para volver al menú principal): ")) - 1
        if ruta_index == -1:
            print("\nVolviendo al Menú Principal...")
            break
        if ruta_index < 0 or ruta_index >= len(data["rutas_entrenamiento"]):
            print("\n¡Número de ruta inválido!")
            continue
        ruta_seleccionada = data["rutas_entrenamiento"][ruta_index]
        nuevo_modulo = input("\nIngrese el nombre del nuevo módulo: ")
        ruta_seleccionada["modulos"].append(nuevo_modulo)
        with open("Rutas.json", "w") as file:
            json.dump(data, file, indent=4)
        
        print(f"¡El módulo '{nuevo_modulo}' ha sido agregado a la ruta '{ruta_seleccionada['nombre']}' con éxito!") 
