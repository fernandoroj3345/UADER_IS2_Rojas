class Factorial:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Factorial, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def calculate(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("El número debe ser un entero no negativo")
        return self._factorial(n)

    def _factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self._factorial(n - 1)

# Prueba del patrón Singleton con la clase Factorial
factorial1 = Factorial()
factorial2 = Factorial()

print(factorial1 is factorial2)  # True, ambas referencias apuntan a la misma instancia

# Calcular factorial
n = 5
print(f"Factorial de {n} es {factorial1.calculate(n)}")  # Factorial de 5 es 120

# Otra clase utilizando la misma instancia de Factorial
class AnotherClass:
    def __init__(self):
        self.factorial_calculator = Factorial()

    def get_factorial(self, n):
        return self.factorial_calculator.calculate(n)

# Prueba con AnotherClass
another_instance = AnotherClass()
print(f"Factorial de {n} desde AnotherClass es {another_instance.get_factorial(n)}")  # Factorial de 5 desde AnotherClass es 120