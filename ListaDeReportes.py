import json
def menu_reportes(opcion):
    while True : 
        if opcion == 1:
            mostrar_campers()
            break
        elif opcion == 2:
            mostrar_camper_aprobados()
            break
        elif opcion == 3:
            mostrar_entrenadores()
            print ("\n")
            break
        elif opcion == 4:
            mostrar_campers_bajo_rendimiento()
            break
        elif opcion == 5:
            listar_campers_y_trainers_por_ruta()
            break
        elif opcion == 6 : 
            Estadisticas_Modulos()
            break 
        elif opcion == 7 : 
            print ("\n Volviendo al menu principal...")
            break
        else:
            print("\nOpción inválida. Por favor, ingrese una opción válida.")
    return

def mostrar_campers():
    with open("Camper.json", "r") as file: 
        campers_json = json.load(file) 
    campers = campers_json["campers"]
    
    # Mostrar información de cada camper
    print("\nCampers Registrados:")
    for camper in campers:
        print(f"ID: {camper['id']}")
        print(f"Nombres: {camper['nombres']}")
        print(f"Apellidos: {camper['apellidos']}")
        print(f"Dirección: {camper['direccion']}")
        print(f"Acudiente: {camper['acudiente']}")
        print("Teléfonos:")
        print(f"  Celular: {camper['telefonos']['celular']}")
        print(f"  Fijo: {camper['telefonos']['fijo']}")
        print(f"Estado: {camper['estado']}")
        print()

def mostrar_camper_aprobados():
    with open("Camper.json", "r") as file:
        campers_json = json.load(file)

    campers = campers_json["campers"]
    
    print("\nCampers Aprobados:")
    for camper in campers:
        if camper['estado'] == "Aprobado":
            print(f"ID: {camper['id']}")
            print(f"Nombres: {camper['nombres']}")
            print(f"Apellidos: {camper['apellidos']}")
            print(f"Estado: {camper['estado']}")
            print()

def mostrar_entrenadores() : 
    with open ('Entrenadores.json', 'r') as file : 
        entrenadores_json = json.load(file)
        
    for entrenadores in entrenadores_json : 
        print (f" Identificacion: {entrenadores['identificacion']}")
        print (f" Nombres: {entrenadores['nombre']}")
        print (f" Apellidos: {entrenadores['apellidos']}")
        print ()

def mostrar_campers_bajo_rendimiento():
    with open("Camper.json", "r") as file:
        campers_json = json.load(file)

    campers = campers_json["campers"]

    print("\nCampers con Bajo Rendimiento:")
    for camper in campers:
        if camper["estado"] == "Riesgo de Expulsión":
            for modulo in camper.get("notas_modulos", []):
                for materia, nota in modulo.items():
                    if nota["final"] < 60:
                        print(f"Nombre: {camper['nombres']} {camper['apellidos']}")
                        print(f"Módulo: {materia}")
                        print(f"Nota Final: {nota['final']}\n")
                        break  


def listar_campers_y_trainers_por_ruta():
    with open("Rutas.json", "r") as file:
        rutas_entrenamiento = json.load(file)["rutas_entrenamiento"]
    
    with open("Camper.json", "r") as file:
        campers = json.load(file)["campers"]
        
    ruta_deseada = input("Ingrese el nombre de la ruta de entrenamiento: ")
    ruta_encontrada = None
    for ruta in rutas_entrenamiento:
        if ruta["nombre"] == ruta_deseada:
            ruta_encontrada = ruta
            break
    
    if ruta_encontrada is None:
        print("La ruta de entrenamiento especificada no existe.")
        return
    
    print(f"\nDetalles de la Ruta de Entrenamiento '{ruta_encontrada['nombre']}':")
    print("Módulos:", ', '.join(ruta_encontrada["modulos"]))
    
    trainer_asignado = ruta_encontrada.get("entrenador_asignado")
    if trainer_asignado:
        print("Trainer Encargado:", f"{trainer_asignado['nombre']} {trainer_asignado['apellidos']}")
    else:
        print("Trainer Encargado: No asignado")
    
    print("\nCampers Asociados a la Ruta:")

    for camper in campers:
        if camper["ruta_asignada"] == ruta_deseada:
            print(f"- {camper['nombres']} {camper['apellidos']}")


def Estadisticas_Modulos():
    # Cargar el archivo JSON de campers
    with open("Camper.json", "r") as file:
        campers_data = json.load(file)

    # Iterar sobre cada camper
    for camper in campers_data["campers"]:
        print(f"Estudiante: {camper['nombres']} {camper['apellidos']}")
        print("\nRuta asignada:", camper["ruta_asignada"])
        
        print("\nNotas por módulo:")
        if not camper["ruta_asignada"] in camper :
            print(f"Estudiante: {camper['nombres']} {camper['apellidos']}")
            

        # Iterar sobre las notas de los módulos del estudiante
        for modulo in camper.get("notas_modulos", []):
            for modulo_nombre, nota_info in modulo.items():
                print(f"\tMódulo: {modulo_nombre}")
                print(f"\t- Nota teórica: {nota_info['teorica']}")
                print(f"\t- Nota práctica: {nota_info['practica']}")
                print(f"\t- Nota de quiz: {nota_info['quiz']}")
                print(f"\t- Estado del módulo: {nota_info['estado']}")
                print()
            if not modulo in camper.get("notas_modulos",[]):
                print("\n\tNo se encontraron notas para este módulo.") 