class Empleado:
    def __init__(self, puesto, edad, horas, nombre, genero, tarifa_por_hora=10):
        self.puesto = puesto
        self.edad = edad
        self.horas = horas
        self.nombre = nombre
        self.genero = genero
        self.tarifa_por_hora = tarifa_por_hora

    def ObtenerInfo(self):
        print(
            f'--------------------------------\n' +
            f'Información del empleado:\n' +
            f'Nombre: {self.nombre}\n' +
            f'Edad: {self.edad}\n' +
            f'Puesto: {self.puesto}\n' +
            f'Género: {self.genero}\n' +
            f'Horas trabajadas: {self.horas}\n' +
            f'--------------------------------\n'
        )

    def PagoPorHoras(self):
        salario = self.horas * self.tarifa_por_hora
        print(f'El salario de {self.nombre} es: ${salario}\n')

    def Puesto(self):
        print(f'El puesto de {self.nombre} es: {self.puesto}\n')


empleado1 = Empleado('Médico', 34, 600, 'Juan', 'H')

empleado1.ObtenerInfo()
empleado1.PagoPorHoras()
empleado1.Puesto()