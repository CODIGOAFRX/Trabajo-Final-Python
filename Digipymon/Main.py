import os
## Hemos importado el random para que nos genere número aleatorios
import random
## Este import se utiliza para que el texto que se muestre tenga una duración
import time
## Hemos importado todas las clases de  nuestro Videojuego
from Jugador import Jugador
from Enemigo import Enemigo
from Inventario import Inventario
from ListaNombres import ListaNombres
from Digipymon import Digipymon 
from os import system

## Esta función principal como es el main abarca todo el proceso del Videojuego
def main():
    print("")
    
    print("Bienvenido a Digipymon!! Podrás hacerte con todos?!")
    time.sleep(0.5)
    print("")
    nombre_jugador = str(input("¿Cúal es tu nombre ser de Luz? "))
    print("")
    print(f"Bienvenido {nombre_jugador}!!") 
    print("")
    jugador1 = Jugador(nombre_jugador)
    inventario1 = Inventario()
    inventario1.añadir_objeto("Digipyball",3)
    bucle = True
    while bucle:
        print("")
        ## Creamos una variable opcion_menu en el cual vamos a igualar o llamar a la función menú que hemos creado. 
        #  Colocamos todas las opcione que vayamos a crear.
        opcion_menu = menu()
        if opcion_menu == "7":
            print("¡Hasta luego!")
            bucle = False
        elif opcion_menu == "1":
            system("cls")
            bucle_bacano = True
            while bucle_bacano:
                ## Creamos una variable opcion_mundos en el cual vamos a igualar o llamar a la función mundos que hemos creado.
                opcion_mundos = mundos()
                if opcion_mundos == "1":
                    system("cls")
                    digipymon1 = buscar_digipymon(jugador1,inventario1)  
                    probabilidad = 100 - (digipymon1.nivel * 10)
                    print("La probabilidad de captura de este" , str(digipymon1.nombre) ,"es :", str(probabilidad),"%")
                    print("")
                    captura = str(input("Quieres intentar capturarlo? (y/n): "))
                    print("")
                    ## Creamos un objeto cuantas_digipyball en el cual vamos a igualarlo para obtener del inventario nuestra lista de objetos en este caso las Digipyballs.
                    cuantas_digipyballs = inventario1.objetos.get("Digipyball")
                    if captura == "y" or captura == "Y":        # Condicional de captura
                        if cuantas_digipyballs > 0 and jugador1.cantidad_digipymon < 6:
                            bucle1 = True
                            while bucle1:
                                inventario1.usar_objeto("Digipyball")
                                cuantas_digipyballs = inventario1.objetos.get("Digipyball")
                                ## 
                                aleatorio = random.randint(1, 100)
                                
                                if aleatorio > 0 and aleatorio <= probabilidad :    # Factor random de captura
                                    jugador1.añadir_digipymon(digipymon1)
                                    print("")
                                    print("Enhorabuena, has capturado este ",str(digipymon1.nombre))  
                                    print("")
                                    bucle1 = False
                                else:
                                    print("")
                                    print("No has podido capturar este digipymon")
                                    print("")
                                    if cuantas_digipyballs > 0:
                                        pregunta1 = str(input("Quieres volver a intentarlo? (y/n): "))
                                        if pregunta1 == "n" or pregunta1 == "N" or cuantas_digipyballs <= 0:
                                            bucle1 = False
                                    else: 
                                        print("¡Ya no tienes digipyballs!")
                                        print("")
                                        bucle1 = False
                        elif cuantas_digipyballs == 0:  # Para realizar la captura hacen falta digipyballs
                            print("!!!No tienes suficientes digipyballs¡¡¡")
                            print("")
                        elif jugador1.cantidad_digipymon == 6:  # Para realizar la captura tienes quev tener menos de 6 digipymons
                            print("No tienes suficiente espacio para guardar otro digipymon")
                    elif captura == "n" or captura == "N":
                        system("cls")
                        print("Has huido con éxito")
                        print("")    
                    else:
                        print("Opción inválida. Intente de nuevo.") # Opción para que no se rompa el juego si no se introduce 
                                                                    # el valor esperado
                        print("")
                elif opcion_mundos=="2":
                    system("cls")
                    print(".")
                    time.sleep(0.3)
                    print(".")
                    time.sleep(0.3)
                    print(".")
                    time.sleep(0.3)
                    print(".")
                    print("Atrancando en Isla Volcán")
                    print("")
                    print("WOOW HA APARECIDO UN DIGIPYMON EVOLUCIONADO DE FUEGO!!")
                    print("")
                ## Aquí estamos calculando la probabilidad de captura del digipymon.
                    digipymon1 = buscar_digipymon_evo_Fuego(jugador1,inventario1)
                    probabilidad = 100 - (digipymon1.nivel * 10)
                    print("La probabilidad de captura de este" , str(digipymon1.nombre) ,"es :", str(probabilidad),"%")
                    print("")
                    captura = str(input("Quieres intentar capturarlo? (y/n): "))
                    print("")
                    cuantas_digipyballs = inventario1.objetos.get("Digipyball")
                    if captura == "y" or captura == "Y":            # Repetición del código de captura anterioir
                        if cuantas_digipyballs > 0 and jugador1.cantidad_digipymon < 6:
                            bucle1 = True
                            while bucle1:
                                cuantas_digipyballs = inventario1.objetos.get("Digipyball")
                                aleatorio = random.randint(1, 100)
                                inventario1.usar_objeto("Digipyball")
                                if aleatorio > 0 and aleatorio <= probabilidad :
                                    jugador1.añadir_digipymon(digipymon1)
                                    print("")
                                    print("Enhorabuena, has capturado este ",str(digipymon1.nombre))  
                                    print("")
                                    bucle1 = False
                                else:
                                    print("")
                                    print("No has podido capturar este digipymon")
                                    print("")
                                    if cuantas_digipyballs > 0:
                                        pregunta1 = str(input("Quieres volver a intentarlo? (y/n) : "))
                                        if pregunta1 == "n" or pregunta1 == "N" or cuantas_digipyballs <= 0:
                                            bucle1 = False
                                    else: 
                                        system("cls")
                                        print("¡Ya no tienes digipyballs!")
                                        print("")
                                        bucle1 = False
                        elif cuantas_digipyballs == 0:
                            print("!!!No tienes suficientes digipyballs¡¡¡")
                            print("")
                        elif jugador1.cantidad_digipymon == 6:
                            print("No tienes suficiente espacio para guardar otro digipymon")
                    elif captura == "n" or captura == "N":
                        system("cls")
                        print("Has huido con éxito")
                        print("")
                    else:
                        print("Opción inválida. Intente de nuevo.")
                        print("")
                elif opcion_mundos=="3":        # Funcionamiento igual que el apartado anterior
                    system("cls")
                    print(".")
                    time.sleep(0.3)
                    print(".")
                    time.sleep(0.3)
                    print(".")
                    time.sleep(0.3)
                    print(".")
                    print("Descendiendo al Submarino Profundo")
                    print("")
                    print("WOOW HA APARECIDO UN DIGIPYMON EVOLUCIONADO DE AGUA!!")
                    print("")
                    digipymon1 = buscar_digipymon_evo_Agua(jugador1,inventario1)
                    probabilidad = 100 - (digipymon1.nivel * 10)
                    print("La probabilidad de captura de este" , str(digipymon1.nombre) ,"es :", str(probabilidad),"%")
                    print("")
                    captura = str(input("Quieres intentar capturarlo? (y/n): "))
                    print("")
                    cuantas_digipyballs = inventario1.objetos.get("Digipyball")
                    if captura == "y" or captura == "Y":
                        if cuantas_digipyballs > 0 and jugador1.cantidad_digipymon < 6:
                            bucle1 = True
                            while bucle1:
                                cuantas_digipyballs = inventario1.objetos.get("Digipyball")
                                aleatorio = random.randint(1, 100)
                                inventario1.usar_objeto("Digipyball")
                                if aleatorio > 0 and aleatorio <= probabilidad :
                                    jugador1.añadir_digipymon(digipymon1)
                                    print("")
                                    print("Enhorabuena, has capturado este ",str(digipymon1.nombre))  
                                    print("")
                                    bucle1 = False
                                else:
                                    print("")
                                    print("No has podido capturar este digipymon")
                                    print("")
                                    if cuantas_digipyballs > 0:
                                        pregunta1 = str(input("Quieres volver a intentarlo? (y/n): "))
                                        if pregunta1 == "n" or pregunta1 == "N" or cuantas_digipyballs <= 0:
                                            bucle1 = False
                                    else: 
                                        print("¡Ya no tienes digipyballs!")
                                        print("")
                                        bucle1 = False
    
                        elif cuantas_digipyballs == 0:
                            system("cls")
                            print("!!!No tienes suficientes digipyballs¡¡¡")
                            print("")
                        elif jugador1.cantidad_digipymon == 6:
                            print("No tienes suficiente espacio para guardar otro digipymon")
                    elif captura == "n" or captura == "N":
                        system("cls")
                        print("Has huido con éxito")
                        print("")
                    else:
                        print("Opción inválida. Intente de nuevo.")
                        print("")
                elif opcion_mundos=="4":                # Funcionamiento igual que el apartado anterior
                    system("cls")
                    print(".")
                    time.sleep(0.3)
                    print(".")
                    time.sleep(0.3)
                    print(".")
                    time.sleep(0.3)
                    print(".")
                    print("Adentrándonos en las Flores Malolientes ")
                    print("")
                    print("WOOW HA APARECIDO UN DIGIPYMON EVOLUCIONADO DE PLANTA!!")
                    print("")
                    digipymon1 = buscar_digipymon_evo_Planta(jugador1, inventario1)
                    probabilidad = 100 - (digipymon1.nivel * 10)
                    print("La probabilidad de captura de este" , str(digipymon1.nombre) ,"es :", str(probabilidad),"%")
                    print("")
                    captura = str(input("Quieres intentar capturarlo? (y/n): "))
                    print("")
                    cuantas_digipyballs = inventario1.objetos.get("Digipyball")
                    if captura == "y" or captura == "Y":
                        if cuantas_digipyballs > 0 and jugador1.cantidad_digipymon < 6:
                            bucle1 = True
                            while bucle1:
                                cuantas_digipyballs = inventario1.objetos.get("Digipyball")
                                aleatorio = random.randint(1, 100)
                                inventario1.usar_objeto("Digipyball")
                                if aleatorio > 0 and aleatorio <= probabilidad :
                                    jugador1.añadir_digipymon(digipymon1)
                                    print("")
                                    print("Enhorabuena, has capturado este ",str(digipymon1.nombre))  
                                    print("")
                                    bucle1 = False
                                else:
                                    print("")
                                    print("No has podido capturar este digipymon")
                                    print("")
                                    if cuantas_digipyballs > 0:
                                        pregunta1 = str(input("Quieres volver a intentarlo? (y/n) : "))
                                        if pregunta1 == "n" or pregunta1 == "N" or cuantas_digipyballs <= 0:
                                            bucle1 = False
                                    else: 
                                        system("cls")

                                        print("¡Ya no tienes digipyballs!")
                                        print("")
                                        bucle1 = False
                        elif cuantas_digipyballs == 0:
                            system("cls")
                            print("!!!No tienes suficientes digipyballs¡¡¡")
                            print("")
                        elif jugador1.cantidad_digipymon == 6:
                            print("No tienes suficiente espacio para guardar otro digipymon")
                    elif captura == "n" or captura == "N":
                        system("cls")
                        print("Has huido con éxito")
                        print("")
                    else:
                        print("Opción inválida. Intente de nuevo.")
                        print("")
                elif opcion_mundos=="5":
                    system("cls")
                    print("Saliendo")
                    print(".")
                    time.sleep(0.3)
                    print(".")
                    time.sleep(0.3)
                    print(".")
                    time.sleep(0.3)
                    bucle_bacano = False
                elif opcion_mundos!="1" or opcion_mundos!="2" or opcion_mundos!="3" or opcion_mundos!="4" or opcion_mundos!="5": 
                    print("El valor que has introducido es incorrecto!!!!")
                    print("")     
        elif opcion_menu == "2":        
            system("cls")
            combate(jugador1)           # Llama a lla función combate
        elif opcion_menu == "6":
            system("cls")
            consultar_digipymons(jugador1)          # Imprime lista de digipymons que tienes
            opcion2 = str(input("¿Quieres acceder al evolucionador? (Y|N) : "))
            if opcion2 == "Y" or opcion2 == "y":
                nombre_digipymon1 = str(input("Introduce el nombre del digipymon : "))  
                evolucionar_bicho(jugador1,nombre_digipymon1)       # Llama a la función evolucionar_bicho
            elif opcion2 == "N" or opcion2 == "n":
                system("cls")
                print("Saliendo")
                print(".")
                time.sleep(0.3)
            else:
                print("")
                print("Opción Incorrecta!! Vuelva a intentarlo")
        elif opcion_menu == "3":
            system("cls")
            digishop_completo(jugador1,inventario1)     # Llama a la función digishop
        elif opcion_menu == "5":
            system("cls")
            inventario1.mostrar_objetos()               # Muestra el inventario
        elif opcion_menu == "4":
            system("cls")
            inventario1.mostrar_objetos()               # Muestra el inventario y te pregunta cuál de los objetos quieres usar
            bucle7 = True                               # si anabolizantes o pociones  
            while bucle7: 
                if jugador1.cantidad_digipymon != 0:    
                    opcion_usar = str(input("¿Qué objeto del inventario deseas usar? Anabolizante (A|P) Pociones (S para salir): "))
                    print("")
                    if opcion_usar == "A" and inventario1.objetos["Anabolizantes"] != 0  or opcion_usar == "a" and inventario1.objetos["Anabolizantes"] != 0 :
                        consultar_digipymons(jugador1)
                        cualquiere = int(input("¿A qué número de digipymon quieres chetar? : "))    # Selección de digipymon
                        if cualquiere <= len(jugador1.lista_digipymon):
                            digipymon_elegido = jugador1.lista_digipymon[cualquiere-1]
                            print("")
                            print("Inyectando esteroides a "+ str(digipymon_elegido.nombre))
                            time.sleep(2)
                            print("")
                            print("WUAOOU ESO HA SENTADO GENIAL!!")
                            time.sleep(1)
                            print("")
                            inventario1.usar_objeto("Anabolizantes")        # Usa el objeto
                            digipymon_elegido.ataque += 5
                            print("Sus nuevas estadísticas son: ")
                            print("")
                            print(digipymon_elegido)
                        elif cualquiere > len(jugador1.lista_digipymon):
                            print("No tienes ningún digipymon con ese número")
                            print("")
                        else:
                            print("Opción inválida")
                            print("")
                    elif opcion_usar == "P" and inventario1.objetos["Poción Curativa"] != 0 or opcion_usar == "p" and inventario1.objetos["Poción Curativa"] != 0:
                        consultar_digipymons(jugador1)
                        cualquiere2 = int(input("¿A qué número de digipymon quieres curar? : "))    # Selección de digipymon
                        if cualquiere2 <= len(jugador1.lista_digipymon):
                            print("")
                            digipymon_elegido = jugador1.lista_digipymon[cualquiere2-1]
                            print("Bebiendo poción repugnante")
                            time.sleep(2)
                            print("")
                            print("SIENTE EL PODER DE LA CURACIÓN! ¡TU VITALIDAD HA SIDO RESTAURADA. ¡ADELANTE, HÉROE, TU CAMINO SIGUE BRILLANDO!")
                            time.sleep(1)
                            print("")
                            inventario1.usar_objeto("Poción Curativa")       # Usa el objeto
                            print("")
                            digipymon_elegido.vida += 10
                            print("Sus nuevas estadísticas son: ")
                            print("")
                            print(digipymon_elegido)
                        elif cualquiere2 > len(jugador1.lista_digipymon):
                            print("No tienes ningún digipymon con ese número")
                            print("")
                        else:
                            print("Opción inválida")
                            print("")
                    elif opcion_usar =="s" or opcion_usar == "S":
                        print("Saliendo del inventario")
                        time.sleep(0.3)
                        print(".")
                        time.sleep(0.3)
                        print(".")
                        time.sleep(0.5)
                        print(".")
                        bucle7 = False      # Cierra el bucle y sale
                    elif opcion_usar == "A" and inventario1.objetos["Anabolizantes"] == 0  or opcion_usar == "a" and inventario1.objetos["Anabolizantes"] == 0 : 
                        print("No te quedan anabolizantes, pasa por la tienda") # Comprueba que te quedan anabolizantes
                        print("")
                        time.sleep(0.3)
                        print(".")
                        time.sleep(0.3)
                        print(".")
                        time.sleep(0.3)
                        print(".")
                        bucle7 = False
                    elif opcion_usar == "P" and inventario1.objetos["Poción Curativa"] == 0 or opcion_usar == "p" and inventario1.objetos["Poción Curativa"] == 0: 
                        print("No te quedan pociones, pasa por la tienda")  # Comprueba que te quedan pociones
                        print("")
                        time.sleep(0.3)
                        print(".")
                        time.sleep(0.3)
                        print(".")
                        time.sleep(0.3)
                        print(".")
                        bucle7 = False
                    else: 
                        print("Opción inválida. Intente de nuevo.") 
                        print("")
                else: 
                    print("No tienes ningún digipymon") # No tienes digipymons por lo que muestra este mensaje
                    time.sleep(0.3)
                    print(".")
                    time.sleep(0.3)
                    print(".")
                    time.sleep(0.3)
                    print(".")
                    bucle7 = False
        else: 
            print("Opción inválida. Intente de nuevo.")
            print("")
