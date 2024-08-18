class Auto:
    def __init__(self, marca, modelo, año, color, tipo_combustible, cilindrada, transmision, precio_compra, origen, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo_combustible = tipo_combustible
        self.cilindrada = cilindrada
        self.transmision = transmision
        self.precio_compra = precio_compra
        self.origen = origen
        self.kilometraje = kilometraje
        self.ruedas = 4
        self.capacidad_pasajeros = 5
        self.precio_venta = precio_compra * 1.4

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo de combustible: {self.tipo_combustible}")
        print(f"Cilindrada: {self.cilindrada} cc")
        print(f"Transmisión: {self.transmision}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Origen: {self.origen}")
        print(f"Kilometraje: {self.kilometraje} km")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")

# Función para registrar autos
def registrar_autos():
    autos = []

    for _ in range(2):  # Registrar al menos dos autos
        marca = input("Marca del auto: ")
        modelo = input("Modelo del auto: ")
        año = int(input("Año del auto: "))
        color = input("Color del auto: ")
        tipo_combustible = input("Tipo de combustible del auto: ")
        cilindrada = int(input("Cilindrada del auto (cc): "))
        transmision = input("Transmisión del auto (manual/automática): ")
        precio_compra = float(input("Precio de compra del auto: "))
        origen = input("Origen del auto (nacional/importado): ")
        kilometraje = int(input("Kilometraje del auto: "))

        auto = Auto(marca, modelo, año, color, tipo_combustible, cilindrada, transmision, precio_compra, origen, kilometraje)
        autos.append(auto)

    return autos


def mostrar_autos(autos):
    for auto in autos:
        auto.mostrar_informacion()
        print("-" * 30)


autos = registrar_autos()
mostrar_autos(autos)
