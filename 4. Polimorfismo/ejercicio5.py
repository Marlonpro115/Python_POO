# Ejercicio 5: Clases de Profesiones con Polimorfismo
# Crea tres clases: Médico, Ingeniero, y Docente, cada una con un método trabajar() que describa la información técnica del profesional.

class Medico:
    def __init__(self, cargo, horas, edad):
        self.pacientes = int(input('Ingrese el numero de pacientes : '))
        self.cargo = cargo
        self.horas = horas
        self.edad = edad
        
    def trabajar(self):
        print(
            f'\n\n================================\n' +
            f'Informacion tecnica de un medico\n' +
            f'================================\n' +
            f'Un médico o facultativo1 es un profesional que practica la medicina2​3​ y que intenta mantener y recuperar la salud mediante el estudio, el diagnóstico y el tratamiento de la enfermedad o lesión del paciente. En la lengua española, en forma coloquial, se denomina también doctor a este tipo de profesional, aunque no haya obtenido el grado de doctorado.4​ La persona que ejerce la medicina es un profesional altamente calificado en materia sanitaria. Debido a que tiene que dar respuestas acertadas y rápidas a problemas de salud, mediante decisiones tomadas habitualmente en condiciones de gran incertidumbre, precisa de formación continuada a lo largo de toda su vida laboral.\n\n'
        )
        
class Ingeniero:
    def __init__(self, cargo, horas, edad):
        self.cargo = cargo
        self.horas = horas
        self.edad = edad
        
    def trabajar(self):
        print(
            f'\n\n===================================\n' +
            f'Informacion tecnica de un ingeniero\n' +
            f'===================================\n' +
            f'La información técnica de un ingeniero incluye la capacitación en ciencias físicas básicas como física, química y matemáticas, así como habilidades de resolución de problemas y la capacidad de comunicar resultados a través de informes técnicos. Estos informes son documentos que presentan el planteamiento, desarrollo y resultados de una investigación o práctica de laboratorio.\n\n'
        )
        
class Docente:
    def __init__(self, cargo, horas, edad):
        self.cargo = cargo
        self.horas = horas
        self.edad = edad
        
    def trabajar(self):
        print(
            f'\n\n================================\n' +
            f'Informacion tecnica de un docente\n' +
            f'================================\n' +
            f'La información técnica sobre un docente puede incluir aspectos como las especificaciones de su formación académica, metodologías de enseñanza, y habilidades interpersonales, como la empatía, que son esenciales para facilitar el aprendizaje. Según los datos, la función docente implica un proceso profesional que abarca la enseñanza y el aprendizaje sistemático. Es importante recordar que estos elementos varían según el contexto y la normativa de cada región.\n\n'
        )
     
def mostrar_trabajo(trabajo):
    trabajo.trabajar()
        
objectMedico = Medico('Doctor', 1000, 56)
objectIngeniero = Ingeniero('Supervisor', 4002, 23)
objectDocente = Docente('Maestro', 4000, 70)

mostrar_trabajo(objectMedico)
mostrar_trabajo(objectDocente)
mostrar_trabajo(objectIngeniero)