## Se crea la función mundos donde vamos a tener un menú para capturar digipymons según zonas donde habitan.
def mundos():
    print("1.  Buscar digipymon aleatorio    (  Principiante  )     ****")
    print("2.  Visitar Isla Volcán           (  Experto       )     ****")
    print("3.  Visitar Submarino Profundo    (  Experto       )     ****")
    print("4.  Visitar Flores Malolientes    (  Experto       )     ****")
    print("                                     5. Salir            ****")
    opcion = str(input("Ingrese una opcion: "))
    print("")
    return opcion
## Función que genera un digipymon estandar con un nombre aleatorio de nuestra lista y resto de atributos aleatorios
def generar_digipymon_aleatorio():
    vida = random.randint(10, 20)
    ataque = random.randint(1,10)
    nivel = random.randint(1,3)
    tipos = ["Fuego", "Agua", "Planta"]
    tipo = random.choice(tipos)
    lista = ListaNombres()
    nombre = lista.obtener_nombres_digipymon()
    digipymon = Digipymon(nombre, vida, ataque,tipo, nivel)
    return digipymon
## Función que genera un digipymon evolcionado con un nombre aleatorio de su lista de nombres, tipo fuego y resto de atributos aleatorios
def generar_digipymon_Evo_Fuego():
    vida = random.randint(30, 80)
    ataque = random.randint(20,100)
    nivel = random.randint(8,9)
    tipos = ["Fuego"]
    tipo = random.choice(tipos)
    lista = ListaNombres()
    numero_aletorio= random.randint(0,19)
    nombre = lista.obtener_nombre_digipymon_evolucionado(numero_aletorio)
    digipymon_evo_Fuego = Digipymon(nombre, vida, ataque,tipo, nivel)
    return digipymon_evo_Fuego
