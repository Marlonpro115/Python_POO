class Animal:
    def __init__(self, nombre, edad, raza, comida, tipo):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.comida = comida
        self.tipo = tipo
        
    def Alimento(self):
        return print(f'El alimento del animal {self.nombre} es : {self.comida}\n\n')
    
    def TipoDeAnimal(self):
        return print(f'La raza del animal {self.nombre} es de tipo : {self.raza}\n\n')
    
    def ObtenerEdad(self):
        if self.edad <= 10:
            return print('Tu animal es muy joven\n\n')
        else:
            return print('Tu animal es muy Viejo\n\n')
        
animal1 = Animal('Juan', 14, 'Canina', 'Comida de perros', 'perro')

animal1.Alimento()
animal1.TipoDeAnimal()
animal1.ObtenerEdad()