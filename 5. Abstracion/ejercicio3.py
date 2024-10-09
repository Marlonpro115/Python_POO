# Ejercicio 3: Crea una clase abstracta TareaEmpleado con un método abstracto realizar_tarea(). 
# Implementa las clases Ingeniero y Doctor que heredan de TareaEmpleado e implementan el método realizar_tarea() de manera específica según su especialidad.

from abc import ABC, abstractmethod

class TareaEmpleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass
    
class Ingeniero(TareaEmpleado):
    def __init__(self, horas, accion):
        self.horas = horas
        self.accion = accion
        
    def realizar_tarea(self):
        print(
            f'El Ingeniero a realizado su trabajo correctamente!!!\n\n' +
            f'Horas de trabajo : {self.horas}\n' +
            f'Accion realizada : {self.accion}\n\n'
        )
        
class Doctor(TareaEmpleado):
    def __init__(self, horas , accion):
        self.horas = horas
        self.accion = accion
        
    def realizar_tarea(self):
        print(
            f'El Doctor a realizado su trabajo correctamente!!!\n\n' +
            f'Horas de trabajo : {self.horas}\n' +
            f'Accion realizada : {self.accion}\n\n'
        )

ingeniero = Ingeniero(12, 'Supervisar')
doctor = Doctor(45, 'Operar')

ingeniero.realizar_tarea()
doctor.realizar_tarea()