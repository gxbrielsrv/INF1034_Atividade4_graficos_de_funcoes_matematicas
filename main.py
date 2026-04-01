import random
from time import sleep
from turtle import *
t= Turtle()
t.speed(0)

def raiz_x(x):
    return x**0.5

def sobre_x(x):
    return 1/x

def elevado_x(x):
    return 2**x

def menos_x(x):
    return 5-(x**2)

def quadrado_x(x):
    return (x**2) - (5*x) + 6

def cubo_x(x):
    return x**3 - x**2 - x + 1

def plano():
    t.hideturtle()
    t.setheading(0)
    t.color('black')
    t.pu()
    t.goto(-300,0)
    t.pd()
    t.goto(300,0)
    t.stamp()
    t.pu()
    t.goto(0,-300)
    t.pd()
    t.goto(0,300)
    t.lt(90)
    t.stamp()
    
def corrida(n):
    tartarugas = []
    for i in range(n):
        t= Turtle()
        t.shape("turtle")
        t.pu()
        t.goto(-200, -100 + i*40)
        t.pd()
        tartarugas.append(t)
    for _ in range(100): 
        for t in tartarugas:
            t.pu()
            t.fd(random.randint(1, 10))

def pista():
    t.color('black')
    t.pu()
    t.goto(-500, 250)
    t.pd()
    t.goto(350,250)
    t.color('red')
    t.goto(350,-250)
    t.color('black')
    t.goto(-500,-250)


#funçao 1
plano()
t.color('red')
t.pu()
t.goto(0,raiz_x(0))
t.pd()
for x in range(10,301):
    t.goto(x, raiz_x(x))
sleep(3)
t.clear()

#funçao 2
plano()
t.color('red')
t.pu()
t.goto(-299,sobre_x(10))
t.pd()
for x in range(-299,0):
    t.goto(x, sobre_x(x/50)*10)
t.pu()
t.goto(0, 500)
t.pd()
for x in range(1, 299):
    t.goto(x, sobre_x(x/50)*10)
sleep(3)
t.clear()

#funçao 3
plano()
t.pu()
t.goto(-300, 0)
t.pd()
t.color('red')
for x in range(-300, 10):
    t.goto(x, elevado_x(x))
sleep(3)
t.clear()

#funçao 4
plano()
t.pu()
t.goto(-150, -500)
t.pd()
t.color('red')
for x in range(-149, 149):
    t.goto(x, menos_x(x/15)*20)
sleep(3)
t.clear ()

#funçao 5
plano()
t.pu()
t.goto(-250, 510)
t.pd()
t.color('red')
for x in range(-249, 330):
    t.goto(x, quadrado_x(x/15)*20)
sleep(3)
t.clear()

#funçao 6
plano()
t.pu()
t.goto(-250, -510)
t.pd()
t.color('red')
for x in range(-249, 330):
    t.goto(x, cubo_x(x)/1000)
sleep(3)
t.clear()

#extra(corrida de tartarugas)
pista()
corrida(5)
sleep(3)

mainloop()