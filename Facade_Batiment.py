from turtle import *
def rectangle(x,y,nL,nl,):
   up()
   goto(x,y)
   down()
   for i in range(2):
     fd(nL)
     rt(90)
     fd(nl)
     rt(90)
  
def trait(x,y,nl,nL):
    up()
    goto(x,y)
    down()
    rt(nl)
    fd(nL)
def cercle(x,y,n):
   lt(90)
   up()
   goto(x,y)
   down()
   begin_fill()
   fillcolor('#2F4F4F')
   circle(n)
   end_fill()
def demiCercle(x,y,n):
    lt(90)
    up()
    goto(x,y)
    down()
    circle(n,180)
   
def fenetre1b(x,y,nL,nl):
    begin_fill()
    fillcolor('#FFFFFF')
    rectangle(x,y,nL,nl)
    end_fill()
    trait(x+(nL/2),y,90,nl)
    lt(90)
def fenetre2b(x,y,nL,nl):
    begin_fill()
    fillcolor('#FFFFFF')
    rectangle(x,y,nL,nl)
    end_fill()
    trait(x,y-(nl/2),360,nL)
    trait(x+(nL/2),y,90,nl)
    lt(90)
def doubleFenetres(x,y,nL,nl):
    fenetre2b(x,y,nL,nl)
    fenetre2b(x,y-170,nL,2*nl)
def escalier(x,y,nL,nl):
    for i in range (5):
       rectangle(x,y,nL,nl)
       x-=10
       y-=15
       nL+=20
def tripleElevation(x,y,nL,nl):
    for i in range(3):
       begin_fill()
       fillcolor('#D3D3D3')
       rectangle(x,y,nL,nl)
       end_fill()
       x-=125
    
def entree(x,y,nL,nl):
   rectangle(x,y,nL,nl)
   begin_fill()
   fillcolor('#C0C0C0')
   rectangle(x+8,y,nL-15,nl)
   end_fill()
   rectangle(-75,230,250,40)
  
def triangle(x,y,n):
  up()
  goto(x,y)
  down()
  begin_fill()
  fillcolor('#8FBC8F')
  lt(25)
  fd(n)
  rt(50)
  fd(n)
  end_fill()
def trapezeToiture1(x,y,nL,nl):
   up()
   goto(x,y)
   down()
   begin_fill()
   fillcolor('#F5F5F5')
   lt(145)
   fd(nl)
   rt(145)
   fd(nL)
   rt(145)
   fd(nl)
   end_fill()
def trapezeToiture2(x,y,nL,nl):
   up()
   goto(x,y)
   down()
   begin_fill()
   fillcolor('#8FBC8F')
   lt(147)
   fd(nl)
   rt(147)
   fd(nL)
   rt(147)
   fd(nl)
   end_fill()

   
def menuiserieElevationD(x,y,nL,nl):
   for i in range(3):
      doubleFenetres(x,y,nL,nl)
      x-=124
def menuiserieElevationG(x,y,nL,nl):
   for i in range(3):
      doubleFenetres(x,y,nL,nl)
      x+=124
def menuiserieToit(x,y,nL,nl):
   for i in range(3):
      fenetre1b(x,y,nL,nl)
      x+=55

   
def fondation():
   begin_fill()
   fillcolor('#F5F5F5')
   rectangle(-450,200,1000,430)
   end_fill()
   trait(-450,-220,360,1000)
   


def elevation():
   tripleElevation(425,190,115,390)
   tripleElevation(-190,190,115,390)
   begin_fill()
   fillcolor('#FFFFFF')
   rectangle(-50,190,205,376)
   end_fill()
   entree(-42,190,190,300)
   

def toiture():
   trapezeToiture1(-450,200,1080,50)
   lt(290)
   rt(55)
   rectangle(-315,230,50,725)
   rectangle(-315,230,50,180)
   rectangle(-135,230,50,360)
   rt(90)
   triangle(-315,280,100)
   lt(25)
   triangle(225,280,100)
   lt(25)
   trapezeToiture2(-157,280,530,77)
   lt(288)
   rt(53)
   rt(88)
   begin_fill()
   fillcolor('#FFFFFF')
   rectangle(-75,230,250,40)
   end_fill()

def menuiserie():
   menuiserieElevationG(-432,180,98,100)
   menuiserieElevationD(432,180,98,100)
   fenetre2b(25,10,55,120)
   fenetre1b(25,150,55,55)
   lt(90)
   menuiserieToit(-300,230,40,25)
   fenetre1b(-100,230,40,28)
   fenetre1b(0,230,40,28)
   fenetre1b(36,230,40,28)
   fenetre1b(72,230,40,28)
   fenetre1b(170,230,40,28)
   menuiserieToit(243,230,40,25)



def finition():
   escalier(25,-110,55,15)
   demiCercle(80,10,28)
   lt(90)
   cercle(66,65,14)
   
   


   

def batiment():
   fondation()
   elevation() 
   toiture()
   menuiserie()
   rt(90)
   finition()


speed(0)
batiment()

 
