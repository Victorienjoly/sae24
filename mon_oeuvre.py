import pygame
from random import *
import math
import sys

#Récupération des variables depuis le site
colonnes=int(sys.argv[1])
lignes=int(sys.argv[2])

#Fonction dessinant un rectangle
def rectangle(x,y,angle):    
    x1=32.5
    y1=10
    x2=-32.5
    y2=10
    x3=-32.5
    y3=-10
    x4=32.5
    y4=-10
    x1p=math.cos(angle)*x1-math.sin(angle)*y1
    y1p=math.sin(angle)*x1+math.cos(angle)*y1
    x2p=math.cos(angle)*x2-math.sin(angle)*y2
    y2p=math.sin(angle)*x2+math.cos(angle)*y2
    x3p=math.cos(angle)*x3-math.sin(angle)*y3
    y3p=math.sin(angle)*x3+math.cos(angle)*y3
    x4p=math.cos(angle)*x4-math.sin(angle)*y4
    y4p=math.sin(angle)*x4+math.cos(angle)*y4
    couleur=(randint(180,211),randint(180,211),randint(180,211))
    pygame.draw.polygon(screen,couleur,((x+x1p,y+y1p),(x+x2p,y+y2p),(x+x3p,y+y3p),(x+x4p,y+y4p)))
    pygame.draw.polygon(screen,(0,0,0),((x+x1p,y+y1p),(x+x2p,y+y2p),(x+x3p,y+y3p),(x+x4p,y+y4p)),width=2)


#Initialisation de pygame
pygame.init()
screen = pygame.surface.Surface((532,770))
pygame.draw.rect(screen,(255,255,255),(0,0,532,770))

#Boucles dessinant l'oeuvre
angle=0
y=15
temp_lignes=lignes*0.4
l1=math.ceil(temp_lignes)
print(l1)
l2=lignes-l1
for j in range (l1):
    x=40
    for i in range (colonnes):
        angle=-(randint(0,10)/10)
        rectangle(x, y, angle)

        x=x+50
    y=y+30
   
for j in range (l2):
    x=40
    angle=(j-5)*0.1
    for i in range (colonnes):
        rectangle(x, y, angle)

        x=x+50
    y=y+30
 
fichier='mon_oeuvre.png'
pygame.image.save(screen,fichier)
print("done")