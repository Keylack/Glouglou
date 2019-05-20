def Graph_pressure(P, CordX, CordY, u, v):
    import numpy as np
    import matplotlib.pyplot as plt
    plt.ion()
    plt.figure(1)
    plt.clf()
    plt.subplot(211)
    plt.contourf(CordX, CordY, P, cmap=plt.cm.bone)
    plt.colorbar()
    plt.subplot(212)
    plt.quiver(CordX, CordY, u, -v, scale =5, scale_units='inches')
    plt.draw()
    plt.pause(0.001)
