class Reloj:
    def __init__(self, marca, tipo, material):
        self.marca = marca
        self.tipo = tipo
        self.material = material
        self.precio = int(input('Ingrese el precio del reloj : '))
        
    def detalles(self):
        print(
            f'\n\n------------------\n' +
            f'Detalles del reloj\n' +
            f'------------------\n\n' +
            f'Marca : {self.marca}\n' +
            f'Tipo : {self.tipo}\n' +
            f'Material : {self.material}\n' +
            f'Precio : {self.precio}\n\n'
        )
        
class RelojInteligente(Reloj):
    def __init__(self, marca, tipo, material, pantalla):
        super().__init__(marca, tipo, material)
        self.pantalla = pantalla
        self.sistema = input('Ingrese el sistema operativo del reloj : ')
        self.bateria = int(input('Ingrese la baterial actual del reloj : '))
        
    def encenderReloj(self):
        print(
            f'El tipo de pantalla del reloj es : {self.pantalla}\n' +
            f'El sistema operativo del reloj es : {self.sistema}\n' +
            f'Bateria actual del reloj : {self.bateria}\n\n'
        )
        
        if self.bateria <= 0:
            print(f'El reloj {self.tipo} tiene la bateria baja y no puede encender!!!\n\n')
        else:
            print(f'El reloj {self.tipo} puede encender con normalidad!!!\n\n')
            
reloj_1 = RelojInteligente('Smart', 'Inteligente', 'Metal', 'OLED')
reloj_1.detalles()
reloj_1.encenderReloj()