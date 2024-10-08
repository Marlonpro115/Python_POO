class Personas:
    def __init__(self, nombres, apellidos, identidad, fechaDeNacimiento, sexo):
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__identidad = identidad
        self.fechaDeNacimiento = fechaDeNacimiento
        self.sexo = sexo

    def nombres(self):
        return self.__nombres

    def apellidos_(self):
        return self.__apellidos

    def identidad(self):
        return self.__identidad

    def setName(self, newName):
        self.__nombres = newName
 
    def setApellidos(self, newApellido):
        self.__apellidos = newApellido

    def detalles(self):
        print(
            f'\n----------------------\n' +
            f'Detalles de la persona\n' +
            f'----------------------\n\n' +
            f'Nombres : {self.__nombres}\n' +
            f'Apellidos : {self.__apellidos}\n' +
            f'N° de identidad : {self.__identidad}\n' +
            f'Fecha de nacimiento : {self.fechaDeNacimiento}\n' +
            f'Sexo : {self.sexo}\n\n'
        )

persona = Personas('Jorge', 'Rojas', 141425326262, '14/09/1987', 'M')

persona.detalles()

print('---------------------------------------\n\n')

persona.setName('Carlos')
print(f'Nombres : { persona.nombres() }\n')
persona.setApellidos('Perez')
print(
    f'Apellidos : { persona.apellidos_() }\n' +
    f'N° de idnetidad : { persona.identidad() }\n' +
    f'Fecha de nacimiento : {persona.fechaDeNacimiento}\n' +
    f'Sexo : {persona.sexo}\n'
)