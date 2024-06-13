#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
class Factorial:
    """
    Clase para calcular factoriales de números enteros no negativos.

    Atributos:
        min (int): El límite inferior del rango para el cálculo de factoriales.
        max (int): El límite superior del rango para el cálculo de factoriales.

    Métodos:
        __init__(self, min, max): Inicializa la instancia de la clase con los valores de min y max.
        run(self): Calcula y muestra los factoriales entre min y max.
    """

    def __init__(self, min, max):
        """
        Constructor de la clase.

        Argumentos:
            min (int): El límite inferior del rango para el cálculo de factoriales.
            max (int): El límite superior del rango para el cálculo de factoriales.
        """
        self.min = min
        self.max = max

    def run(self):
        """
        Calcula y muestra los factoriales entre min y max.
        """
        for num in range(self.min, self.max + 1):
            factorial = 1
            for i in range(2, num + 1):
                factorial *= i
            print(f"Factorial de {num} es {factorial}")


if __name__ == "__main__":
    # Ejemplo de uso
    factorial_obj = Factorial(1, 10)
    factorial_obj.run()