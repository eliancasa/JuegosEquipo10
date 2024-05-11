from random import shuffle
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
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
    global num_taps  # Acceso a la variable num_taps globalmente
    num_taps += 1  # Incrementa el contador de taps
    
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
        goto(x + 22, y + 15)  # Ajuste la posición de escritura para centrar el número en el cuadro
        color('black')
        write(tiles[mark], align="center", font=('Arial', 20, 'normal'))

    # Mostrar el número de taps en la ventana
    up()
    goto(-180, 180)
    color('black')
    write(f"Taps: {num_taps}", font=('Arial', 16, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()