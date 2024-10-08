class Electrodomesticos:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        self.capacidad = int(input('Capacidad electrica : '))
        
    def detalles(self):
        print(
            f'\n-----------------------------\n' +
            f'Detalles del electrodomestico\n' +
            f'-----------------------------\n\n' +
            f'Marca : {self.marca}\n' +
            f'Color : {self.color}\n' +
            f'Capacidad : {self.capacidad}\n\n'
            )
        
class Refrigerador(Electrodomesticos):
    def __init__(self, marca, color, tipo):
        super().__init__(marca, color)
        self.tipo = tipo
        self.temperatura = int(input('Ingrese la temperatura del refrigerador (°C) : '))
        
        
    def ajustarTemperatura(self):
        print(f'El tipo de refigerador : {self.tipo}\n')
        
        if self.temperatura > 5:
            print(f'Deberias ajutar la tempratura de {self.temperatura} a menor 5\n\n')
        else:
            print(f'La temperatura del refigerador es perfecta!!!\n\n')
            
Electro_1 = Refrigerador('Honor', 'Rojo', 'Super Veloz')
Electro_1.detalles()
Electro_1.ajustarTemperatura()