## Función que genera un digipymon evolcionado con un nombre aleatorio de su lista de nombres, tipo agua y resto de atributos aleatorios
def generar_digipymon_Evo_Agua():
    vida = random.randint(30, 80)
    ataque = random.randint(20,100)
    nivel = random.randint(8,9)
    tipos = ["Agua"]
    tipo = random.choice(tipos)
    lista = ListaNombres()
    numero_aletorio= random.randint(0,19)
    nombre = lista.obtener_nombre_digipymon_evolucionado(numero_aletorio)
    digipymon_evo_Agua = Digipymon(nombre, vida, ataque,tipo, nivel)
    return digipymon_evo_Agua
## Función que genera un digipymon evolcionado con un nombre aleatorio de su lista de nombres, tipo planta y resto de atributos aleatorios
def generar_digipymon_Evo_Planta():
    vida = random.randint(30, 80)
    ataque = random.randint(20,100)
    nivel = random.randint(8,9)
    tipos = ["Planta"]
    tipo = random.choice(tipos)
    lista = ListaNombres()
    numero_aletorio= random.randint(0,19)
    nombre = lista.obtener_nombre_digipymon_evolucionado(numero_aletorio)
    digipymon_evo_Planta = Digipymon(nombre, vida, ataque,tipo, nivel)
    return digipymon_evo_Planta
