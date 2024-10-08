
class Celular:
    def __init__(self, modelo, marca, ram, bateria, cpu):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.bateria = bateria
        self.cpu = cpu
        
    def MostrarDetalles(self):
        print(
            f'--------------------------------\n' +
            f'Informacion del celular :\n\n' +
            f'Modelo : {self.modelo}\n' +
            f'Marca : {self.marca}\n' +
            f'Ram : {self.ram}\n' +
            f'Bateria : {self.bateria}\n' +
            f'Cpu : {self.cpu}\n' +
             f'--------------------------------\n\n'
            )

    def Carga(self):
        if self.bateria <= 1000 :
            print(f'El celular esta descargado!\n\n')
        else :
            print('Celular con buena carga\n\n')

    def Rendimiento(self):
        if self.cpu <= 500:
            print(f'El rendimiento de {self.marca} es algo lento!!\n\n')
        else:
            print(f'Vaya que buen redimiento tiene tu {self.marca}!!\n\n')

clase = Celular('ut-p4561', 'Xiaomi', 4, 5000, 600)
clase.MostrarDetalles()
clase.Carga()
clase.Rendimiento()