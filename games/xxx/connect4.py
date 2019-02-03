"""
Connect 4
The goal is to place 4 discs in a row
"""


from sense_hat import SenseHat
#from sense_emu import SenseHat
from time import sleep, time
from gamelib import *

sense = SenseHat()
##sense.set_rotation(180)

state =[[0] * 8] * 7 #Créé le tableau d'affichage 8*8 empli de cases vides

#Définit les différentes couleurs
colors=(BLUE, RED, YELLOW)

def show(state):
    """Met en place le terrain : 6*7 cases bleues."""
    sense.clear()
    for y in range (6):
        for x in range(7):
            s = state [y][x]
            sense.set_pixel(x, 7-y, colors[s])
        
def cursor(p): #Sélection de la colonne ou laisser tomber le jeton
    x = 0
    selection = True #Tour en cours?
    while selection:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'right': #Déplace le curseur à droite
                    x =(x + 1) % 7
                elif event.direction == 'left': #Déplace le curseur à gauche
                    x =(x - 1) % 7
                elif event.direction =='down': #Confirme la sélection
                    selection = False #Termine le tour
                    put_down(x,p) #Appelle la fonction qui fait tomber le jeton
        for i in range(7): #Affiche le curseur au bon endroit
            if i ==x:
                sense.set_pixel(i, 0, colors[p]) #Colorie le pixel de la bonne couleur            
            else:    
                sense.set_pixel(i, 0, (0, 0, 0)) #Rend les pixels noirs après le passage du curseur
    return x #Renvoie la sélection de colonne x                         

def put_down(x,p):
    """Fait tomber le pixel"""
    if sense.get_pixel(x,2)==[0,0,248]: #Regarde si la colonne est bien vide (donc bleue) au dernier niveau
        for y in range(7): #Trouve la position du dernier pixel libre
            print('y =', y)
            print(sense.get_pixel(x,7-y))
            if sense.get_pixel(x,7-y)==[0,0,248]: #Si le pixel est libre, alors
                print('Pixel Libre')
                for z in range(7-y):
                    sense.set_pixel(x, z, colors[p])
                    sleep(0.03)
                    if z != 1 and z != 0:
                        sense.set_pixel(x, z, colors[0])
                    else:
                        sleep(0.01)
                        sense.set_pixel(x, 1, [0,0,0])
                    print('z', z)
                sense.set_pixel(x, 7-y, colors[p])
                checkConnect(x,7-y)
                return
    else:
        cursor(p) #Relance la sélection pour le joueur
    return

def checkConnect(x,y):#Fonction de détection des puissance4
    print(x,y)
    print(sense.get_pixel(x,y))
    print('State :', sense.get_pixels())
    #if sense.get_pixel(x,y)==[248, 0, 0]: #Regarde si le pixel gagnant est rouge
        #score(1)
    #elif sense.get_pixel(x,y)==[248, 252, 0]: #Regarde si le pixel gagnant est rouge
        #score(2)
    return

def inGame(): #Fonction qui lance les tours
    x = 0 #0==p1 0==p2
    show(state)
    for i in range(42): #Nombre max de tour : 42 (Nombre de cases)
        if x==0:
            cursor(1) #Lance le tour du joueur p1
            x=1
        elif x==1:
            cursor(2) #Lance le tour du joueur p2
            x=0

def main():
    inGame()

# Execute the main() function when the file is executed,
# but do not execute when the module is imported as a module.
print('module name =', __name__)

if __name__ == '__main__':
    main()  