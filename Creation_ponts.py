import turtle

sir = turtle.Turtle()
sir.speed(6)
sir.shape("turtle")

def grille_pont_triangulaire(x):
   for i in range(3):
        if i==0:
          sir.left(45)
          sir.forward(70)
          sir.back(70)
        else:
          sir.left(90)
          sir.forward(70)
          sir.back(70)
          x+=112
        sir.goto(x+56, 190)
        x+=56
        sir.goto(x+56, 0)
        x+=56
        sir.goto(x+56, 215)
        x+=56
        sir.goto(x+56, 0)
        x+=56
        sir.goto(x+56, 190)
        x+=56
        sir.goto(x+56, 0)
        x+=56
        sir.left(270)
        sir.forward(70)
        sir.back(70)
        if i<2:
            sir.goto(x+112,0)
        else:
            sir.goto(0,0)

def grille_pont_rectangulaire(y):
   for i in range(3):
        sir.goto(y-56, 0)
        sir.right(360)
        sir.forward(145)
        sir.back(145)
        y-=56
        sir.goto(y-56,0)
        sir.forward(190)
        sir.back(190)
        y-=56
        sir.goto(y-56,0)
        sir.forward(215)
        sir.back(215)
        y-=56
        sir.goto(y-56,0)
        sir.forward(225)
        sir.back(225)
        y-=56
        sir.goto(y-56,0)
        sir.forward(215)
        sir.back(215)
        y-=56
        sir.goto(y-56,0)
        sir.forward(190)
        sir.back(190)
        y-=56
        sir.goto(y-56,0)
        sir.forward(145)
        sir.back(145)
        y-=112
        if i < 2:
            sir.goto(y-56,0)


def pied_pont(z):
        sir.fillcolor("#0E4BEF")
        sir.begin_fill()
        sir.goto(z-56,0)
        sir.left(-180)
        sir.forward(25)
        sir.right(90)
        sir.forward(40)
        sir.left(90)
        sir.forward(25)
        sir.left(90)
        sir.forward(192)
        sir.left(90)
        sir.forward(25)
        sir.left(90)
        sir.forward(40)
        sir.right(90)
        sir.forward(25)
        sir.end_fill()
        sir.goto(z,0)

def demi_cercle():
        sir.circle(224,-180)


def creation_pont():

        sir.width(4)
        sir.color("#0E4BEF")
        sir.penup()
        sir.goto(-616,0)
        sir.pendown()
        sir.goto(-672,0)
        sir.right(90)
        demi_cercle()
        pied_pont(-224)
        sir.right(180)
        demi_cercle()
        pied_pont(224)
        sir.right(180)
        demi_cercle()
        grille_pont_rectangulaire(672)
        grille_pont_triangulaire(-616)

creation_pont()

turtle.done()