class Perro:
    def __init__(self, nombre, raza, edad, peso, color, dueño, telefono):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.dueño = dueño
        self.telefono = telefono
        self.estado = "NO ATENDIDO"
        self.tamaño = "perro grande" if peso >= 10 else "perro pequeño"
    
    def registrar(self):
        self.estado = "ATENDIDO"
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Dueño: {self.dueño}")
        print(f"Teléfono: {self.telefono}")
        print(f"Estado: {self.estado}")
        print(f"Tamaño: {self.tamaño}")


nombre = input("Nombre del perro: ")
raza = input("Raza del perro: ")
edad = int(input("Edad del perro: "))
peso = float(input("Peso del perro (kg): "))
color = input("Color del perro: ")
dueño = input("Nombre del dueño: ")
telefono = input("Teléfono del dueño: ")

perro = Perro(nombre, raza, edad, peso, color, dueño, telefono)
perro.registrar()
perro.mostrar_informacion()
