#Tabatha Gáytan - A00827656
#Fecha - 7 de mayo 2021
#Reflexión - Aprendí a realizar un memorama utilizando turtle, asimismo comprender línea por línea de código.
#Problemas - Tuve complicaciones para poder poder mostrar la cantidad de clicks que se realiza durante el juego.
#Solución - Con ayuda de la maestra al igual que ir línea por línea para encontrar el error.

from random import *
from turtle import *
from freegames import path

car = path('carcopy.gif')

#MEMORAMA DE LIBROS FAVORITOS

tiles = ['Red Queen','Throne of Glass','Cruel Prince','Shadow and Bone','Six of Crows',
         'Furthermore','Aurora Burning','From Blood and Ash', 'Wicked Saints', 'Skyhunter',
         'Crescent City', 'Crave','Furyborn','Vicious','Truthwitch',
         'Graceling','Illuminae','Uprooted','Percy Jackson','Caraval',
         'Circe','Cinder','Renegades','Nevernight','Shatter Me',
         'Queen of Shadows','ACOTAR','Heroes of Olympus','The Deal','The Score',
         'The Mistake','King of Scars']
tiles = tiles * 2

#contador de clicks
taps = 0

state = {'mark': None}
hide = [True] * 64

#parte de atras del memorama
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'darkviolet')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

#para saber donde se hizo el click
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

#fucnión callback cuando das click sobre la ventana
def tap(x, y):
    global mark, taps
    #imprime donde las coorenadas dan click
    print(x,y)
    taps = taps + 1
    
    "Update mark and hidden tiles based on tap."
    #retorna el índice correspondiente a (x,y) en tiles[spot]
    spot = index(x, y)
    #saca el valor de state
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        #el estado ahora cambia a la carta donde el usuario dio click
        state['mark'] = spot
    else:
        #quiere decir que son pares - los hace visibles
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    #limpia la ventana
    clear()
    #mueve el turtle al (0,0)
    goto(0, 0)
    #carga la imagen del carro
    shape(car)
    #dibuja el carro
    stamp()

    #dibuja las 64 cartas del memorama
    contador = 0
    for count in range(64):
        #True si todavía no estan descubierta
        if hide[count]:
            #calcula su esquina inferior izquierda donde se dibujará el square
            x, y = xy(count)
            #dibja el square
            square(x, y)
            contador = contador + 1

    mark = state['mark']
    #despliega la carta donde se dio click
    if mark is not None and hide[mark]:
        #calcula la posición (x,y) de la carta
        x, y = xy(mark)#levanta lápiz
        up()
        goto(x + 2, y + 18)
        #cambia el color de lápiz a blanco
        color('white')
        #despliega el número de la carta oculta
        write(tiles[mark], font=('Arial', 15, 'bold'))

    escondidas = hide.count(True)
    print("Sin encontrar hide.count(True) = ", escondidas)
    if escondidas == 0:
        up()
        goto(-145,120)
        color('white')
        write('GANASTE UN AUTO',font = ('Arial',30,'bold'))
        goto(-100,90)
        color('white')
        write('FELICIDIADES!',font = ('Arial',30,'bold'))
        goto(-60,60)
        color('white')
        write(f'Hiciste {taps} taps',font = ('Arial',18,'bold'))
        return
    #muestra en la ventana lo dibujado
    update()
    ontimer(draw, 100)

#revolver las cartas
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
#detectar eventos del mouse
onscreenclick(tap)
draw()
done()