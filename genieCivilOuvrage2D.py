from turtle import *

def carre(x,y,n,couleur):
   """Fonction pour dessiner un carre
     (x,y)sont les coordonées du coin superieur gauche, n est la longueur du trait
     Sorties : carre
     connues : -
     Methodes : boucle"""
   up()
   goto(x,y)
   down()
   color(couleur)
   for i in range (4):
      fd(n)
      lt(90)



def rectangle(x,y,nL,nl):
    """Fonction pour dessiner un rectangle
       (x,y)sont les coordonées du coin superieur gauche,nL est la longueur du longueur et nl celle de la largeure
        sorties : rectangle
        connues : -
        methodes : boucle"""
   up()
   goto(x,y)
   down()
   for i in range(2):
     fd(nL)
     lt(90)
     fd(nl)
     lt(90)


def triangle (x,y,n):
    """Fonction pour dessiner un triangle
    (x,y)sont les coordonées du coin superieur gauche, n est la longueur du trait
    Sorties : rectangle
    connues : -
    Methodes : boucle"""
  up()
  goto(x,y)
  down()
  for i in range(3):
    fd(n)
    lt(120)
    fd(n)


def polygone(x,y,n,c):
  """Fonction pour dessiner un polygone
     (x,y)sont les coordonées du coin superieur gauche
     n est la taille d'un coté
     c est le nombre de cotés.
     sorties : polygone
     methodes :boucle et affectation"""
  up()
  goto(x,y)
  down()
  angle=360/c
  for i in range(c):
    fd(n)
    rt(angle)


def cercle(x,y,n):
   """Fonction pour dessiner un cercle
     (x,y)sont les coordonées du coin superieur gauche, n est le rayon du cercle
     Sorties : cercle
     Methodes : """
   lt(90)
   up()
   goto(x,y)
   down()
   circle(n)
   

def demiCercle(x,y,n):
  """Fonction pour dessiner un demi cercle
  (x,y)sont les coordonées du coin superieur gauche, n est le rayon du demi cercle."""
    lt(90)
    up()
    goto(x,y)
    down()
    circle(n,180)

def losange(x,y,n):
    """Fonction pour dessiner un losange
      (x,y)sont les coordonées du coin superieur gauche, n est la longueur d'un coté."""
    lt(90)
    up()
    goto(x,y)
    down()
    circle(n,steps=4)


def trapezeToiture1(x,y,nL,nl):
  """Fonction pour dessiner un trapeze,
     (x,y) sont les coordonées du coin inferieur gauche
      nL est la longueur de la base 
      nl est la longueur de la base superieur."""
   up()
   goto(x,y)
   down()
   lt(145)
   fd(nl)
   rt(145)
   fd(nL)
   rt(145)
   fd(nl)


def elip(x,y,n):
    """Fonction pour dessiner une ellipse
   (x,y)sont les coordonées du coin superieur gauche, n est le rayon d'une ellipse."""
    up()
    goto(x,y)
    down()
    for i in range (2):
        circle(n,90)
        circle(n//2,90)



 
 