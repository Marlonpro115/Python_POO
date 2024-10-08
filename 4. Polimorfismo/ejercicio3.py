# Ejercicio 3: Animales con Polimorfismo
# Crea tres clases: Perro, Gato, y Pájaro, cada una con un método sonido() que haga el sonido correspondiente.

class Perro:
    def __init__(self, raza, sexo, edad):
        self.peso = int(input('Ingrese el peso : '))
        self.raza = raza
        self.sexo = sexo
        self.edad = edad
        
    def mostrar_info(self):
        print(
            f'=====================\n' +
            f'Informacion del perro\n' +
            f'=====================\n\n' +
            f'Raza : {self.raza}\n' +
            f'Sexo : {self.sexo}\n' +
            f'Edad : {self.edad}\n' +
            f'Peso : {self.peso}\n' +
            f'=====================\n\n'
        )
        
    def sonido(self):
        print('El perro hace : "Guau!!"')
        
class Gato:
    def __init__(self, raza, sexo, edad):
        self.peso = int(input('Ingrese el peso : '))
        self.raza = raza
        self.sexo = sexo
        self.edad = edad
        
    def mostrar_info(self):
        print(
            f'=====================\n' +
            f'Informacion del gato\n' +
            f'=====================\n\n' +
            f'Raza : {self.raza}\n' +
            f'Sexo : {self.sexo}\n' +
            f'Edad : {self.edad}\n' +
            f'Peso : {self.peso}\n' +
            f'=====================\n\n'
        )
    
    def sonido(self):
        print('El perro hace : "Miau!!"')
        
class Pajaro:
    def __init__(self, raza, sexo, edad):
        self.peso = int(input('Ingrese el peso : '))
        self.raza = raza
        self.sexo = sexo
        self.edad = edad
        
    def mostrar_info(self):
        print(
            f'=====================\n' +
            f'Informacion del perro\n' +
            f'=====================\n\n' +
            f'Raza : {self.raza}\n' +
            f'Sexo : {self.sexo}\n' +
            f'Edad : {self.edad}\n' +
            f'Peso : {self.peso}\n' +
            f'=====================\n\n'
        )
        
    def sonido(self):
        print('El perro hace : "Kiruuuu!!"')
        

def mostar_sonido(animal):
    animal.sonido()
    
objectPerro = Perro('Hotdog', 'M', 15)
objectGatp = Gato('Blanca', 'F', 10)
objectPajaro = Pajaro('Loro', 'M', 4)

mostar_sonido(objectPerro)
mostar_sonido(objectGatp)
mostar_sonido(objectPajaro)