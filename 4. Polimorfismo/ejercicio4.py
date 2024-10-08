# Ejercicio 4: Instrumentos Musicales con Polimorfismo
# Crea clases: Guitarra, Piano, y Trompeta, cada una con un método tocar() que describa la información técnica del instrumento.

class Guitarra:
    def __init__(self, tipo, marca, material):
        self.tipo = tipo
        self.marca = marca
        self.material = material
        self.cuerdas = int(input('Ingrese el numero de cuerdas : '))
    
    def tocar(self):
        print(
            f'Informacion de la guitarra\n\n' +
            f'La guitarra es un instrumento musical de cuerda pulsada, compuesto de una caja de madera, un mástil sobre el que va adosado el diapasón o trastero —generalmente con un agujero acústico en el centro de la tapa (boca)—, y seis cuerdas. Sobre el diapasón van incrustados los trastes, que permiten las diferentes notas.\n\n')
        

class Piano:
    def __init__(self, tipo, marca, material):
        self.tipo = tipo
        self.marca = marca
        self.material = material
        self.cuerdas = int(input('Ingrese el numero de cuerdas : '))
    
    def tocar(self):
        print(
            f'Informacion del piano\n\n' +
            'El piano es un instrumento de cuerda pulsada: su interior contiene cuerdas conectadas a unos macillos. Cada tecla mueve un macillo dentro del piano y al presionar las teclas, esos macillos golpean las cuerdas. Cuanto más fuerte se tocan las teclas, más fuerte golpean y por lo tanto, más fuerte será el sonido.\n\n')
        
    
class Trompeta:
    def __init__(self, tipo, marca, material) -> None:
        self.tipo = tipo
        self.marca = marca
        self.material = material
        self.cuerdad = int(input('Ingrese el numero de cuerdas : '))
        
    def tocar(self):
        print(
            f'Informacion de la trompeta\n\n' +
            'La trompeta es un instrumento musical de viento, que pertenece a la familia de los instrumentos de viento metal, fabricado en aleación de metal. El sonido se produce gracias a la vibración de los labios del intérprete en la parte denominada boquilla a partir de la columna del aire (flujo del aire). Comúnmente, suele estar afinada en si ♭ (bemol), es decir, un tono por debajo de la afinación escrita en el pentagrama, aunque también hay trompetas afinadas en fa, en do, en la y en mi, - bemol -.Al músico que toca la trompeta se le conoce como trompetista o trompeta.\n\n')

def mostarComoSeToca(intrumento):
    intrumento.tocar()
  
objectGuitarra = Guitarra('Bajo', 'M-523', 'Metalico')
objectPiano = Piano('Elegante', 'k-14141', 'Madera')
objectTrométa = Trompeta('Florcorica', 'Yin-1', 'Metalico')

print('\n\n')
mostarComoSeToca(objectGuitarra)
mostarComoSeToca(objectPiano)
mostarComoSeToca(objectTrométa)