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