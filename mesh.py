def meshing(m,n,X,Y):
    import numpy as np
    x = np.linspace(0, X, n)
    y = np.linspace(0, Y, m)
    xx,yy = np.meshgrid(x,y)
    return xx, yy
