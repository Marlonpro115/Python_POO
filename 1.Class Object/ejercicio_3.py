class Carro:
    def __init__(self, marca, modelo, velocidad, motor, color):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.motor = motor
        self.color = color
        
    def ObtenerCilindraje(self):
        if self.velocidad > 100:
            return print('Tu carro es demasido veloz!!\n\n')
        else:
            return print('Tal parece que es un poco lento...\n\n')
        
    def ObtenerMarca(self):
        return print(f'La marca de tu carro es {self.marca}')
    
    def ObtenerInfo(self):
        return print( 
            f'--------------------------------\n' +
            f'Informacion del carro : \n' +
            f'Marca : {self.marca}\n' +
            f'Modelo : {self.modelo}\n' +
            f'Velocidad : {self.velocidad}\n' +
            f'Motor : {self.motor}\n' +
            f'Color : {self.color}' +
            f'--------------------------------\n\n'
        )

carro1 = Carro('Nisan', 'kt-8', 100, 'upk-1000', 'rojo')

carro1.ObtenerCilindraje()
carro1.ObtenerMarca()
carro1.ObtenerInfo()