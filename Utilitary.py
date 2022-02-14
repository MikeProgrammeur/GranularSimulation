from Math import *


def halfspring(delta,k):
    if delta>=0 :
        return 0
    else :
        return -k*delta

def friction(speed,g,b):
    v = norm(speed)
    return add_vv(prodscve(-g,speed),prodscve(-b*(v**2),speed))




def sortgrain(listgrain,case,box):
    mat = [ [ [] for i in range(case) ] for j in range(case) ]
    for e in listgrain :
        loc = e.getloc()
        pos = (int(loc[0]*case/box[0]) , int(loc[1]*case/box[1]))
        e.setij(pos)
        ide  = e.getid()
        if 0<=pos[0] and pos[0]<=case-1 and 0<=pos[1] and pos[1]<=case-1 :
            mat[pos[1]][pos[0]].append(ide)
    return mat


def neighborhood(pos,case):#pos is (i,j)
    "return the list of all the neighbor of a case"
    l = []
    v = [(0,0),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    b = [add_vv(e,pos) for e in v ]
    for e in b:
        if 0<=e[0] and e[0]<=case-1 and 0<=e[1] and e[1]<=case-1 :
            l.append(e)
    return l
