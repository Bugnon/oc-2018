import random
import time
from mcpi import minecraft
mc = minecraft.Minecraft.create()

###Creates the Board###
mc.postToChat("Welcome to Minecraft MineSweeper")
x, y, z = mc.player.getPos()
mc.setBlocks(x, y-1, z, x+20, y-1, z+20, 58)

global mine
mine = random.randrange(0, 11, 1)
print(mine)

###Places the mine###
mine_x = int(x+mine)
mine_y = int(y-1)
mine_z = int(z+mine)

print (mine_x), (mine_y), (mine_z)###test
mc.setBlock(mine_x, mine_y, mine_z,58)

score = 0

mc.postToChat("Score is "+str(score))
#test = mc.setBlock(x + mine, y-1, z + mine, 46,1)
time.sleep(10)
while True:  ###TEST IF YOU STAND ON THE BLOCK
    
    x1, y1, z1 = mc.player.getTilePos()
    #print x1, y1, z1 ###test
    time.sleep(0.1)
    
    if (x1, y1-1, z1) == (mine_x, mine_y, mine_z):
        mc.setBlocks(x-5, y+1, z-5, x+5, y+2, z+5, 10) ##CHANGE TO WATER?
        print ("GAME OVER")
        mc.postToChat("G A M E  O V E R")
        mc.postToChat("Score is "+str(score))
        break
    else:
        score = score + 1
        mc.setBlock(x1, y1-1, z1, 41)
        
mc.postToChat("GAME OVER") 