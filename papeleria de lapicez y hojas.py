class Articulo:
    def __init__(self, tipo, especificacion, precio_compra):
        self.tipo = tipo
        self.especificacion = especificacion
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.30

    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Especificación: {self.especificacion}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")


def registrar_articulos():
    articulos = []

    for _ in range(2):  
        tipo = "Cuaderno"
        especificacion = input("Especificación del cuaderno (50 o 100 hojas): ")
        precio_compra = float(input("Precio de compra del cuaderno: "))
        cuaderno = Articulo(tipo, f"{especificacion} hojas, marca HOJITAS", precio_compra)
        articulos.append(cuaderno)

    for _ in range(2):  
        tipo = "Lápiz"
        especificacion = input("Especificación del lápiz (grafito o colores): ")
        precio_compra = float(input("Precio de compra del lápiz: "))
        lapiz = Articulo(tipo, f"{especificacion}, marca RAYAS", precio_compra)
        articulos.append(lapiz)

    return articulos


def mostrar_articulos(articulos):
    for articulo in articulos:
        articulo.mostrar_informacion()
        print("-" * 30)


articulos = registrar_articulos()
mostrar_articulos(articulos)
