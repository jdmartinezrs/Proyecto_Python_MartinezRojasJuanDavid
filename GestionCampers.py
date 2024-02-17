import json
def menu_campers(opcion):
    while True : 
        if opcion == 1:
            registrar_nuevo_camper()
            break
        elif opcion == 2:
            modificar_informacion_camper()
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

def registrar_nuevo_camper():
    while True:
        identificacion = int(input("Ingrese el número de identificación del nuevo camper: "))
        nombres = input("Ingrese los nombres del nuevo camper: ")
        apellidos = input("Ingrese los apellidos del nuevo camper: ")
        direccion = input("Ingrese la dirección del nuevo camper: ")
        acudiente = input("Ingrese el nombre del acudiente del nuevo camper: ")
        celular = input("Ingrese el número de celular del nuevo camper: ")
        fijo = input("Ingrese el número fijo del nuevo camper: ")
        estado = "En proceso de ingreso"  
        
        nuevo_camper = {
            "id": identificacion,
            "nombres": nombres,
            "apellidos": apellidos,
            "direccion": direccion,
            "acudiente": acudiente,
            "telefonos": {
                "celular": celular,
                "fijo": fijo
            },
            "estado": estado
        }
        
        with open("Camper.json", "r") as file:
            data = json.load(file)
        
        data['campers'].append(nuevo_camper)
        
        with open("Camper.json", "w") as file:
            json.dump(data, file, indent=4)
        
        print("\n¡Nuevo camper registrado con éxito!")
        
        respuesta = input("\n¿Desea registrar otro camper? (si/no): ")
        if respuesta.lower() != "si":
            break
def modificar_informacion_camper():
    identificacion = int(input("\nIngrese el número de identificación del camper que desea modificar: "))
    with open("Camper.json", "r") as file:
        data = json.load(file)
    camper_encontrado = False
    for camper in data['campers']:
        if camper['id'] == identificacion:
            camper_encontrado = True
            break
    
    if camper_encontrado == False:
        print("\nNo se encontró ningún camper con esa identificación.")
        return
    
    print("\nInformación actual del camper:")
    print("Identificación:", camper['id'])
    print("Nombres:", camper['nombres'])
    print("Apellidos:", camper['apellidos'])
    print("Dirección:", camper['direccion'])
    print("Acudiente:", camper['acudiente'])
    print("Teléfonos:")
    print("  Celular:", camper['telefonos']['celular'])
    print("  Fijo:", camper['telefonos']['fijo'])
    print("Estado:", camper['estado'])
    
    print("\nIngrese los nuevos datos para el camper:")
    camper['nombres'] = input("Nuevos nombres: ")
    camper['apellidos'] = input("Nuevos apellidos: ")
    camper['direccion'] = input("Nueva dirección: ")
    camper['acudiente'] = input("Nuevo nombre del acudiente: ")
    camper['telefonos']['celular'] = input("Nuevo número de celular: ")
    camper['telefonos']['fijo'] = input("Nuevo número fijo: ")
    camper['estado'] = input("Nuevo estado: ")
    
    # Escribir los datos actualizados en el archivo JSON
    with open("Camper.json", "w") as file:
        json.dump(data, file, indent=4)
    
    print("¡Información del camper actualizada con éxito!")
def consultar_estado_camper():
    identificacion = int(input("\nIngrese el número de identificación del camper a consultar: "))
    with open("Camper.json", "r") as file:
        data = json.load(file)
    for camper in data["campers"]:
        if camper["id"] == identificacion:
            print(f"\nEl estado del camper {camper['nombres']} {camper['apellidos']} es: {camper['estado']}")
            return
    print("\nNo se encontró ningún camper con ese número de identificación.")

def asignar_nota_prueba_inicial():
    with open("Camper.json", "r") as file:
        data = json.load(file)
    for camper in data["campers"]:
        if camper["estado"] == "En proceso de ingreso":
            nota = int(input(f"\nIngrese la nota de la prueba inicial para el camper {camper['id']}: "))
            camper["nota_prueba_inicial"] = nota
            if nota >= 60:
                camper["estado"] = "Aprobado"
                print("\nNotas de la prueba inicial asignadas correctamente.")
            elif nota < 60 : 
                camper["estado"] = "Reprobado"
                print("\nNotas de la prueba inicial asignadas correctamente.")
        

            else :
                print("\nNo se encontró ningún camper en el estado de ingreso.") 
                return
        
        with open("Camper.json", "w") as file:
            json.dump(data, file, indent=4)