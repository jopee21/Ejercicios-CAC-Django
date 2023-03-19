class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def get_bonificacion(self):
        return self.__bonificacion

    def es_titular_valido(self):
        return self._titular.es_mayor_de_edad() and self._titular.get_edad() < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        return f"Cuenta Joven\nTitular: {self._titular.mostrar()}\nCantidad: {self._cantidad}\nBonificación: {self.__bonificacion}"