import numpy as np

def getMedia(lista):
    lista = np.array(lista)
    #Verificamos que la lista de datos no estes vacia
    if not lista.size:
        return None, None, None
    else:
        #Asignamos los resulados de las operaciones a una variable:
        # rA_A = Resultado del agente A
        # rA_B = Resultado del agente B
        # rA_C = Resultado del agente C
        rA_A = np.mean(lista)
        rA_B = len(lista)/np.sum(1/lista)
        rA_C = 0
        #ordenamiento de menor a mayor de la lista de numeros
        lista = np.sort(lista)
        #Comprovamos si la cantidad de datos en la lista es par
        if len(lista)%2 == 0:
            #Obtenemos los numeros de la mitad de la lista
            indice_1 = (len(lista)//2) - 1
            indice_2 = len(lista)//2
            dato_1 = lista[indice_1]
            dato_2 = lista[indice_2]
            #Calculamos el promedio de estos numeros
            rA_C = (dato_1 + dato_2)/2.0
        else:
            rA_C = lista[len(lista)//2]

        return rA_A, rA_B, rA_C

def getStaircase(number):
    StairAgente_A =""
    StairAgente_B =""
    for i in range(0,number):
        StairAgente_A += ("#"*(i+1)).rjust(number) + "\n"
        StairAgente_B += ("#"*(number-i)).rjust(number) + "\n"
    
    return StairAgente_A, StairAgente_B

numeros = np.array([33,2,3,4,5,6,7,8,9,10])
Agente_A, Agente_B, Agente_C = getMedia(numeros)

SAgente_A, SAgente_B = getStaircase(10)
print("A= ", Agente_A)
print("B= ", Agente_B)
print("C= ", Agente_C)
print(SAgente_A)
print(SAgente_B)

for i in range(1, 5):
    espacios = 4 - i
    escalones = i * "#"
    linea = " " * espacios + escalones
    print(linea)