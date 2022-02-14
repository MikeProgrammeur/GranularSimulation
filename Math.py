def normalize(U):
    "return the vector U normalized if not equal to 0 , else return (0,0)"
    no = (U[0]**2 + U[1]**2)**.5
    if no==1:
        return U
    elif no!=0:
        return prodscve(1/no,U)
    else:
        return (0,0)

def add_vv(u,v):
    "add two vector from R3"
    return (u[0]+v[0],u[1]+v[1])

def dist(A,B):
    "distance between A and B"
    return ((A[0]-B[0])**2 + (A[1]-B[1])**2)**.5
    
def norm(U):
    return ( (U[0])**2 + (U[1])**2 )**.5

def dotprod(U,V):
    "dot product on R2"
    return U[0]*V[0] + U[1]*V[1]

def prodscve(l,U):
    "return U multiplied by the scalar l"
    return ( l*U[0], l*U[1])

def dotovect(A,B):
    "vector from A to B"
    return (B[0]-A[0],B[1]-A[1])
