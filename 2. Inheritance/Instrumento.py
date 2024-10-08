class Intrumento:
    def __init__(self, tipo, marca, material):
        self.tipo = tipo
        self.marca = marca
        self.material = material
        self.precio = int(input('Ingrese el precio del producto : '))
        
    def detalles(self):
        print(
            f'\n\n-----------------------\n' +
            f'Detalles del Intrumento\n' +
            f'-----------------------\n' +
            f'Tipo : {self.tipo}\n' +
            f'Marca : {self.marca}\n' +
            f'Material : {self.material}\n' +
            f'Precio : {self.precio}\n\n'
        )
        
class Guitarra(Intrumento):
    def __init__(self, tipo, marca, material, NumeroDeCuerdas):
        super().__init__(tipo, marca, material)
        self.NumeroDeCuerdas = NumeroDeCuerdas
        self.acordesBasicos = int(input('Ingrese cuando acordes hay : '))
        
    def TocarGuitarra(self):
        print(
            f'El numero de cuerdas de la guitarra es : {self.NumeroDeCuerdas}\n\n' +
            f'El numero de acordes es : {self.acordesBasicos}\n\n'
        )
        
        if self.acordesBasicos <= 5:
            print('La guitarra no se puede tocar bien!!!')
        else:
            print('La guitarra se puede tocar con normalidad!!!')
            
guitar_1 = Guitarra('Guitara', 'Proyect', 'Metal', 5)
guitar_1.detalles()
guitar_1.TocarGuitarra()