## Se define un función de menú principal del videojuego.
def menu():
    print("** Digipymon:                  ****")
    time.sleep(0.15)                            # El menú se vaya mostrando linea por linea para que tenga mejor aspecto visual
    print("1. Buscar digipymon            ****")
    time.sleep(0.15)
    print("2. Luchar contra un entrenador ****")
    time.sleep(0.15)
    print("3. Ir a la tienda              ****")
    time.sleep(0.15)
    print("4. Usar objetos                ****")
    time.sleep(0.15)
    print("5. Consultar inventario        ****")
    time.sleep(0.15)
    print("6. Consultar digipymons        ****")
    time.sleep(0.15)
    print("7. Salir")
    time.sleep(0.15)
    print("")
    opcion = str(input("Ingrese una opcion: "))
    print("")
    return opcion
## Esta función se encarga de crear el digipymon e imprimirlo por pantalla. Por ultimo lo devuelve.
def buscar_digipymon(Jugador,Inventario):
    digipymon1 = generar_digipymon_aleatorio()
    print(digipymon1)
   
    return digipymon1
## Esta función se encarga de crear el digipymon de fuego e imprimirlo por pantalla. Por ultimo lo devuelve.
def buscar_digipymon_evo_Fuego(Jugador,Inventario):
    digipymon1 = generar_digipymon_Evo_Fuego()
    print(digipymon1)
   
    return digipymon1
