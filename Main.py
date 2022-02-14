###################################################################
#                                                                 #
#            Plan simulation of sand grain stacking               #
#                  -----------------------------                  #
#              -------------------------------------              #
#                 -------------------------------                 #
#                                                                 #
###################################################################

import random as rd

from Utilitary import *
from Class import *
from Math import *
import time
import pygame
pygame.init()
screen = pygame.display.set_mode((1280,720))

# repere
#        y
#        ^
#        |
#        +----> x





box = (.10,.10) # the box that contain sand is 10 by 10 cm large
case = 20 # we cut it in little square to determine neighborhood of one grain
#idealy one cas must be around the diameter of a grain wide, so the grain can only interact with 8 cases
nbgrain = 200
dt = 0.001 #sec
grainradius = 0.002
kspring = 30 #Newton per meter
gamma = 0.1 # coeffcient for fluid friction
beta = 0.1 # second coeffeicient for friction dehind quadratic member
grainlist = [Grain((rd.uniform(0,0.1),rd.uniform(0,0.1) ),k,(0,0),(0,0),0.001) for k in range(nbgrain)] #list of all grains within the box
walllist = [ Wall([(0,-1),(0,1)],(1,0)) , Wall([(0.1,-1),(0.1,1)],(-1,0)) , Wall([(-1,0),(1,0)],(0,1))]
quadmat = [] #we sort all the grain in a 'quadtree', we divide the box in case*case, we store grain id only



running = True
while running :
    st=time.time()

    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                pass
    quadmat = sortgrain(grainlist,case,box)

    for e in grainlist:

        """force determination"""
        neighcase = neighborhood(e.getij(),case)
        list_interaction = []
        for p in neighcase:
            list_interaction += quadmat[p[1]][p[0]]
        for k in list_interaction:
            e.interaction(grainlist[k],grainradius,kspring)
        for w in walllist:
            e.bounceonwall(w,kspring,grainradius)

        e.forcext(gamma,beta)

        """move"""
        e.move(dt)

        """display"""
        loc = e.getloc()
        pygame.draw.circle(screen,(158,155,83),[5000*loc[0],500-5000*loc[1]],5000*grainradius)

    pygame.draw.line(screen,(120,120,120),(0,500),(500,500))
    pygame.draw.line(screen,(120,120,120),(500,500),(500,0))

    pygame.draw.line(screen,(120,120,120),(0,0),(0,500))


    pygame.display.update()
    #pygame.time.wait(100)


    fps = 1/(time.time()-st+0.0001)
    st=time.time()
    print(fps)
