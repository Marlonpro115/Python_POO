# ejercicio 2: Clases de  Vehículos con Polimorfismo
# Crea tres clases: Carro, Moto y Bicicleta, cada una con un método descripcion() que describa el tipo de vehículo.

class Carro:
    def __init__(self, marca, modelo, color):
        self.velocidad = int(input('Ingrese la velocidad del carro : '))
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def descripcion(self):
        print(
            f'=====================\n' +
            f'Informacion del carro\n' +
            f'=====================\n\n' +
            f'Marca : {self.marca}\n' +
            f'Modelo : {self.modelo}\n' +
            f'Color : {self.color}\n' +
            f'Velocidad : {self.velocidad}\n\n' +
            f'====================='
        )
        
class Moto:
    def __init__(self, marca, modelo, color):
        self.velocidad = int(input('Ingrese la velocidad de la moto : '))
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def descripcion(self):
        print(
            f'======================\n' +
            f'Informacion de la moto\n' +
            f'======================\n\n' +
            f'Marca : {self.marca}\n' +
            f'Modelo : {self.modelo}\n' +
            f'Color : {self.color}\n' +
            f'Velocidad : {self.velocidad}\n\n' +
            f'======================\n\n'
        )
        
class Bicicleta:
    def __init__(self, marca, modelo, color):
        self.tipo = input('Ingresa el tipo de bicicleta : ')
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def descripcion(self):
        print(
            f'===========================\n' +
            f'Informacion de la bicicleta\n' +
            f'===========================\n\n' +
            f'Marca : {self.marca}\n' +
            f'Modelo : {self.modelo}\n' +
            f'Color : {self.color}\n' +
            f'Tipo : {self.tipo}\n\n' +
            f'===========================\n\n'
        )

def descripcion(vehiculos):
    vehiculos.descripcion()
    
    
objetcCarro = Carro('HIUNDA', 'jt-js', 'Rojo')
objectMoto = Moto('Kawasaki', 'jijd34-52', 'Negro')
objectBicicleta = Bicicleta('Red', 'h-678', 'Azul')

descripcion(objetcCarro)
descripcion(objectMoto)
descripcion(objectBicicleta)