## Esta función se encarga de crear el digipymon de agua e imprimirlo por pantalla. Por ultimo lo devuelve.
def buscar_digipymon_evo_Agua(Jugador,Inventario):
    digipymon1 = generar_digipymon_Evo_Agua()
    print(digipymon1)
   
    return digipymon1
## Esta función se encarga de crear el digipymon de planta e imprimirlo por pantalla. Por ultimo lo devuelve.
def buscar_digipymon_evo_Planta(Jugador,Inventario):
    digipymon1 = generar_digipymon_Evo_Planta()
    print(digipymon1)
   
    return digipymon1
## Esta función realiza un combate entre jugador y un enemigo aleatorio. El combate se realiza por turnos, y en cada turnos luchan
#  un digipymon del jugador y un digipymon del enemigo. El resultado del combate afecta a la cantidad de digicoins del jugador.
#  Lo más importante de esta función es la capacida de generar al enemigo tantos digipymons como tengamos nosotros
def combate(jugador1,):
    lista1 = ListaNombres()
    nombre = lista1.obtener_nombre_entrenadores()
    enemigo1 = Enemigo(nombre)
    for i in range(jugador1.cantidad_digipymon):
        digipymon_enemigo = generar_digipymon_aleatorio()
        enemigo1.añadir_digipymon(digipymon_enemigo)
    bucle2 = True
    while bucle2:
        opcion_combate = str(input(f"¿ Quieres enfrentarte a {nombre}? (y/n): ")) 
        if opcion_combate == "y" or opcion_combate == "Y":
            if jugador1.cantidad_digipymon != 0:
                print("¡Comienza el combate!")
                time.sleep(2)
                print("")
                contador_win = 0
                contador_lose = 0
                for i in range(min(len(jugador1.lista_digipymon), len(enemigo1.lista_digipymon))):
                    print(f"Turno {i+1}:")
                    mi_digipymon = jugador1.lista_digipymon[i]
                    enemigo_digipymon = enemigo1.lista_digipymon[i]
                    enemigo_digipymon.ataque = enemigo_digipymon.ataque + jugador1.contador_victorias_totales * 2  #aqui redondea para arriba
                    print(f"Tu {mi_digipymon.nombre} se enfrenta al {enemigo_digipymon.nombre} del enemigo.")
                    print(f"Tu {mi_digipymon.nombre} tiene {mi_digipymon.ataque} de ataque.")
                    print(f"El {enemigo_digipymon.nombre} del enemigo tiene {enemigo_digipymon.ataque} de ataque.")
                    print(f"El tipo de {mi_digipymon.nombre} es {mi_digipymon.tipo} ")
                    print(f"El tipo de {enemigo_digipymon.nombre} es {enemigo_digipymon.tipo} ")
                    ## Aquí se encuentra la mejora que hace que el fuego le gane a la planta, la planta al gua y el agua al fuego
                    #  como podemos ver afecta directamentesobre el ataque del digipymon enemigo
                    if (mi_digipymon.tipo == "Fuego"and enemigo_digipymon.tipo == "Planta") or (mi_digipymon.tipo == "Planta"and enemigo_digipymon.tipo == "Agua") or (mi_digipymon.tipo == "Agua"and enemigo_digipymon.tipo == "Fuego"):
                        enemigo_digipymon.ataque == enemigo_digipymon.ataque * 0.8
                    elif (mi_digipymon.tipo == "Fuego"and enemigo_digipymon.tipo == "Fuego") or (mi_digipymon.tipo == "Planta"and enemigo_digipymon.tipo == "Planta") or (mi_digipymon.tipo == "Agua"and enemigo_digipymon.tipo == "Agua"):
                        enemigo_digipymon.ataque == enemigo_digipymon.ataque * 1
                    else:
                        enemigo_digipymon.ataque = enemigo_digipymon.ataque * 1.2
                    ## Aquí se comprueba quien gana los combates y cuanta vida pierde cada digipyon
                    if mi_digipymon.ataque > enemigo_digipymon.ataque and mi_digipymon.vida != 0 :
                        print("¡Ganas el combate!")
                        print("")
                        mi_digipymon.vida -= round(enemigo_digipymon.ataque, 0)
                        if mi_digipymon.vida < 0 :  
                            mi_digipymon.vida = 0
                        contador_win += 1
                        print(f"Tu {mi_digipymon.nombre} ha ganado, pero pierde {round(enemigo_digipymon.ataque, 0)} de vida.")
                        print("")
                    elif mi_digipymon.ataque < enemigo_digipymon.ataque or mi_digipymon.vida <= 0:
                        if mi_digipymon.vida <= 0:
                            print("¡Pierdes el combate! Tu digipymon está reventao pare")
                            contador_lose += 1
                        else:
                            print("¡Pierdes el combate!")
                            print("")
                            
                            mi_digipymon.vida -= round(enemigo_digipymon.ataque, 0)
                            if mi_digipymon.vida < 0 :  
                                mi_digipymon.vida = 0
                            contador_lose += 1
                        
                        print(f"Tu {mi_digipymon.nombre} ha perdido, y pierde {round(enemigo_digipymon.ataque, 0)} de vida.")                       
                    elif mi_digipymon.ataque == enemigo_digipymon.ataque:
                        print(f"¡Es un empate! Tu {mi_digipymon.nombre} no pierde vida")                   
                    print("------")
                    print("Fin del combate.")
                    time.sleep(2)
                    print("")
                ## Aquí se determina quien ha ganado el enfrentamiento final haciendo un recuento de victorias de coombates.
                #  Por último se hace un reparto de oro o se resta al jugador dependiendo de lo bien o mal que le fue en la batalla.
                if contador_win > contador_lose :
                    print("Tu recuento de victorias es favorable!! Enhorabuena ganaste el primer puesto hoy.")
                    print("")
                    jugador1.contador_victorias_totales += 1
                    jugador1.digicoins += contador_win * 5
                    print(f"Tu oro ha aumentado a : {jugador1.digicoins} oros")
                    bucle2 = False                    
                elif contador_win < contador_lose :
                    print("Hoy ha sido un mal día, vuelve a intentarlo pronto!")
                    print("")
                    jugador1.digicoins -= contador_lose                   
                    if jugador1.digicoins < 0:
                        jugador1.digicoins = 0
                    print(f"Tu oro ha descendido a : {jugador1.digicoins} oros")
                    bucle2 = False
                else:
                    print("¡Es un empate!")
                    bucle2 = False
                    jugador1.digicoins += contador_win 
                    print(f"Tu oro ha aumentado a: {jugador1.digicoins} oros")
            else: 
                print("")
                print("No tienes digipymons")
                bucle2 = False
        elif opcion_combate == "n"  or opcion_combate == "N":
            print("")
            print("Nos quedamos con uno de oro por tu cobardía")
            jugador1.digicoins -= 1
            bucle2 = False
        else:
            print("")
            print("Ingrese una opcion valida")
            print("")            
 ## Esta función muestra menú de opciones de la tienda al usuario, solicita al usuario qu ingrese una opción y devuelve
 #  la opción ingresada.
