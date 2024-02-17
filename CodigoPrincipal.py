import GestionesMenus 
import GestionCampers
import GestionRutas

while True : 
    opc = GestionesMenus.mostrar_menu_principal()
    if opc == 1: 
        opc_GestionCampers = GestionesMenus.mostrar_menu_gestion_campers()
        GestionCampers.menu_campers(opc_GestionCampers)
    elif opc == 2: 
        opc_GestionRutas = GestionesMenus.mostrar_menu_gestion_rutas()
        GestionRutas.menu_ruta(opc_GestionRutas)
    elif opc == 3: 
        opc_GestionEntrenadores = GestionesMenus.mostrar_menu_gestion_entrenadores
        GestionesMenus.mostrar_menu_gestion_entrenadores(opc_GestionEntrenadores)
    elif opc == 4: 
        opc_GenerarReportes = GestionesMenus.mostrar_menu_generar_reportes
        GestionesMenus.mostrar_menu_generar_reportes(opc_GenerarReportes)
    elif opc == 5: 
        opc_GestionRutas = GestionesMenus.mostrar_menu_gestion_rutas
        GestionesMenus.mostrar_menu_gestion_rutas(opc_GestionRutas)
    elif opc == 6: 
        confirmacion = input ( "\n ¿Desea salir del sistema? ")
        if confirmacion == "si" : 
            print ("\n ¡ Hasta Pronto ! ")
        else : 
            print (" Hola de nuevo ")