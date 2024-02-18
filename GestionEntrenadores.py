import json
def menu_entrenadores(opcion):
    while True : 
        if opcion == 1:
            registrar_nuevo_entrenador()
            break
        elif opcion == 2:
            asignar_entrenador_a_ruta()
            break
        elif opcion == 3:
            mostrar_entrenador_asignado()
            print ("\n")
            break
        elif opcion == 4:
            asignar_entrenador_a_sala()
            break
        elif opcion == 5:
            print("\nVolviendo al menú principal...")
            break
        else:
            print("\nOpción inválida. Por favor, ingrese una opción válida.")
    return

def registrar_nuevo_entrenador():
    while True:
        identificacion = int(input("Ingrese el número de identificación del nuevo entrenador: "))
        nombre = input("Ingrese el nombre del nuevo entrenador: ")
        apellidos = input("Ingrese los apellidos del nuevo entrenador: ")
        horarios_disponibles = input("Ingrese los horarios disponibles del nuevo entrenador separados por comas: ").split(",")
        nuevo_entrenador = {
            "identificacion": identificacion,
            "nombre": nombre,
            "apellidos": apellidos,
            "horarios_disponibles": horarios_disponibles
        }
        with open("Entrenadores.json", "r") as file:
            datos_entrenadores = json.load(file)
        datos_entrenadores.append(nuevo_entrenador)
        with open("Entrenadores.json", "w") as file:
            json.dump(datos_entrenadores, file, indent=4)

        print("¡Nuevo entrenador registrado con éxito!")

        continuar = input("¿Desea registrar otro entrenador? (s/n): ")
        if continuar.lower() != 's':
            break
    return

def asignar_entrenador_a_ruta():
    # Cargar datos de rutas y entrenadores desde los archivos JSON
    with open("Rutas.json", "r") as file:
        rutas_disponibles = json.load(file)["rutas_entrenamiento"]
    with open("Entrenadores.json", "r") as file:
        entrenadores_disponibles = json.load(file)

    print("Rutas de entrenamiento disponibles:")
    for idx, ruta in enumerate(rutas_disponibles, start=1):
        print(f"{idx}. {ruta['nombre']}")

    opcion_ruta = int(input("Seleccione el número de la ruta a la que desea asignar un entrenador: "))
    ruta_seleccionada = rutas_disponibles[opcion_ruta - 1]

    print("\nEntrenadores disponibles:")
    for idx, entrenador in enumerate(entrenadores_disponibles, start=1):
        print(f"{idx}. {entrenador['nombre']} {entrenador['apellidos']} ")

    opcion_entrenador = int(input("Seleccione el número del entrenador que desea asignar a la ruta: "))
    entrenador_seleccionado = entrenadores_disponibles[opcion_entrenador - 1]

    ruta_seleccionada["entrenador_asignado"] = {
        "nombre": entrenador_seleccionado["nombre"],
        "apellidos": entrenador_seleccionado["apellidos"],
    }

    with open("Rutas.json", "w") as file:
        json.dump({"rutas_entrenamiento": rutas_disponibles}, file, indent=4)

    print("Entrenador asignado a la ruta con éxito.")

def mostrar_entrenador_asignado():
    # Cargar los datos de las rutas desde el archivo JSON
    with open("Rutas.json", "r") as file:
        rutas_disponibles = json.load(file)["rutas_entrenamiento"]

    print("Rutas de entrenamiento disponibles:")
    for idx, ruta in enumerate(rutas_disponibles, start=1):
        print(f"{idx}. {ruta['nombre']}")
    

    while True:
        opcion = input("\nSeleccione el número de la ruta para ver el entrenador asignado (0 para cancelar): ")
        if opcion == "0":
            print("Operación cancelada.")
            return
        elif opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(rutas_disponibles):
                ruta_seleccionada = rutas_disponibles[opcion - 1]["nombre"]
                break
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")

    for ruta_disponible in rutas_disponibles:
        if ruta_disponible["nombre"] == ruta_seleccionada:
            if "entrenador_asignado" in ruta_disponible:
                print(f"\nEntrenador asignado a la ruta {ruta_disponible['nombre']}:")
                entrenador = ruta_disponible["entrenador_asignado"]
                print(f"Nombre: {entrenador['nombre']} {entrenador['apellidos']}")
                break
            else:
                print(f"\nNo hay entrenador asignado a la ruta {ruta_disponible['nombre']}.")
                break
    else:
        print("Ruta no encontrada.")

def asignar_entrenador_a_sala():
    # Cargar datos de las salas de entrenamiento y las rutas de entrenamiento
    with open("SalasEntrenamiento.json", "r") as file:
        salas_entrenamiento = json.load(file)
    
    with open("Rutas.json", "r") as file:
        rutas_entrenamiento = json.load(file)["rutas_entrenamiento"]

    print("\nSalas de entrenamiento disponibles:")
    for index, sala in enumerate(salas_entrenamiento, start=1):
        horarios_disponibles = sala.get("horarios_disponibles", "No especificados")
        print(f"{index}. {sala['nombre']} - Horarios disponibles: {', '.join(horarios_disponibles)}")
    

    sala_index = int(input("\nSeleccione el número de la sala de entrenamiento a la que desea asignar un entrenador (0 para cancelar): ")) - 1
    if sala_index == -1:
        print("\nOperación cancelada.")
        return
    if sala_index < 0 or sala_index >= len(salas_entrenamiento):
        print("\n¡Número de sala inválido!")
        return
    
    sala_seleccionada = salas_entrenamiento[sala_index]

    ruta_estudiantes_sala = set([estudiante["ruta_asignada"] for estudiante in sala_seleccionada.get("estudiantes", [])])

    print("\nEntrenadores disponibles para asignar:")
    for index, ruta in enumerate(rutas_entrenamiento, start=1):
        entrenador_asignado = ruta.get("entrenador_asignado", {})
        nombre_entrenador = f"{entrenador_asignado.get('nombre', 'Sin asignar')} {entrenador_asignado.get('apellidos', '')}"
        print(f"{index}. {ruta['nombre']} - Entrenador Asignado: {nombre_entrenador}")

    ruta_index = int(input("\nSeleccione el número de la ruta de entrenamiento del entrenador que desea asignar (0 para cancelar): ")) - 1
    if ruta_index == -1:
        print("\nOperación cancelada.")
        return
    if ruta_index < 0 or ruta_index >= len(rutas_entrenamiento):
        print("\n¡Número de ruta inválido!")
        return
    
    ruta_seleccionada = rutas_entrenamiento[ruta_index]
    entrenador_asignado = ruta_seleccionada.get("entrenador_asignado")

    if "entrenadores" not in sala_seleccionada:
        sala_seleccionada["entrenadores"] = []
    
    sala_seleccionada["entrenadores"].append(entrenador_asignado)

    with open("SalasEntrenamiento.json", "w") as file:
        json.dump(salas_entrenamiento, file, indent=4)
    
    print(f"\n¡El entrenador {entrenador_asignado['nombre']} {entrenador_asignado['apellidos']} ha sido asignado a la sala de entrenamiento '{sala_seleccionada['nombre']}' con éxito!")

