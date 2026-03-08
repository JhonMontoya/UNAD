''' 
    Este archivo contiene el programa de la tarea 5 del curso de programa que genera contraseñas de 
    forma aleatoria fue desarrollado por :
    Jhonathan Damian Guerrero Montoya
    Grupo 240
'''

import random
import string

# Generador base (clase padre)
class GeneradorBase:
    def generar(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases.")

# Generador de contraseñas (clase hija)
class GeneradorContrasena(GeneradorBase):
    def __init__(self, longitud):
        self.__longitud = longitud 

        # Validamos la longitud mínima
        if self.__longitud < 8:
            raise ValueError("La longitud mínima permitida es 8 caracteres.")

        # Conjuntos permitidos
        self.numeros = string.digits
        self.mayusculas = string.ascii_uppercase
        self.minusculas = string.ascii_lowercase
        self.especiales = "¿¡?=)(/¨*+-%&$#!."

    #Metodo para validar que no haya caracteres repetidos
    def __validar_unicidad(self, caracteres):
        if len(caracteres) != len(set(caracteres)):
            raise ValueError("Error: Se generaron caracteres repetidos.")
        return True

    #Metodo para generar la contraseña
    def generar(self):
        try:
            # 1. Obligatorio: un carácter de cada tipo
            password = [
                random.choice(self.numeros),
                random.choice(self.mayusculas),
                random.choice(self.minusculas),
                random.choice(self.especiales)
            ]

            # 2. Crear un pool de caracteres permitidos SIN REPETIR
            pool = list(set(self.numeros + self.mayusculas + self.minusculas + self.especiales))

            # Quitar los que ya se usaron
            for c in password:
                if c in pool:
                    pool.remove(c)

            # 3. Completar la longitud solicitada
            faltantes = self.__longitud - len(password)
            password.extend(random.sample(pool, faltantes))

            # 4. Mezclar para evitar orden predecible
            random.shuffle(password)

            # 5. Validar que no existan repetidos
            self.__validar_unicidad(password)

            return "".join(password)

        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception("Ha ocurrido un error inesperado:", e)

#Raiz principal del programa
def main():
    try:
        print("=== Generador de Contraseñas Seguras ===")
        longitud = int(input("Ingrese la longitud deseada (mínimo 8): "))

        generador = GeneradorContrasena(longitud)
        contrasena = generador.generar()

        print("\nContraseña generada exitosamente:")
        print(contrasena)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()
