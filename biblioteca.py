# Clase Libro
class Libro:
    def __init__(self, id_libro, titulo, autor, año_publicacion):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible = True

    def mostrar_informacion(self):
        estado = 'Disponible' if self.disponible else 'Prestado'
        print(f"ID: {self.id_libro}, Título: {self.titulo}, Autor: {self.autor}, Año: {self.año_publicacion}, Estado: {estado}")

# Clase Usuario
class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []

    def mostrar_informacion(self):
        print(f"ID Usuario: {self.id_usuario}, Nombre: {self.nombre}, Libros Prestados: {[libro.titulo for libro in self.libros_prestados]}")

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"El libro '{libro.titulo}' ha sido agregado a la biblioteca.")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"El usuario '{usuario.nombre}' ha sido registrado.")

    def prestar_libro(self, id_libro, id_usuario):
        libro = next((l for l in self.libros if l.id_libro == id_libro), None)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

        if libro and usuario:
            if libro.disponible:
                libro.disponible = False
                usuario.libros_prestados.append(libro)
                print(f"El libro '{libro.titulo}' ha sido prestado a '{usuario.nombre}'.")
            else:
                print(f"El libro '{libro.titulo}' no está disponible.")
        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, id_libro, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            libro = next((l for l in usuario.libros_prestados if l.id_libro == id_libro), None)
            if libro:
                libro.disponible = True
                usuario.libros_prestados.remove(libro)
                print(f"El libro '{libro.titulo}' ha sido devuelto por '{usuario.nombre}'.")
            else:
                print(f"El usuario '{usuario.nombre}' no tiene prestado el libro con ID {id_libro}.")
        else:
            print("Usuario no encontrado.")

    def mostrar_libros(self):
        print("\nListado de Libros:")
        for libro in self.libros:
            libro.mostrar_informacion()

    def mostrar_usuarios(self):
        print("\nListado de Usuarios:")
        for usuario in self.usuarios:
            usuario.mostrar_informacion()

# Función principal
def main():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Sistema de Gestión de Biblioteca ---")
        print("1. Agregar Libro")
        print("2. Registrar Usuario")
        print("3. Prestar Libro")
        print("4. Devolver Libro")
        print("5. Mostrar Libros")
        print("6. Mostrar Usuarios")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_libro = input("Ingrese el ID del libro: ")
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            año_publicacion = input("Ingrese el año de publicación: ")
            libro = Libro(id_libro, titulo, autor, año_publicacion)
            biblioteca.agregar_libro(libro)

        elif opcion == '2':
            id_usuario = input("Ingrese el ID del usuario: ")
            nombre = input("Ingrese el nombre del usuario: ")
            usuario = Usuario(id_usuario, nombre)
            biblioteca.registrar_usuario(usuario)

        elif opcion == '3':
            id_libro = input("Ingrese el ID del libro a prestar: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.prestar_libro(id_libro, id_usuario)

        elif opcion == '4':
            id_libro = input("Ingrese el ID del libro a devolver: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.devolver_libro(id_libro, id_usuario)

        elif opcion == '5':
            biblioteca.mostrar_libros()

        elif opcion == '6':
            biblioteca.mostrar_usuarios()

        elif opcion == '7':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción correcta.")

if __name__ == "__main__":
    main()
