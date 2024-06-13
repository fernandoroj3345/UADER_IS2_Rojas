"""Implemente una clase “factura” que tenga un importe correspondiente al total
de la factura pero de acuerdo a la condición impositiva del cliente (IVA
Responsable, IVA No Inscripto, IVA Exento) genere facturas que indiquen tal
condición."""

class Factura:
    def __init__(self, importe, condicion_impositiva):
        self.importe = importe
        self.condicion_impositiva = condicion_impositiva

    def imprimir_factura(self):
        print("----- Factura -----")
        print(f"Importe Total: ${self.importe:.2f}")
        print(f"Condición Impositiva: {self.condicion_impositiva}")
        print("-------------------")

# Ejemplo de uso
if __name__ == "__main__":
    factura_responsable = Factura(1000, "IVA Responsable")
    factura_responsable.imprimir_factura()
    
    factura_no_inscripto = Factura(850, "IVA No Inscripto")
    factura_no_inscripto.imprimir_factura()
    
    factura_exento = Factura(1200, "IVA Exento")
    factura_exento.imprimir_factura()