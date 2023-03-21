class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        if edad < 0:
            print("La edad no puede ser negativa")
        else:
            self.edad = edad

    def set_dni(self, dni):
        self.dni = dni

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_dni(self):
        return self.dni

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18