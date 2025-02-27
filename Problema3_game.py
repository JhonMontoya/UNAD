# Nombre: Jhonathan Damian Guerrero Montoya
# Grupo: 374
# Programa: Ingeniería de Sistemas
# Codigo fuente: autoría propia

import time
import sys
import random

#Definimos la función slow_print, que permite dar efectos de escritura lenta en pantalla.
def slow_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

#Damos mensaje de bienvenida al juego.
slow_print("Bienvenido al planeta Centauro")
slow_print("El malvado Throm quiere invadir el planeta")

#Definimos las variables diccionario para las dos razas, con sus respectivos valores.
R_benevola={ "Ositos": 1, "Principes": 2, "Enanos": 3, "Caris": 4, "Fulos": 5}
R_malvada={ "Lolos": 2, "Fulanos": 2, "Hoggins": 2, "Lurcos": 3, "Trollis": 5}

while True:
    #Preguntamos al jugador si quiere ayudar a defender el planeta.
    slow_print("Quieres ayudar a defender este planeta?")

    #definimos la variable ejercitoUsuario como una lista vacia en donde se almacenaran los valores de las razas que el jugador escoja.
    ejercitoUsuario = []
    ejercitoMaquina = []
    
    ayuda = input("Si/No: ").upper()
    cantidadEjercito = random.randint(1, 7)
    cantidadEjercitoMaquina = random.randint(1, 7)
    if( ayuda == "SI" or ayuda == "S"):
        slow_print("Excelente!, ahora haces parte de la resistencia")
        slow_print("escoje tu ejercito para la batalla", 0.05)
        slow_print(f"Tienes derecho a escoger {cantidadEjercito} unidades benevolas para tu ejercito", 0.05)
        
        while len(ejercitoUsuario) < cantidadEjercito:
            print("-------------------------------------------")
            i=1
            for raza in R_benevola:
                print(i, ". ", raza)
                i += 1
            print("Selecciona una unidad benevola para tu ejercito (",len(ejercitoUsuario),"/",cantidadEjercito,"):")
            seleccion = int(input())
            if seleccion in range(1, 6):
                ejercitoUsuario.append(list(R_benevola.keys())[seleccion-1])
            else:
                slow_print("Unidad no válida, intenta de nuevo.",0.02)
        slow_print("Buena elección", 0.05)
        slow_print("Tu ejercito está listo para la batalla", 0.05)
        ejercitoMaquina = random.sample(list(R_malvada.keys()), cantidadEjercitoMaquina)
        slow_print("El ejercito de Throm se acerca", 0.05)
        slow_print("Preparate para la batalla", 0.02)
        print("-------------------------------------------")
        print(f"|{'Tu ejer.:':10} |{'Poder:':3}| VS | {'Ejer. Throm:':10}|{'Poder:':3} |")
        for i in range(max(cantidadEjercito, cantidadEjercitoMaquina)):
            print("-------------------------------------------")
            if i<len(ejercitoUsuario):
                user_unit = ejercitoUsuario[i]
                user_power = R_benevola[user_unit]
            else:
                user_unit = ""
                user_power = ""

            if i<len(ejercitoMaquina):
                machine_unit = ejercitoMaquina[i]
                machine_power = R_malvada[machine_unit]
            else:
                machine_unit = ""
                machine_power = ""
            print(f"| {user_unit:10} | {user_power:3} | VS | {machine_unit:10} | {machine_power:3} |")
        print("-------------------------------------------")
        totalUsuario = sum([R_benevola[unidad] for unidad in ejercitoUsuario])
        totalMaquina = sum([R_malvada[unidad] for unidad in ejercitoMaquina])
        print("Tu poder de ataque es: ", totalUsuario)
        print("El poder de ataque de Throm es: ", totalMaquina)
        if totalUsuario > totalMaquina:
            slow_print("Felicidades, has ganado la batalla",0.02)
            slow_print("Throm ha sido derrotado",0.02)
            slow_print("Gracias por salvar al planeta Centauro",0.02)
        elif totalUsuario < totalMaquina:
            slow_print("Lo siento, has perdido la batalla",0.02)
            slow_print("Oh... Throm ha conquistado el planeta",0.02)
            slow_print("Gracias por intentar salvar al planeta Centauro",0.02)
        else:
            slow_print("La batalla ha terminado, has empatado",0.02)
            slow_print("Gracias por intentar salvar al planeta Centauro",0.02)
    else:
        slow_print("Has decidido aliarte con Throm")
        slow_print("Escoje tu ejercito para la batalla", 0.05)
        slow_print(f"Tienes derecho a escoger {cantidadEjercito} unidades malvadas para tu ejercito", 0.05)
    
        while len(ejercitoUsuario) < cantidadEjercito:
            print("-------------------------------------------")
            i=1
            for raza in R_malvada:
                print(i, ". ", raza)
                i += 1
            print("Selecciona una unidad malvada para tu ejercito (",len(ejercitoUsuario),"/",cantidadEjercito,"):")
            seleccion = int(input())
            if seleccion in range(1, 6):
                ejercitoUsuario.append(list(R_malvada.keys())[seleccion-1])
            else:
                slow_print("Unidad no válida, intenta de nuevo.",0.02)
        slow_print("Ya has escgido tu ejercito ", 0.05)
        ejercitoMaquina = random.sample(list(R_benevola.keys()), cantidadEjercitoMaquina)
        slow_print("El ejercito de la resistencia se acerca", 0.05)
        slow_print("Preparate para la batalla", 0.02)
        print("-------------------------------------------")
        print(f"|{'Tu ejer.:':10} |{'Poder:':3}| VS | {'Ejer. Throm:':10}|{'Poder:':3} |")
        for i in range(max(cantidadEjercito, cantidadEjercitoMaquina)):
            print("-------------------------------------------")
            if i<len(ejercitoUsuario):
                user_unit = ejercitoUsuario[i]
                user_power = R_malvada[user_unit]
            else:
                user_unit = ""
                user_power = ""

            if i<len(ejercitoMaquina):
                machine_unit = ejercitoMaquina[i]
                machine_power = R_benevola[machine_unit]
            else:
                machine_unit = ""
                machine_power = ""
            print(f"| {user_unit:10} | {user_power:3} | VS | {machine_unit:10} | {machine_power:3} |")
        print("-------------------------------------------")
        totalUsuario = sum([R_malvada[unidad] for unidad in ejercitoUsuario])
        totalMaquina = sum([R_benevola[unidad] for unidad in ejercitoMaquina])
        print("Tu poder de ataque es: ", totalUsuario)
        print("El poder de ataque de la resistencia es: ", totalMaquina)
        if totalUsuario > totalMaquina:
            slow_print("Felicidades, has ganado la batalla",0.02)
            slow_print("La resistencia ha sido derrotada",0.02)
            slow_print("Throm a conquistado el planeta Centauro",0.02)
        elif totalUsuario < totalMaquina:
            slow_print("Lo siento, has perdido la batalla",0.02)
            slow_print("La resistencia ha derrotado a Throm",0.02)
        else:
            slow_print("La batalla ha terminado, has empatado",0.02)
        
    print("¿Deseas jugar de nuevo?")
    continuar = input("Si/No: ").upper()
    if(continuar == "NO" or continuar == "N"):
        slow_print("Gracias por visitar el planeta Centauro",0.02)
        break
    else:
        continue