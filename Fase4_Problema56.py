'''    
    Fase 4: Problemas 5 y 6
    Nombre: Jhonathan Damian Guerrero Montoya
    Grupo: 374
    Programa: Ingeniería de Sistemas
    Codigo fuente: autoría propia
    Fecha: 10-may-2025
'''

import time
import sys

#Definimos la función slow_print, que permite dar efectos de escritura lenta en pantalla.
def slow_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def problema5():    
    #Definimos el diccionario reporte, que almacenará los montos a pagar por cada póliza.
    reporte = {}
    #Definimos la función validarCodigo, que valida el código de la póliza ingresado por el usuario.
    def validarCodigo(codigoPoliza):
        try:
            #Validamos que el código de la póliza sea un número de 7 dígitos
            if not codigoPoliza.isdigit():
                raise ValueError("El código de la póliza debe ser un número.")
            elif len(codigoPoliza) != 7:
                raise ValueError("El código de la póliza debe tener 7 dígitos.")
            #Validamos que el primer dígito sea un número entre 1 y 3
            elif int(codigoPoliza[0]) not in range(1, 4):
                raise ValueError("El primer dígito del código de la póliza debe ser un número entre 1 y 3.")
            return True
        
        except ValueError as e:
            print(f"Error: {e}")
            return False
    
    #Definimos la función hacerPago, que solicita al usuario el código de la póliza.
    def calcularMonto(codigoPoliza):
        print("Ingreasa el monto:")
        print(30*"-")
        montoUsuario = input()
        try:
            #Validamos que el monto sea un número
            if not montoUsuario.isdigit():
                raise ValueError("El monto debe ser un número.")
            #Validamos que el monto sea mayor a 0
            elif int(montoUsuario) <= 0:
                raise ValueError("El monto debe ser mayor a 0.")
            #Calculamos el monto a pagar
            elif codigoPoliza[0] == "1":
                return int(montoUsuario) 
            elif codigoPoliza[0] == "2":
                if int(montoUsuario) <= 1000000:
                    return int(montoUsuario)
                else:
                    return int(montoUsuario) * 0.7
            elif codigoPoliza[0] == "3":
                return int(montoUsuario) * 0.65
            
        except ValueError as e:
            print(f"Error: {e}")
            return None
    
    #Definimos la función hacerPago, que solicita al usuario el código de la póliza.
    def hacerPago():
        
        while True:
            print("Introduce el código de tu poliza:")
            print(30*"-")
            codigoPoliza = input()
            #Validamos el código de la póliza
            validacion = validarCodigo(codigoPoliza)
            
            if validacion:
                print(30*"-")
                monto = calcularMonto(codigoPoliza)
                slow_print(f"El monto a pagar a la persona es: {monto}")
                reporte[codigoPoliza] = monto
                break
    
    #Damos la bienvenida al usuario
    slow_print("Bienvenido a la sección del problema 5")
    print(30 * "-")
    time.sleep(0.7)
    
    #Corazon del programa, donde se ejecuta el menú principal al problema 6.
    salir = False
    while not salir:
        print("Seguros Oficial S.A.")
        print(30*"-")
        print("Opción 1: Hacer un pago.")
        print("Opción 2: Salir.")
        slow_print("¿Cuál es su opción?")
        print(30*"-")
        try:
            opcion = int(input())
            if opcion == 1:
                print(30*"-")
                hacerPago()
            elif opcion == 2:
                print(30*"-")
                slow_print("Este es el reporte de pagos:")
                print(30*"-")
                for codigo, monto in reporte.items():
                    print(f"Poliza: {codigo} -> Monto: {monto}")
                print(30*"-")
                print("Total de polizas: ", len(reporte))
                print("Total de pagos: ", sum(reporte.values()))
                print(30*"-")
                slow_print("¡Hasta pronto!")
                salir = True
            else:
                print('Opcion no valida debe ser 1 o 2')
                time.sleep(1)
        except Exception as e:
            print(f"Ha ocurrido un error: '{e}'")
            print("Debes de ingresar un número")
            time.sleep(1)

