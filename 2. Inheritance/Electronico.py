class Electronico:
    def __init__(self, marca, modelo, procesador):
        self.marca = marca
        self.modelo = modelo
        self.procesadro = procesador
        self.ram = int(input('Ingrese la cantidad de ram(Gb) : '))
        
    def detalles(self):
        print(
            f'\n\n------------------------\n' +
            f'Detalles del Electronico\n' +
            f'------------------------\n\n' +
            f'Marca : {self.marca}\n' +
            f'Modelo : {self.modelo}\n' +
            f'Procesador : {self.procesadro}\n' +
            f'Ram : {self.ram}\n\n'
        )
        
class Laptop(Electronico):
    def __init__(self, marca, modelo, procesador, discoDuro):
        super().__init__(marca, modelo, procesador)
        self.discoDuro = discoDuro
        self.bateria = int(input('Ingrese la duracion de la bateria en horas : '))
        
    def encenderLaptop(self):
        print(
            f'Disco duro de la laptop : {self.discoDuro}\n\n' +
            f'Duracion de la bateria en horas : {self.bateria}\n\n'
        )
        
        if self.bateria <= 0:
            print(f'Al parecer la laptop, modelo {self.modelo} y marca {self.marca} no podra encender debido aque no tiene bateria!!!\n\n')
        else:
            print(f'Al parecer la laptop, modelo {self.modelo} y marca {self.marca} Podras usarla con normalidad!!!\n\n')
            
            
laptop_1 = Laptop('HONOR', 'H-PO899', 'S23-ULTRA', 'SSD 512GB')
laptop_1.detalles()
laptop_1.encenderLaptop()