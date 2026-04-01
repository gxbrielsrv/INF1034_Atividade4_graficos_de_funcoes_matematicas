from turtle import *
t= Turtle()




def raiz_x(x):
    return x**0.5

def sobre_x(x):
    return 1/x

def elevado_x(x):
    return 2**x




t.speed(5)


#Plano Cartesiano
def plano():
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

#funçao 1
# plano()
# t.color('red')
# t.pu()
# t.goto(0,raiz_x(0))
# t.pd()

# for x in range(10,301):
#     t.goto(x, raiz_x(x))
# t.clear()

#funçao 2
# plano()
# t.color('red')
# t.pu()
# t.goto(-299,sobre_x(10))
# t.pd()

# for x in range(-299,0):
#     t.goto(x, sobre_x(x/50)*10)

# t.pu()
# t.goto(0, 300)
# t.pd()

# for x in range(1, 299):
#     t.goto(x, sobre_x(x/50)*10)
# t.clear()

#funçao 3

plano()
t.pu()
t.goto(-300, 0)
t.pd()

t.color('red')
for x in range(-300, 100):
    t.goto(x, elevado_x(x))







mainloop()