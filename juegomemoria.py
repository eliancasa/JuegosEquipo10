from random import shuffle  # Importa la función shuffle para barajar los emojis
from turtle import *  # Importa todas las funciones y objetos de Turtle para dibujar y controlar la ventana gráfica
from freegames import path  # Importa la función path para obtener la ruta del archivo de imagen del carro

# Ruta del archivo de imagen del carro
car = path('car.gif')

# Lista de emojis que se utilizarán en el juego
emojis = ['😀', '😎', '😜', '😇', '🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼', '🐨', '🐯', '🦁', '🐮']

# Lista que contiene los emojis duplicados 4 veces, totalizando 16 emojis
tiles = emojis * 4

# Diccionario que almacena el estado del juego, incluyendo la posición marcada actualmente
state = {'mark': None}

# Lista que indica si los cuadros están ocultos o no
hide = [True] * 64

# Variable para contar los taps
num_taps = 0

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global num_taps
    num_taps += 1
    
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        
    # Verificar si todos los cuadros están destapados
    if all_revealed():
        up()
        goto(-100, 0)
        color('white')
        write("¡Todos los cuadros están destapados!", font=('Arial', 20, 'normal'))

def all_revealed():
    """Check if all tiles are revealed."""
    return all(not h for h in hide)

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 22, y + 15)  # Ajustar la posición de escritura para centrar el emoji en el cuadro
        color('black')
        write(tiles[mark], align="center", font=('Arial', 20, 'normal'))

    # Mostrar el número de taps en la ventana
    up()
    goto(-180, 180)
    color('black')
    write(f"Taps: {num_taps}", font=('Arial', 16, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)  # Baraja los emojis
setup(420, 420, 370, 0)  # Configura la ventana con un tamaño de 420x420 y un fondo blanco
addshape(car)  # Agrega la forma del carro
hideturtle()  # Oculta el cursor de la tortuga
tracer(False)  # Desactiva el trazado de animación
onscreenclick(tap)  # Asigna la función tap al evento de clic del mouse
draw()  # Inicia el juego
done()  # Mantiene la ventana abierta