def digishop(jugador1):
    print("MOSTRANDO DIGISHOP...")
    time.sleep(0.3)
    print(f"                                                               ****  ORO: {jugador1.digicoins}")
    print("     TIENDA DIGISHOP:                                          ****")
    time.sleep(0.1)
    print("  1. Digipyball: 5 digicoins                                   ****")
    time.sleep(0.1)
    print("  2. Poción: 3 digicoins (restaura 10p de vida)                ****")
    time.sleep(0.1)
    print("  3. Anabolizantes: 4 digicoins (aumenta 5p de ataque)         ****")
    time.sleep(0.1)
    print("  4. Salir")
    time.sleep(0.1)
    print("")
    opcion_tienda = str(input("Ingrese una opcion: "))
    print("")
    return opcion_tienda
## Muestra todos los digipymons que tiene el jugador.    
def consultar_digipymons(jugador1):
    for i in range(len(jugador1.lista_digipymon)):
        print(f"Digipymon numero {i+1}:")
        print("")
        mi_digipymon = jugador1.lista_digipymon[i]
        print(str(mi_digipymon))
        print("")       
## Muestra un menú de la tienda al usuario, permite al usuario comprar objetos si tiene suficientes digicoins,
#  y añade los objetos comprados al inventario1.
def digishop_completo(jugador1,inventario1):
    bucle3 = True
    while bucle3:
        system("cls")
        opcion_tienda = digishop(jugador1)
        if opcion_tienda == "1":
            if jugador1.digicoins >= 5:
                print("Has comprado una Digipyball")
                print("")
                jugador1.digicoins -= 5
                inventario1.añadir_objeto("Digipyball",1)
            else:
                print("No tienes suficientes digicoins")
                bucle3 = False
        elif opcion_tienda == "2":
            if jugador1.digicoins >= 3:
                print("Has comprado una poción Curativa (+10p de vida)")
                print("")
                jugador1.digicoins -= 3
                inventario1.añadir_objeto("Poción Curativa",1) 
            else:
                print("No tienes suficientes digicoins")
                bucle3 = False
        elif opcion_tienda == "3":
            if jugador1.digicoins >= 4:
                print("Has comprado anabolizantes (+5p de ataque)")
                print("")
                jugador1.digicoins -= 4
                inventario1.añadir_objeto("Anabolizantes",1)
            else:
                print("No tienes suficientes digicoins")
                print("")
                bucle3 = False
        elif opcion_tienda == "4":
            bucle3 = False
            time.sleep(0.3)           
            print("Saliendo de tienda")
            time.sleep(1)
            system("cls")
        else:
            print("Opción inválida.")
            print("")
            continuar = str(input("Pulse intro para volver a intentar. "))
