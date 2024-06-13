class Hamburguesa:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def entregar_en_mostrador(self):
        print(f"Hamburguesa {self.tipo} lista para ser retirada en mostrador.")
    
    def retirar_por_cliente(self):
        print(f"Hamburguesa {self.tipo} lista para ser retirada por el cliente.")
    
    def enviar_por_delivery(self):
        print(f"Hamburguesa {self.tipo} lista para ser enviada por delivery.")


# Ejemplo de uso
if __name__ == "__main__":
    hamburguesa_clasica = Hamburguesa("Clásica")
    hamburguesa_clasica.entregar_en_mostrador()
    
    hamburguesa_vegetariana = Hamburguesa("Vegetariana")
    hamburguesa_vegetariana.retirar_por_cliente()
    
    hamburguesa_vegana = Hamburguesa("Vegana")
    hamburguesa_vegana.enviar_por_delivery()