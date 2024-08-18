class DispositivoElectronico:
    def __init__(self, tipo, modelo, procesador, memoria, almacenamiento, precio_compra):
        self.tipo = tipo
        self.marca = "PHR"
        self.modelo = modelo
        self.procesador = procesador
        self.memoria = memoria
        self.almacenamiento = almacenamiento
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.7
        self.origen = "importado"

    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Procesador: {self.procesador}")
        print(f"Memoria: {self.memoria} GB")
        print(f"Almacenamiento: {self.almacenamiento} GB")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")
        print(f"Origen: {self.origen}")

# Función para registrar dispositivos
def registrar_dispositivos():
    dispositivos = []

    for _ in range(2):  # Registrar al menos dos dispositivos de cada tipo
        tipo = input("Tipo de dispositivo (celular/tablet/portátil): ")
        modelo = input("Modelo del dispositivo: ")
        procesador = input("Procesador del dispositivo: ")
        memoria = int(input("Memoria RAM del dispositivo (GB): "))
        almacenamiento = int(input("Almacenamiento del dispositivo (GB): "))
        precio_compra = float(input("Precio de compra del dispositivo: "))

        dispositivo = DispositivoElectronico(tipo, modelo, procesador, memoria, almacenamiento, precio_compra)
        dispositivos.append(dispositivo)

    return dispositivos

# Función para mostrar información de los dispositivos
def mostrar_dispositivos(dispositivos):
    for dispositivo in dispositivos:
        dispositivo.mostrar_informacion()
        print("-" * 30)

# Ejemplo de uso
dispositivos = registrar_dispositivos()
mostrar_dispositivos(dispositivos)