def evolucionar_bicho(jugador1,nombre_digipymon):       # Primero consulta si se puede evolucionar. 
                                                        # Luego llama a la función generar digipymon.
                                                        # Añade dicho digipymon a la lista de digipymon del jugador 1. 
                                                        # Asocia el nombre del digipymon a su evolucion respectiva y crea una nueva lista. 
            evolucion = jugador1.consultar_evolucion(nombre_digipymon)
            if evolucion : 
                evolucionado = generar_digipymon_evo(nombre_digipymon)
                jugador1.lista_digipymon.append(evolucionado)
                
            nueva_lista_digipymon = [digipymon for digipymon in jugador1.lista_digipymon if digipymon.nombre != nombre_digipymon]
            jugador1.lista_digipymon = nueva_lista_digipymon
            
            print(f"{evolucionado.nombre} se ha añadido correctamente a tu lista de digipymons")                                           
## Genera un digipymon evolucionado aleatorio con atributos y un nombre basado en el nombre_digipymon proporcionado,
#  devuelve el digipymon generado.              
def generar_digipymon_evo(nombre_digipymon): #Genera un digipymon evolucionado
    vida = random.randint(30, 80)
    ataque = random.randint(20,100)
    nivel = random.randint(8,9)
    tipos = ["Fuego"]
    tipo = random.choice(tipos)
    lista = ListaNombres()
    nombre = lista.obtener_nombre_digipymon_evolucionado(lista.lista_nombres_digipymons.index(nombre_digipymon))
    digipymon_evo = Digipymon(nombre, vida, ataque,tipo, nivel)
    return digipymon_evo  

## Se llama a la función main para ejecutar el codigo.
main()