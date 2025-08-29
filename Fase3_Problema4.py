'''
    Nombre: Jhonathan Damian Guerrero Montoya
    Grupo: 374
    Programa: Ingeniería de Sistemas
    Codigo fuente: autoría propia
    Fecha: 09-abr-2025
'''

#Definifimos una funcion para la solucion de cada problema
def intereses():
    
    #Definimos la tasa de interes como una variable fija del 0.7% que equivale al  0.007 en decimal.
    tasa_interes = 0.007
    #Se le pide al usuario que ingrese el capital inicial y el tiempo en meses.
    print("Bienvenido al banco, te ofrecemos un interes del 0.7% mes vencido")
    capital = float(input("Ingrese el capital inicial: \n"))
    tiempo = int(input("Ingrese el tiempo (en meses): \n"))

    #Se calculan los intereses generados mes a mes y se muestra al usuario el resultado.
    print("-"*60)
    for t in range(tiempo + 1):
        #Se muestra el capital al usuario con 2 decimales.
        print(f"|->\t Su capital al mes {t} es de: {capital:.2f}")
        #Se calcula el interes generado en cada mes y se suma al capital los intereses generados.
        interes = capital * tasa_interes
        capital += interes
    print("-"*60)
    print("Gracias por usar nuestro servicio")
    print("*"*60)
    
def matrices():
    
    #Se inicializan una matriz 3x3 con ceros.
    A = [[0 for j in range(3)] for i in range(3)]
    
    #Se le pide al usuario que ingrese los valores de la matriz y se va realizando la suma de las diagonales.
    sumDP = 0
    sumDS = 0
    print("Ingrese valores desde 100 hasta 200 en cada elemento de la matriz:")
    print("-"*60)
    for i in range(3):
        for j in range(3):
            #Verificamos que el valor ingresado por el usuario este dentro del rango de 100 a 200.
            while True:
                valor = int(input(f"A[{i}][{j}]: "))
                if valor in range(100, 201):
                    A[i][j] = valor
                    break
                else:
                    print("El valor ingresado no es válido, por favor ingrese un valor entre 100 y 200.")
                    continue
                
            #por otro lado sumamos los valores de la diagonal principal y secundaria.
            if i == j:
                sumDP += A[i][j]
            if i + j == 2:
                sumDS += A[i][j]
    print("-"*60)
    #Se imprime la matriz en pantalla y las sumas de las diagonales.
    print("La matriz es:")    
    for i in range(3):
        print("\t |", end=" ")
        for j in range(3):
            print(f"{A[i][j]:3}", end=" ")
        print("|")
    
    print("la suma de la diagonal principal es: ")
    print(f"{A[0][0]:3} + {A[1][1]:3} + {A[2][2]:3} = {sumDP:3}")
    print("la suma de la diagonal secundaria es: ")
    print(f"{A[0][2]:3} + {A[1][1]:3} + {A[2][0]:3} = {sumDS:3}")
    print("-"*60)
    print("Por tanto,")
    print(f"el promedio de la diagonal principal es: {sumDP/3:.2f}")
    print(f"el promedio de la diagonal secundaria es: {sumDS/3:.2f}")
    print("-"*60)
    
    if sumDP > sumDS:
        print("La suma de la diagonal principal es mayor que la diagonal secundaria")
        print("en consecuencia el promedio de la diagonal principal es mayor que el de la diagonal secundaria")
    elif sumDP < sumDS:
        print("La suma de la diagonal secundaria es mayor que la diagonal principal")
        print("en consecuencia el promedio de la diagonal secundaria es mayor que el de la diagonal principal")
    else:
        print("La suma de ambas diagonales es igual")
        print("en consecuencia los promedios de ambas diagonales son iguales")    
    print("-"*60)
    print("Gracias por usar nuestro servicio")
    print("*"*60)
    
#Se da la bienvenida al programa y se muestra un menú de inicio para que el usuario pueda elegir el problema que desea resolver.

print("*"*60)
print("Bienvenido al programa")
print("a continuación se mostrara un menú de opciones")

while True:
    print("-"*60)
    print("1. Problema de estructuras repetitivas")
    print("2. Problema de matrices bidimensionales")
    print("3. Salir")
    print("-"*60)
    opcion = int(input("Ingresa el número de la opción a elegir: \n"))
    
    if opcion==1:
        intereses()
    elif opcion==2:
        matrices()
    elif opcion==3:
        print("Gracias por usar el programa")
        print("-"*60)
        break
    else:
        print("Opción no válida, por favor elige una opción del menú")
        continue