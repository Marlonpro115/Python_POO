import math

class FigurasGeometricas:
    def __init__(self, nombre, lados, radio=None, area=None, forma="desconocida"):
        self.nombre = nombre
        self.lados = lados
        self.radio = radio
        self.area = area
        self.forma = forma

    def obtenerArea(self):
        if self.nombre.lower() == "círculo" and self.radio:
            self.area = math.pi * (self.radio ** 2)
        elif self.lados == 4 and self.forma.lower() == "cuadrado":
            self.area = self.radio ** 2
        else:
            print("No se puede calcular el área para esta figura sin más información.")
        return self.area

    def ObtenerDatos(self):
        print(
            f'--------------------------------\n' +
            f'Información de la figura geométrica:\n' +
            f'Nombre: {self.nombre}\n' +
            
            f'Lados: {self.lados}\n' +
            f'Radio: {self.radio if self.radio else "No aplica"}\n' +
            f'Área: {self.area if self.area else "No calculada"}\n' +
            f'Forma: {self.forma}\n' +
            f'--------------------------------\n'
        )

    def ObtenerRadio(self):
        if self.radio:
            print(f'El radio de la figura es: {self.radio}')
        else:
            print('Esta figura no tiene radio.')

figura1 = FigurasGeometricas("Círculo", 0, radio=7)
figura1.ObtenerDatos()
print(f"Área calculada: {figura1.obtenerArea()}")

figura2 = FigurasGeometricas("Cuadrado", 4, radio=5, forma="Cuadrado")
figura2.ObtenerDatos()
print(f"Área calculada: {figura2.obtenerArea()}")