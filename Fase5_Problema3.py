'''
    PROBLEMA 3:
    Este programa se desarrolla con el objetivo de ayudar a una empresa con el sistema de gestion de la informacion de sus empleados.

    Elaborado por: Jhonathan Damian Guerrero Montoya
    Grupo: 374
    Programa: Ingeniería de Sistemas
    Curso: Fundamentos de programación
    Codigo fuente: autoría propia
    Fecha: 18-may-2025

'''

#Impotamos librerias necesarias para que los mensajes que salen en pantalla tengan en slow motion solo para hacer el programa mas atractivo.

import time
import sys

#Definimos la funcion slow_print que imprime el mensaje en pantalla letra por letra con un tiempo de espera entre cada letra.
def slow_print(message, delay=0.12):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

#Definimos la clase empleado
class Empleado:
    def __init__(self, nombre, departamento, salario, desempenio):
        self.nombre = nombre
        self.departamento = departamento
        self.salario = salario
        self.desempenio = desempenio

    #Definimos el metodo getInformation para obtener la informacion del empleado
    def getInformation(self):
        return {
            "Nombre": self.nombre,
            "Departamento": self.departamento,
            "Salario": self.salario,
            "Desempenio": self.desempenio
        }

#Damos la bienvenida al usuario
slow_print("Bienvenido a la empresa S.A.")
print(50*"=")
time.sleep(0.5)
#Solicitamos al usuario que ingrese la cantidad de empleados
print("Por favor ingrese la cantidad de empleados que desea registrar: ")
cantidadEmpleados = input()
print(50*"=")
#Validamos que la cantidad de empleados sea un numero entero mayos o igual a 0
try:
    if not cantidadEmpleados.isdigit():
        raise ValueError("La cantidad de empleados debe ser un número entero.")
    elif int(cantidadEmpleados) < 0:
        raise ValueError("La cantidad de empleados no puede ser negativa.")
    
    #Solicitamos al usuario que ingrese la informacion de los empleados
    empleados = []
    for i in range(int(cantidadEmpleados)):
        print(f"Ingrese la información del empleado {i+1}:")
        nombre = input("Nombre: ")
        departamento = input("Departamento: ")
        #Validamos que el salario ingresado sea un numero mayor a 0
        while True:
            salario = input("Salario: ")
            if salario.isdigit() and float(salario) > 0:
                salario = float(salario)
                break
            else:
                print("El salario debe ser un número mayor a 0.")
                continue
        #Validamos que el desempenio ingresado sea un numero entre 1 y 5
        while True:
            desempenio = input("Nivel de desempeño del 1 al 5: ")
            if desempenio.isdigit() and int(desempenio) in range(1,6):
                desempenio = int(desempenio)
                break
            else:
                print("El nivel de desempeño debe ser un número entero entre 1 y 5.")
                continue
        #Agregamos el empleado a la lista de empleados
        empleados.append(Empleado(nombre, departamento, salario, desempenio))
        slow_print("Empleado registrado con éxito.", 0.02)
        print(50*"=")

    #Mostramos la informacion de los empleados
    slow_print("Información de los empleados registrados:")
    print(50*"=")
    print("| {:<15} | {:^15} | {:^15} | {:^20} | {:^15} |".format("Nombre", "Depto", "Salario", "Desempeño", "Salario Anual"))
    
    print(90*"-")
    totalSalarios = 0
    maximoSalario = 0
    empleadoMaximoSalario = ""
    for empleado in empleados:
        info = empleado.getInformation()
        #Calculamos el salario anual teniendo en cuenta el desempeño
        if info["Desempenio"] == 1:
            salarioAnual = info['Salario'] * 12
            bono = "1 -> 0% de bono"
        elif info["Desempenio"] == 2:
            salarioAnual = info['Salario'] * 12 * 1.05
            bono = "2 -> 5% de bono"
        elif info["Desempenio"] == 3:
            salarioAnual = info['Salario'] * 12 * 1.10
            bono = "3 -> 10% de bono"
        elif info["Desempenio"] == 4:
            salarioAnual = info['Salario'] * 12 * 1.15
            bono = "4 -> 15% de bono"
        else:
            salarioAnual = float(info['Salario']) * 12 * 1.20
            bono = "5 -> 20% de bono"
        #Mostramos la informacion del empleado
        print("| {:<15} | {:<15} | {:>15,.2f} | {:^20} | {:>15,.2f} |".format(
            info['Nombre'], 
            info['Departamento'],
            info['Salario'],
            bono,
            salarioAnual
            ))
        print(90*"-")
        totalSalarios += salarioAnual
        if salarioAnual > maximoSalario:
            maximoSalario = salarioAnual
            empleadoMaximoSalario = info['Nombre']
    #Mostramos el total de salarios y el empleado con el salario más alto
    print(f"Total de salarios anuales: ${totalSalarios:.2f}")
    print(f"Empleado con el salario más alto es: {empleadoMaximoSalario} con un salario de ${maximoSalario}")
    print(50*"=")
except Exception as e:
    print("\t", 45*"*")
    print("\t","Error: ", e)
    print("\t", 45*"*")
    print(50*"=")
    time.sleep(0.5)