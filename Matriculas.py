import json 
def menu_matriculas(opcion):
    while True : 
        if opcion == 1:
            matriculas()
            break
        elif opcion == 2:
            asignar_notas_modulos()
            break
        elif opcion == 3:
            print ("\n Volviendo al menu principal")
            break
        else:
            print("\nOpción inválida. Por favor, ingrese una opción válida.")
    return

def asignar_notas_modulos():
    with open("Rutas.json", "r") as file:
        rutas_entrenamiento = json.load(file)["rutas_entrenamiento"]
    
    with open("Camper.json", "r") as file:
        estudiantes = json.load(file)["campers"]
    
    id_estudiante = int(input("Ingrese la identificación del estudiante: "))
    
    estudiante = None
    for camper in estudiantes:
        if camper["id"] == id_estudiante:
            estudiante = camper
            break
    
    if estudiante:
        ruta_estudiante = estudiante["ruta_asignada"]
        ruta_correspondiente = None
        for ruta in rutas_entrenamiento:
            if ruta["nombre"] == ruta_estudiante:
                ruta_correspondiente = ruta
                break
        if ruta_correspondiente:

            modulos_estudiante = ruta_correspondiente.get("modulos", [])
            notas_modulos_estudiante = []

            for modulo in modulos_estudiante:
                nota_teorica = float(input(f"Ingrese la nota teórica para el módulo '{modulo}': "))
                nota_practica = float(input(f"Ingrese la nota práctica para el módulo '{modulo}': "))
                nota_quiz = float(input(f"Ingrese la nota del quiz para el módulo '{modulo}': "))
                nota_final = (nota_teorica * 0.3) + (nota_practica * 0.6) + (nota_quiz * 0.1)
                notas_modulo = {
                    "teorica": nota_teorica,
                    "practica": nota_practica,
                    "quiz": nota_quiz,
                    "final": nota_final,
                    "estado": "Aprobado" if nota_final >= 60 else "Reprobado"
                }
                notas_modulos_estudiante.append({modulo: notas_modulo})

            estudiante["notas_modulos"] = notas_modulos_estudiante
            contador_reprobados = 0
            for modulo in notas_modulos_estudiante:
                if modulo[list(modulo.keys())[0]]["estado"] == "Reprobado":
                    contador_reprobados += 1
                    if contador_reprobados > 2:
                        estudiante["estado"] = "Riesgo de Expulsión"
                        estudiante['riesgo'] = "Alto"
                        break
            else:
                estudiante["estado"] = "Aprobado"
                
            with open("Camper.json", "w") as file:
                json.dump({"campers": estudiantes}, file, indent=4)

            print("Notas asignadas correctamente.")
        else:
            print("No se encontró la ruta de entrenamiento correspondiente.")
    else:
        print("No se encontró al estudiante con la identificación proporcionada.")
import json

def matriculas():
    with open("SalasEntrenamiento.json", "r") as file:
        salas_entrenamiento = json.load(file)
    
    print("\nSalas de Entrenamiento Disponibles:")
    for index, sala in enumerate(salas_entrenamiento, start=1):
        print(f"{index}. {sala['nombre']}")
    
    sala_index = int(input("\nIngrese el número de la sala que desea ver: ")) - 1
    if sala_index < 0 or sala_index >= len(salas_entrenamiento):
        print("¡Número de sala inválido!")
        return
    
    sala_seleccionada = salas_entrenamiento[sala_index]

    print(f"\nDetalles de la Sala {sala_seleccionada['nombre']}:")
    print(f"Nombre: {sala_seleccionada['nombre']}")
    print(f"Capacidad Máxima: {sala_seleccionada['capacidad_maxima']}")
    print(f"Horarios Disponibles: {', '.join(sala_seleccionada['horarios_disponibles'])}")

    if "entrenadores" in sala_seleccionada:
        print("\nEntrenador(es) asignado(s):")
        for entrenador in sala_seleccionada["entrenadores"]:
            print(f"- {entrenador['nombre']} {entrenador['apellidos']}")
    else:
        print("\nNo hay entrenadores asignados a esta sala.")
    
    if "estudiantes" in sala_seleccionada:
        print("\nEstudiantes asignados:")
        for estudiante in sala_seleccionada["estudiantes"]:
            print(f"- {estudiante['nombres']} {estudiante['apellidos']} (ID: {estudiante['id']})")
    else:
        print("\nNo hay estudiantes asignados a esta sala.")

    fecha_inicio = input("\nIngrese la fecha de inicio (DD/MM/AAAA): ")
    fecha_finalizacion = input("Ingrese la fecha de finalización (DD/MM/AAAA): ")
    
    sala_seleccionada["fecha_inicio"] = fecha_inicio
    sala_seleccionada["fecha_finalizacion"] = fecha_finalizacion

    with open("SalasEntrenamiento.json", "w") as file:
        json.dump(salas_entrenamiento, file, indent=4)
    
    print("\n¡Consulta realizada con éxito!")

