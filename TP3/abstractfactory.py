""" Aplicación de Gestión de Vehículos
Imagina que estás desarrollando una aplicación que maneja diferentes tipos de vehículos. Necesitas crear vehículos con características específicas para diferentes marcas, como Toyota y Ford. Cada marca tiene su propia implementación de autos y camionetas.

Interfaz Abstracta para la Fábrica
Definiremos una interfaz abstracta para la fábrica que declarará métodos para crear un auto y una camioneta."""



from abc import ABC, abstractmethod

# Interfaz abstracta para la fábrica
class VehiculoFactory(ABC):
    @abstractmethod
    def crear_auto(self):
        pass
    
    @abstractmethod
    def crear_camioneta(self):
        pass

# Interfaz abstracta para los productos
class Auto(ABC):
    @abstractmethod
    def caracteristicas(self):
        pass

class Camioneta(ABC):
    @abstractmethod
    def caracteristicas(self):
        pass

# Implementaciones concretas para Toyota
class ToyotaAuto(Auto):
    def caracteristicas(self):
        print("Auto Toyota: Modelo Corolla, Motor 1.8L")

class ToyotaCamioneta(Camioneta):
    def caracteristicas(self):
        print("Camioneta Toyota: Modelo Hilux, Motor 2.8L")

class ToyotaFactory(VehiculoFactory):
    def crear_auto(self):
        return ToyotaAuto()
    
    def crear_camioneta(self):
        return ToyotaCamioneta()

# Implementaciones concretas para Ford
class FordAuto(Auto):
    def caracteristicas(self):
        print("Auto Ford: Modelo Focus, Motor 2.0L")

class FordCamioneta(Camioneta):
    def caracteristicas(self):
        print("Camioneta Ford: Modelo Ranger, Motor 3.2L")

class FordFactory(VehiculoFactory):
    def crear_auto(self):
        return FordAuto()
    
    def crear_camioneta(self):
        return FordCamioneta()

# Cliente que usa la fábrica abstracta
def mostrar_caracteristicas(factory: VehiculoFactory):
    auto = factory.crear_auto()
    camioneta = factory.crear_camioneta()
    auto.caracteristicas()
    camioneta.caracteristicas()

# Ejemplo de uso
if __name__ == "__main__":
    # Supongamos que queremos ver las características de los vehículos Toyota
    toyota_factory = ToyotaFactory()
    mostrar_caracteristicas(toyota_factory)
    
    print()

    # Ahora queremos ver las características de los vehículos Ford
    ford_factory = FordFactory()
    mostrar_caracteristicas(ford_factory)