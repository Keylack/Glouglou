#Imports
import numpy as np
import time
from mesh import meshing
from Resolution_ratee import Resolution_1
from Graph import Graph_pressure
import matplotlib.pyplot as plt


#Data
ro = 1000
V1 = 3
dt = 1
t = 0
tmax = 2000
nu = 1.31e-6
X = 3
Y = 2
g = 9.81
cd = 0
m = input("Enter number of rows: \n")
n = input("Enter number of columns: \n")
m = int(m)+1
n = int(n)+1

#Coordonnées
dx = X/(n-1)
dy = Y/(m-1)
Limite_dt = nu*dt/(dx*dy)
print(Limite_dt)
CordX = np.zeros((m, n))
CordY = np.zeros((m, n))
CordX, CordY = meshing(m,n,X,Y)

#Init matrices
P = np.ones((m, n))
u = np.zeros((m, n))
v = np.zeros((m, n))
#Calcul
while t <= tmax:
    ut = np.zeros((m, n))
    vt = np.zeros((m, n))
    Resolution(u,v,P,dx,dy,dt,m,n,nu,V1,ut,vt)
    print(v[m-1,:])
    if cd == 0 :
        Graph_pressure(P,CordX,CordY,u,v)
        cd += 5
    else:
        cd -= 1
    t += dt