def problema6():
    #Damos la bienvenida al usuario
    slow_print("Bienvenido a la seccion del problema 6")
    print(30 * "-")
    #Definimos la función para leer los productos
    def leerProductos():
        #Definimos el diccionario productos, que almacenará los productos y sus valores.
        productos = {}
        
        #Solicitamos al usuario el producto y sus valores.
        while True:
            print("Introduce el nombre del producto o 0 (cero) para salir:")
            print(30*"-")
            nameProduct = input()
            if nameProduct == "0":
                break
            else:
                print("Introduce el valor unitario del producto sin puntos ni comas:")
                print(30*"-")
                valueProduct = input()
                print("Introduce la cantidad del producto sin puntos ni comas:")
                print(30*"-")
                cantProduct = input()
                try:
                    #Validamos que los valores sea un número
                    if not valueProduct.isdigit() or not cantProduct.isdigit():
                        raise ValueError("El valor debe ser un número.")
                    #Validamos que el valor sea mayor a 0
                    elif int(valueProduct) <= 0 or int(cantProduct) <= 0:
                        raise ValueError("El valor debe ser mayor a 0.")
                    else:
                        productos[nameProduct] = {"Precio": float(valueProduct), "Cantidad": int(cantProduct)}
                        print(f"Producto: {nameProduct}, Precio: {float(valueProduct)}, Cantidad: {int(cantProduct)}")
                    print(30*"-")   
                    slow_print("Producto agregado correctamente.")
                    print(30*"-")
                    print(30*"-")
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
        
        #Calculamos el total a pagar
        total = 0
        for product, values in productos.items():
            total += values["Precio"] * values["Cantidad"]
        
        return len(productos), total

    #Definimos la funcion para determinar el premio
    def premio(nCC, dia):
        
        #Sumamos los dígitos de la cédula
        sumaDigitos = sum(int(d) for d in nCC)
        #Validamos que la suma de los dígitos sea igual al día de la compra
        if sumaDigitos == int(dia):
            return True
        else:
            return False

    #Definimos la función para realizar el cobro
    def cobrar():
    
        cantidadProductos, totalCompra = leerProductos()
        slow_print(f"Total a pagar: {totalCompra}")
        time.sleep(0.7)
        if cantidadProductos != 0:
            print("Validemos si el cliente tiene premio")
            print("Ingrese el número de cédula del cliente:")
            print(30*"-")
            cedulaCliente = input()
            print("Ingrese el día de la compra:")
            print(30*"-")
            diaCompra = input()
            try:
                #Validamos que el número de cédula sea un número
                if not cedulaCliente.isdigit():
                    raise ValueError("El número de cédula debe ser un número.")
                #Validamos que el día de la compra sea un número
                elif not diaCompra.isdigit():
                    raise ValueError("El día de la compra debe ser un número.")
                #Validamos que el día de la compra sea mayor a 0 y menor o igual a 31
                elif int(diaCompra) <= 0 or int(diaCompra) > 31:
                    raise ValueError("El día de la compra debe ser mayor a 0 y menor o igual a 31.")
                else:
                    if premio(cedulaCliente, diaCompra):
                        print("Felicidades, el cliente tiene premio de descuento del 100% de la compra")
                        totalCompra = 0
                        slow_print(f"Total a pagar: {totalCompra}")
                        print(30*"-")
                        time.sleep(0.2)
                    else:
                        print("Lo sentimos, el cliente no tiene premio")
                        slow_print(f"Total a pagar: {totalCompra}")
                        time.sleep(0.2)
            except ValueError as e:
                print(f"Error: {e}")

    salir = False
    while not salir:
        print("Almacenes LEY S. A.")
        print(30*"-")
        print("1. Hacer un cobro.")
        print("2. Salir.")
        print("¿Cuál es su opción?")
        print(30*"-")
        opcion = input()
        #Validamos la opción del menú
        try:
            if not opcion.isdigit():
                raise ValueError("La opción debe ser un número.")
            else:
                opcion=int(opcion)
                if not opcion in range(1,3):
                    raise ValueError("La opción debe ser 1 o 2.")
                elif opcion == 1:
                    print(30*"-")
                    slow_print("Realizando el cobro")
                    cobrar()
                    time.sleep(0.7)
                elif opcion == 2:
                    slow_print("Saliendo de Almacenes LEY...")
                    time.sleep(0.2)
                    salir = True
                
        except ValueError as e:
            print(f"Error: {e}")
            continue

salir = False
while not salir:
    print(30 * "-")
    print("Bienvenido al programa, seleccione una opción:")
    print("1. Problema 5")
    print("2. Problema 6")
    print("0. Salir")
    print(30 * "-")
    opcion = int(input("ingrese un número (0,1,2): \n"))
    if opcion == 0:
        slow_print("Gracias por usar el programa, hasta pronto.")
        salir = True
    elif opcion == 1:
        problema5()
    elif opcion == 2:
        problema6()
    else:
        slow_print("Opción no válida, intente de nuevo.")