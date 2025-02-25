import time
import sys
import random

#Definimos la función slow_print, que imprime un texto con un delay de 0.1 segundos por caracter.
def slow_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

#Definimos las variables diccionario para las dos razas, con sus respectivos valores.

R_benevola={ "Ositos": 1, "Principes": 2, "Enanos": 3, "Caris": 4, "Fulos": 5}
R_malvada={ "Lolos": 2, "Fulanos": 2, "Hoggins": 2, "Lurcos": 3, "Trollis": 5}

#Damos mensaje de bienvenida al juego.
slow_print("Bienvenido al planeta Centauro")
slow_print("El malvado Throm quiere invadir el planeta")

while True:
    #Preguntamos al jugador si quiere ayudar a defender el planeta.
    slow_print("Quieres ayudar a defender este planeta?")

    #definimos la variable ejercitoUsuario como una lista vacia en donde se almacenaran los valores de las razas que el jugador escoja.
    ejercitoUsuario = []
    ejercitoMaquina = []
    resultadoBatalla = 0
    ayuda = input("Si/No: ").upper()

    if( ayuda == "SI" or ayuda == "S"):
        slow_print("Excelente!, ahora haces parte de la resistencia")
        slow_print("escoje tu ejercito para la batalla", 0.05)
        slow_print("Tienes derecho a escoger 5 unidades benevolas para tu ejercito", 0.05)
        
        while len(ejercitoUsuario) < 5:
            print("-------------------------------------------")
            i=1
            for raza in R_benevola:
                print(i, ". ", raza)
                i += 1
            print("Selecciona una unidad benevola para tu ejercito (",len(ejercitoUsuario),"/5):")
            seleccion = int(input())
            if seleccion in range(1, 6):
                ejercitoUsuario.append(list(R_benevola.keys())[seleccion-1])
            else:
                slow_print("Unidad no válida, intenta de nuevo.")
        slow_print("Buena elección", 0.05)
        slow_print("Tu ejercito está listo para la batalla", 0.05)
        ejercitoMaquina = random.sample(list(R_malvada.keys()), 5)
        slow_print("El ejercito de Throm se acerca", 0.05)
        slow_print("Preparate para la batalla", 0.02)
        print("-------------------------------------------")
        print("|Tus Unidades: | VS | Unidades de Throm: |")
        for i in range(5):
            print("-------------------------------------------")
            print("|",ejercitoUsuario[i], "| \t", R_benevola[ejercitoUsuario[i]],  "| VS |", ejercitoMaquina[i], "| \t",R_malvada[ejercitoMaquina[i]],"|")
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
        slow_print("Tienes derecho a escoger 5 unidades malvadas para tu ejercito", 0.05)
        while len(ejercitoUsuario) < 5:
            print("-------------------------------------------")
            i=1
            for raza in R_malvada:
                print(i, ". ", raza)
                i += 1
            print("Selecciona una unidad malvada para tu ejercito (",len(ejercitoUsuario),"/5):")
            seleccion = int(input())
            if seleccion in range(1, 6):
                ejercitoUsuario.append(list(R_malvada.keys())[seleccion-1])
            else:
                slow_print("Unidad no válida, intenta de nuevo.")
        slow_print("Ya has escgido tu ejercito ", 0.05)
        ejercitoMaquina = random.sample(list(R_benevola.keys()), 5)
        slow_print("El ejercito de la resistencia se acerca", 0.05)
        slow_print("Preparate para la batalla", 0.02)
        print("-------------------------------------------")
        print("|Tus Unidades: | VS | Unidades de la resistencia: |")
        for i in range(5):
            print("-------------------------------------------")
            print("|",ejercitoUsuario[i], "| \t", R_malvada[ejercitoUsuario[i]],  "| VS |", ejercitoMaquina[i], "| \t",R_benevola[ejercitoMaquina[i]],"|")
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
        slow_print("Gracias por visitar el planeta Centauro")
        break
    else:
        continue
        
    
