# Ejercicio 3: Clase Libro
# Crea una clase Libro que tenga los siguientes atributos privados: titulo, autor, y isbn. Implementa métodos getter y setter para cada atributo. 
# Además, añade un atributo público editorial y un método que muestre la información completa del libro.

class Libro:
    def __init__(self, titulo, autor, isbn, publicoEditorial):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.publicoEditorial = publicoEditorial

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getIsbn(self):
        return self.__isbn

    def setTitulo(self, newTitle):
        self.__titulo = newTitle

    def setAutor(self, newAutor):
        self.__autor = newAutor

    def setIsbn(self, newIsbn):
        self.__isbn = newIsbn

    def detalles(self):
        print(
            f'-------------------\n' +
            f'Detalles del libro\n' +
            f'-------------------\n\n'
            f'Titulo : {self.__titulo}\n' +
            f'Autor : {self.__autor}\n' +
            f'Isbn : {self.__isbn}\n' +
            f'Publico editorial : {self.publicoEditorial}\n\n'
        )

libro = Libro('Mariposas', 'Link', '1514kakfksy24', 'Publico')
libro.detalles()

print('---------------------------------------\n\n')

libro.setTitulo('Las mariposas')
print(f'Titulo : {libro.getTitulo()}\n')
libro.setAutor('Link Marcus')
print(f'Precio : {libro.getAutor()}\n')
libro.setIsbn('siowh9184')
print(f'ISBN : {libro.getIsbn()}\n')
print(f'Publico editorial : {libro.publicoEditorial}\n\n')