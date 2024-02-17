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
            asignar_camper_a_ruta()
            print ("\n")
            break
        elif opcion == 4:
            asignar_estudiante_a_area()
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
def asignar_camper_a_ruta():
    while True:
        with open("Camper.json", "r") as file:
            data_campers = json.load(file)
        
        with open("Rutas.json", "r") as file:
            data_rutas = json.load(file)
        print("\nRutas de entrenamiento disponibles:")
        for index, ruta in enumerate(data_rutas["rutas_entrenamiento"], start=1):
            print(f"{index}. {ruta['nombre']}")
        ruta_index = int(input("Seleccione el número de la ruta a la que desea asignar un camper: ")) - 1
        if ruta_index < 0 or ruta_index >= len(data_rutas["rutas_entrenamiento"]):
            print("¡Número de ruta inválido!")
            continue
        ruta_seleccionada = data_rutas["rutas_entrenamiento"][ruta_index]
        print("\nCampers disponibles para asignar:")
        for camper in data_campers["campers"]:
            if camper["estado"] == "En proceso de ingreso":
                print(f"- {camper['nombres']} {camper['apellidos']} (ID: {camper['id']})")
        camper_id = int(input("\nIngrese el ID del camper que desea asignar (0 para cancelar): "))
        if camper_id == 0:
            print("\nAsignación cancelada.")
            break
        camper_encontrado = False
        for camper in data_campers["campers"]:
            if camper["id"] == camper_id:
                camper["ruta_asignada"] = ruta_seleccionada["nombre"]
                print(f"\n¡El camper {camper['nombres']} {camper['apellidos']} ha sido asignado a la ruta '{ruta_seleccionada['nombre']}' con éxito!")
                camper_encontrado = True
                break
        if not camper_encontrado:
            print("\n¡ID de camper inválido!")
        with open("Camper.json", "w") as file:
            json.dump(data_campers, file, indent=4)


import json

def asignar_estudiante_a_area():
    with open("Camper.json", "r") as file:
        data_estudiantes = json.load(file)
    
    with open("SalasEntrenamiento.json", "r") as file:
        data_areas = json.load(file)
    
    print("\nÁreas de entrenamiento disponibles:")
    for index, area in enumerate(data_areas, start=1):
        print(f"{index}. {area['nombre']} - Capacidad máxima: {area['capacidad_maxima']}")
    
    while True:
        area_index = int(input("\nSeleccione el número del área de entrenamiento a la que desea asignar un estudiante (0 para cancelar): ")) - 1
        
        if area_index == -1:
            print("\nOperación cancelada.")
            break
        
        if area_index < 0 or area_index >= len(data_areas):
            print("\n¡Número de área inválido!")
            continue
        
        area_seleccionada = data_areas[area_index]
        
        ruta_estudiante = input("\nIngrese la ruta de entrenamiento del estudiante: ")
        estudiantes_ruta = [estudiante for estudiante in data_estudiantes['campers'] if estudiante.get("ruta_asignada", "").lower() == ruta_estudiante.lower() and estudiante.get("estado") == "Aprobado"]
        
        if len(estudiantes_ruta) == 0:
            print("\nNo hay estudiantes aprobados disponibles para asignar en esta ruta.")
            continue
        
        print("\nEstudiantes disponibles para asignar:")
        for index, estudiante in enumerate(estudiantes_ruta, start=1):
            print(f"{index}. {estudiante['nombres']} {estudiante['apellidos']}")
        
        while True:
            estudiante_index = int(input("\nSeleccione el número del estudiante que desea asignar (0 para cancelar): ")) - 1
            
            if estudiante_index == -1:
                print("\nOperación cancelada.")
                break
            
            if estudiante_index < 0 or estudiante_index >= len(estudiantes_ruta):
                print("\n¡Número de estudiante inválido!")
                continue
            
            estudiante_seleccionado = estudiantes_ruta[estudiante_index]
            
            if area_seleccionada["capacidad_maxima"] <= 0:
                print(f"\nNo hay capacidad disponible en el área de entrenamiento '{area_seleccionada['nombre']}'.")
                break
            
            area_seleccionada["capacidad_maxima"] -= 1
            if "estudiantes" not in area_seleccionada:
                area_seleccionada["estudiantes"] = []
            area_seleccionada["estudiantes"].append(estudiante_seleccionado)
            
            print(f"\n¡El estudiante {estudiante_seleccionado['nombres']} {estudiante_seleccionado['apellidos']} ha sido asignado al área de entrenamiento '{area_seleccionada['nombre']}' con éxito!")
            print(f"\nCapacidad restante en el área de entrenamiento '{area_seleccionada['nombre']}': {area_seleccionada['capacidad_maxima']}")
            break

    with open("SalasEntrenamiento.json", "w") as file:
        json.dump(data_areas, file, indent=4)


