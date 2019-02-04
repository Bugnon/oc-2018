"""
Connect 4
The goal is to place 4 discs in a row
"""


from sense_hat import SenseHat
#from sense_emu import SenseHat
from time import sleep, time
from gamelib import *

sense = SenseHat()
sense.set_rotation(180)

repeat=1
playerScore=[0,0]
turns=0
gameOver=0
stopGame=0

fourYellow=[[248, 252, 0]]*4
fourRed=[[248, 0, 0]]*4

state =[[0] * 8] * 7 #Créé le tableau d'affichage 8*8 empli de cases vides

#Définit les différentes couleurs
colors=(BLUE, RED, YELLOW)

def main(): 
    global turns
    turns=0
    global gameOver
    global playerScore
    if (playerScore[0]==2 or playerScore[1]==2 or stopGame==1) and repeat==0:
        return
    else:
        gameOver=0
        if playerScore[0]!=0 or playerScore[1]!=0:
            playerScore=[0,0]
        show(state)
        turn()

def show(state):
    """Met en place le terrain : 6*7 cases bleues."""
    sense.clear()
    for y in range (6):
        for x in range(7):
            s = state [y][x]
            sense.set_pixel(x, 7-y, colors[s])

def turn():
    global turns
    if gameOver==0:
        if turns%2==0 and turns!=42:
            turns+=1
            select_column(1) #Lance le tour du joueur p1
        elif turns%2==1 and turns!=42:
            turns+=1
            select_column(2) #Lance le tour du joueur p2
        elif turns==42:
            player_scored(0)
            
def player_scored(p):
    global gameOver
    gameOver=1
    global playerScore
    if p != 0:
        playerScore[p-1]+=1
        sense.show_letter(str(playerScore[p-1]),colors[p])
    if playerScore[0]==2 or playerScore[1]==2:
        sleep(1.5)
        sense.clear(colors[p])
    sleep(1.5)
    sense.clear()
    main()
        
def select_column(p): #Sélection de la colonne ou laisser tomber le jeton
    x = 3
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
                elif event.direction == 'up': #Déplace le curseur à droite
                    global stopGame
                    stopGame=1
                    player_scored(0)
        show_selection(x,p)
    return x #Renvoie la sélection de colonne x

def show_selection(x,p):
    for i in range(7): #Affiche le curseur au bon endroit
        if i ==x and gameOver==0:
            sense.set_pixel(i, 0, colors[p]) #Colorie le pixel de la bonne couleur            
        elif gameOver==0:    
            sense.set_pixel(i, 0, (0, 0, 0)) #Rend les pixels noirs après le passage du curseur

def put_down(x,p):
    """Fait tomber le pixel du joueur p dans la colonne x"""
    if sense.get_pixel(x,2)==[0,0,248]: #Regarde si la colonne est bien vide (donc bleue) au dernier niveau
        for y in range(7): #Trouve la position du dernier pixel libre
            if sense.get_pixel(x,7-y)==[0,0,248]: #Si le pixel est libre, alors
                animate_down(x,y,p)
                sense.set_pixel(x, 7-y, colors[p])
                if check_connectfour(x,7-y)==False: #Regarde si le tour est gagnant
                    turn() #Si non, lance le tour d'après
                    return
                return
    else:
        select_column(p) #Relance la sélection pour le joueur
    return

def animate_down(x,y,p):
    for z in range(7-y):
        sense.set_pixel(x, z, colors[p])
        sleep(0.03)
        if z != 1 and z != 0:
            sense.set_pixel(x, z, colors[0])
        else:
            sleep(0.03)
            sense.set_pixel(x, 1, [0,0,0])

def check_connectfour(x,y):#Fonction de détection des puissance4
    if check_horizontal(x,y)==False and check_vertical(x,y)==False:
        if check_diagonal_downleft_upright(x,y)==False:
            if check_diagonal_downright_upleft(x,y)==False:
                return(False)

def check_horizontal(x,y):
    horizontal=sense.get_pixels()[8*y:8*y+7]
    for z in range(4):
        if horizontal[z:z+4]==fourYellow:
            player_scored(2)
            return True
        if horizontal[z:z+4]==fourRed:
            player_scored(1)
            return True
    return False

def check_vertical(x,y):
    vertical=[sense.get_pixel(x,2),sense.get_pixel(x,3),sense.get_pixel(x,4),
           sense.get_pixel(x,5),sense.get_pixel(x,6),sense.get_pixel(x,7)]
    for z in range(3):
        if vertical[z:z+4]==fourYellow:
            player_scored(2)
            return True
        if vertical[z:z+4]==fourRed:
            player_scored(1)
            return True
    return False

def check_diagonal_downleft_upright(x,y):
    diagonal=[]
    create_diagonal_downleft_upright(diagonal,x,y)
    for z in range(4):
        if diagonal[z:z+4]==fourYellow:
            player_scored(2)
            return True
        if diagonal[z:z+4]==fourRed:
            player_scored(1)
            return True
    return False

def create_diagonal_downleft_upright(diagonal,x,y):
    for z in range(7):
        try: diagonal.append(sense.get_pixel(x-z+3,y+z-3))
        except: ValueError
    return(diagonal)

def check_diagonal_downright_upleft(x,y):
    diagonal=[]
    create_diagonal_downright_upleft(diagonal,x,y)
    for z in range(4):
        if diagonal[z:z+4]==fourYellow:
            player_scored(2)
            return True
        if diagonal[z:z+4]==fourRed:
            player_scored(1)
            return True
    return False
        
def create_diagonal_downright_upleft(diagonal,x,y):
    for z in range(7):
        try: diagonal.append(sense.get_pixel(x-z+3,y-z+3))
        except: ValueError
    return(diagonal)

# Execute the main() function when the file is executed,
# but do not execute when the module is imported as a module.
print('module name =', __name__)

if __name__ == '__main__':
    main()
    global repeat
    repeat=1
else:
    global repeat
    repeat=0