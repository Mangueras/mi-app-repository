class Biblioteca:
    """Clase que representa una biblioteca."""

    def __init__(self, nombre, ubicacion):
        """
        Inicializa una instancia de la clase Biblioteca.

        Args:
            nombre (str): El nombre de la biblioteca.
            ubicacion (str): La ubicación de la biblioteca.
        """
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.libros = []

    def agregar_libro(self, libro):
        """
        Agrega un libro a la biblioteca.

        Args:
            libro (Libro): El libro a ser agregado a la biblioteca.
        """
        self.libros.append(libro)

    def mostrar_libros(self):
        """Muestra los libros disponibles en la biblioteca."""
        print("Libros disponibles en la biblioteca", self.nombre)
        for libro in self.libros:
            print(libro)

class Libro:
    """Clase que representa un libro."""

    def __init__(self, titulo, autor, genero):
        """
        Inicializa una instancia de la clase Libro.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            genero (str): El género del libro.
        """
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

    def __str__(self):
        """Devuelve una representación en cadena del libro."""
        return f"Título: {self.titulo} - Autor: {self.autor} - Género: {self.genero}"

class Elecciones:
    """Clase que representa un sistema de elecciones."""

    def __init__(self, tema):
        """
        Inicializa una instancia de la clase Elecciones.

        Args:
            tema (str): El tema de las elecciones.
        """
        self.tema = tema
        self.propuestas = []

    def agregar_propuesta(self, propuesta):
        """
        Agrega una propuesta a las elecciones.

        Args:
            propuesta (Propuesta): La propuesta a ser agregada a las elecciones.
        """
        self.propuestas.append(propuesta)

    def mostrar_propuestas(self):
        """Muestra las propuestas para las elecciones."""
        print("Propuestas para las elecciones sobre", self.tema)
        for propuesta in self.propuestas:
            print(propuesta)

class Propuesta:
    """Clase que representa una propuesta para las elecciones."""

    def __init__(self, titulo, descripcion):
        """
        Inicializa una instancia de la clase Propuesta.

        Args:
            titulo (str): El título de la propuesta.
            descripcion (str): La descripción de la propuesta.
        """
        self.titulo = titulo
        self.descripcion = descripcion

    def __str__(self):
        """Devuelve una representación en cadena de la propuesta."""
        return f"Título: {self.titulo}\nDescripción: {self.descripcion}"

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear una biblioteca
    biblioteca_principal = Biblioteca("Biblioteca Central", "Calle Principal")

    # Crear libros y agregarlos a la biblioteca
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela de caballería")
    biblioteca_principal.agregar_libro(libro1)
    biblioteca_principal.agregar_libro(libro2)

    # Mostrar los libros disponibles en la biblioteca
    biblioteca_principal.mostrar_libros()

    # Crear elecciones sobre el tema de educación
    elecciones_educacion = Elecciones("Educación")

    # Crear propuestas para las elecciones
    propuesta1 = Propuesta("Aumento del presupuesto para escuelas públicas", "Incrementar fondos para mejorar la infraestructura y los recursos educativos.")
    propuesta2 = Propuesta("Implementación de clases de programación en todas las escuelas", "Introducir asignaturas de programación desde edades tempranas para preparar a los estudiantes para el futuro tecnológico.")
    elecciones_educacion.agregar_propuesta(propuesta1)
    elecciones_educacion.agregar_propuesta(propuesta2)

    # Mostrar las propuestas para las elecciones sobre educación
    elecciones_educacion.mostrar_propuestas()
