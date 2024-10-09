# Ejercicio 2: Crea una clase abstracta Empleado con un método abstracto calcular_salario(). 
# Luego, crea dos clases concretas EmpleadoTiempoCompleto y EmpleadoPorHoras que implementen calcular_salario() de manera distinta.

from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass
    
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, horas):
        self.horas = horas
        
    def calcular_salario(self):
        return 24 * 1000 + 3
    
class EmpleadoPorHoras(Empleado):
    def __init__(self, horas):
        self.horas = horas
        
    def calcular_salario(self):
        return self.horas * 100
    
empleadoTiempoCompleto = EmpleadoTiempoCompleto(24)
empleadoPorHoras = EmpleadoPorHoras(100)

print(
    f'El empleado a tiempo gano por su trabjo un total de : {empleadoTiempoCompleto.calcular_salario()}\n\n' +
    f'El empleado por sus horas de trabajo gano un total de : {empleadoPorHoras.calcular_salario()}'
)