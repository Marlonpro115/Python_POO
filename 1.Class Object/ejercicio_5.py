class Motos:
    def __init__(self, marca, modelo, velocidad, motor, color):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.motor = motor
        self.color = color

    def ObtenerInfo(self):
        print(
            f'--------------------------------\n' +
            f'Información de la moto:\n' +
            f'Marca: {self.marca}\n' +
            f'Modelo: {self.modelo}\n' +
            f'Velocidad máxima: {self.velocidad} km/h\n' +
            f'Motor: {self.motor}\n' +
            f'Color: {self.color}\n' +
            f'--------------------------------\n'
        )

    def ObtenerMaximaVelocidad(self):
        print(f'La velocidad máxima de la moto es: {self.velocidad} km/h')

    def Cilindraje(self):
        print(f'El cilindraje de la moto es: {self.motor}')

moto1 = Motos('Yamaha', 'YZF-R1', 299, '998cc', 'Azul')

moto1.ObtenerInfo()
moto1.ObtenerMaximaVelocidad()
moto1.Cilindraje()