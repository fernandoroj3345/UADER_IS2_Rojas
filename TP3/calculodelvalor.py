class TaxCalculator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TaxCalculator, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def calculate_taxes(self, base_amount):
        if base_amount < 0:
            raise ValueError("El importe base imponible debe ser un número no negativo")
        
        iva = base_amount * 0.21
        iibb = base_amount * 0.05
        municipal_contributions = base_amount * 0.012
        
        total_taxes = iva + iibb + municipal_contributions
        return total_taxes

# Prueba del patrón Singleton con la clase TaxCalculator
tax_calculator1 = TaxCalculator()
tax_calculator2 = TaxCalculator()

print(tax_calculator1 is tax_calculator2)  # True, ambas referencias apuntan a la misma instancia

# Calcular impuestos
base_amount = 1000
total_taxes = tax_calculator1.calculate_taxes(base_amount)
print(f"Total de impuestos sobre {base_amount} es {total_taxes:.2f}")  # Total de impuestos sobre 1000 es 272.00

# Otra clase utilizando la misma instancia de TaxCalculator
class SomeOtherClass:
    def __init__(self):
        self.tax_calculator = TaxCalculator()

    def get_total_taxes(self, base_amount):
        return self.tax_calculator.calculate_taxes(base_amount)

# Prueba con SomeOtherClass
another_instance = SomeOtherClass()
print(f"Total de impuestos sobre {base_amount} desde SomeOtherClass es {another_instance.get_total_taxes(base_amount):.2f}")  # Total de impuestos sobre 1000 desde SomeOtherClass es 272.00