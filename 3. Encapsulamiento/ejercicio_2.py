# Ejercicio 2: Clase Producto
# Crea una clase Producto que tenga los siguientes atributos privados: nombre, precio. La clase también debe incluir los atributos públicos, cantidad, categoría. 
# Implementa métodos getter y setter para cada atributo privado. Además, crea un método que muestre toda la información del producto.

class Producto:
    def __init__(self, nombre, precio, publicos, cantidad, categoria):
        self.__nombre = nombre
        self.__precio = precio
        self.publicos = publicos
        self.cantidad = cantidad
        self.categoria = categoria

    def name(self):
        return self.__nombre

    def precio(self):
        return self.__precio

    def setName(self, newName):
        self.__nombre = newName

    def setPrecio(self, newPrecio):
        self.__precio = newPrecio

    def detalles(self):
        print(
            f'\n---------------------\n' +
            f'Detalles del producto' +
            f'---------------------\n\n' +
            f'Nombre : {self.__nombre}\n' +
            f'Precio : {self.__precio}\n' +
            f'Publico : {self.publicos}\n' +
            f'Cantidad : {self.cantidad}\n' +
            f'Categoria : {self.categoria}\n\n'
        )

producto = Producto('LavaRopa', 2000, 'Si', 40, 'Electrico')

producto.detalles()

print('---------------------------------------\n\n')

producto.setName('Licuadora')
print(f'Nombre : {producto.name()}\n')
producto.setPrecio(5000)
print(
    f'Precio : {producto.precio()}\n' +
    f'Publico : {producto.publicos}\n' +
    f'Cantidad : {producto.cantidad}\n' +
    f'Categoria : {producto.categoria}\n'
)