import turtle
from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):

    # Calcular el centro del círculo (punto medio)
    centro_x = (start[0] + end[0]) / 2
    centro_y = (start[1] + end[1]) / 2

    #Calcular el radio del circulo
    radio = ((end[0] - start[0])**2 + (end[1] - start[1])**2)**0.5 / 2
    goto(centro_x, centro_y-radio)  # Mover el cursos al punto inicial para trazar ahí círculo
    pendown() 
    color("blue")#Elegir color del círculo
    turtle.circle(radio)  # Dibujar el círculo con el radio dado con la función círculo de turtle, dando el radio como unico argumento
    penup()


    pass  # TODO

def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    ladoa = end[1]-start[1]
    ladob = end[0]-start[0]
    for i in range(2):
        forward(ladob)
        left(90)
        forward(ladoa)
        left(90)




def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    ladoa = end[0]-start[0]
    for i in range(3):
        forward(ladoa)
        left(120)


def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}

setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('pink'), 'P') #El color rosa se agrega por medio de la tecla P y la función lambda color 
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()