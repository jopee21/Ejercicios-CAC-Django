from abc import ABC
class Cuenta(ABC):
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print(f"Titular: {self.titular.get_nombre()}, Cantidad: {self.__cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad

cuenta1 = Cuenta("Juan Pérez", 5000)
assert cuenta1.titular == "Juan Pérez"
assert cuenta1.get_cantidad() == 5000

cuenta2 = Cuenta("Ana López", 1000)
cuenta2.ingresar(500)
assert cuenta2.get_cantidad() == 1500

print(cuenta1.mostrar())
print(cuenta2.mostrar())