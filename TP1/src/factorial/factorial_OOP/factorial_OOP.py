class Factorial:
    def __init__(self):
        pass

    def calculate(self, num):
        if num < 0:
            return "Factorial de un número negativo no existe"
        elif num == 0:
            return 1
        else:
            fact = 1
            while(num > 1):
                fact *= num
                num -= 1
            return fact

    def run(self, min_num, max_num):
        results = {}
        for num in range(min_num, max_num + 1):
            results[num] = self.calculate(num)
        return results

if __name__ == "__main__":
    factorial_calculator = Factorial()

    min_value = int(input("Ingrese el número mínimo: "))
    max_value = int(input("Ingrese el número máximo: "))

    results = factorial_calculator.run(min_value, max_value)

    for num, result in results.items():
        print(f"Factorial de {num} es {result}")

"""Este script define una clase Factorial con un método calculate para calcular el
factorial de un número y un método run(min, max) que calcula el factorial para cada
número en el rango dado. Luego, en el bloque if __name__ == "__main__":, 
se instancia la clase Factorial, se solicitan al usuario los valores mínimos
y máximos, se llama al método run, y se muestran los resultados."""