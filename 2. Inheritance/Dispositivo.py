class Dispositivo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.ano = año
        self.capacidad = int(input('Ingrese la capacidad de la bateria(mAh) : '))
        
    def detalles(self):
        print(
            f'\n\n------------------------\n' +
            f'Detalles del dispositivo\n' +
            f'------------------------\n\n' +
            f'Marca : {self.marca}\n' +
            f'Modelo : {self.modelo}\n' +
            f'Año de salida : {self.ano}' +
            f'Capacidad(mAh) : {self.capacidad}\n\n'
        )
    
    
class Stmarfhone(Dispositivo):
    def __init__(self, marca, modelo, año, sistema):
        super().__init__(marca, modelo, año)
        self.sistema = sistema
        self.conectividad = input('Ingrese su tipo de conectividad(4G, 3G) : ')
        
    def encender(self):
        print(
            f'El sistema operativo del telefono : {self.sistema}\n\n' +
            f'Tipo de conectividad : {self.conectividad}\n\n'
            )
        
        if self.capacidad <= 0:
            print(f'El starfhone no puede encender porque esta a {self.capacidad}% bateria!!!\n\n')
        else:
            print(f'El telefono si puede encender con normalidad!!!\n\n')
        return
    
telefono_1=Stmarfhone('Samsumg', 's-45l', 2004, 'Android')
telefono_1.detalles()
telefono_1.encender()