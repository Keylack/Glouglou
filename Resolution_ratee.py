def Resolution_1(u,v,P,dx,dy,dt,m,n,nu,V1,ut,vt):
    beta = 1.2
#Obtention vitesse 'temporaire'
    for i in range (0,m-1):
        for j in range (0,n-1):
            if i > 0 and i < m-1 and j > 0 and j < n-1: #Cas général
                ut[i,j] = u[i,j] + dt*(-(((0.5*(u[i,j+1]+u[i,j]))**2-(0.5*(u[i,j]+u[i,j-1]))**2)*dy)-\
                    0.25*((u[i,j]+u[i+1,j])*(v[i+1,j]+v[i+1,j+1])-(u[i,j]+u[i-1,j])*(v[i,j]+v[i,j+1]))*dx+\
                    nu*((u[i,j+1]+u[i,j-1]-2*u[i,j])*dy/dx+(u[i-1,j]+u[i+1,j]-2*u[i,j])*dx/dy))

                vt[i,j] = v[i,j] + dt*(-((0.5*(v[i-1,j]+v[i,j]))**2-((0.5*(v[i,j]+v[i+1,j]))**2))*dx-\
                    0.25*(-(v[i,j]+v[i,j+1])*(u[i,j]+u[i-1,j])*dy+(v[i,j]+v[i,j-1])*(u[i,j-1]+u[i-1,j-1])*dy)+\
                    nu*((v[i,j+1]+v[i,j-1]-2*v[i,j])*dy/dx+(v[i+1,j]+v[i-1,j]-2*v[i,j])*dx/dy))

            if i == 0 and j != 0 and j != n-1: #Paroi inférieure
                u[i,j] = 0
                vt[i,j] = -vt[i+1,j]

            if i == m-1 and j != 0 and j != n-1: #Paroi supérieure
                u[i,j] = 0
                vt[i,j] = v[i,j] + dt*(-((0.5*(v[i-1,j]+v[i,j]))**2)*dx-\
                0.25*((v[i,j]+v[i,j+1])*(u[i,j]+u[i-1,j])*dy-(v[i,j]+v[i,j-1])*(u[i,j-1]+u[i-1,j-1])*dy)+\
                nu*((v[i,j+1]+v[i,j-1]-2*v[i,j])*dy/dx+(v[i-1,j]-v[i,j])*dx/dy))

            if j == 0 and i != m-1 and i != 0: #Entrée
                u[i,j] = V1

            if j == n-1 and i != m-1 and i != 0: #Sortie
                ut[i,j] = ut[i,j-1]
                vt[i,j] = v[i,j] + dt*(-((0.5*(v[i+1,j]+v[i,j]))**2-((0.5*(v[i,j]+v[i-1,j]))**2))*dx-\
                0.25*((v[i,j]+v[i,j+1])*(u[i,j]+u[i-1,j])*dy-(v[i,j]+v[i,j-1])*(u[i,j-1]+u[i-1,j-1])*dy)+\
                nu*((v[i,j-1]+v[i,j-1]-2*v[i,j])*dy/dx+(v[i+1,j]+v[i-1,j]-2*v[i,j])*dx/dy))


#Calcul pression

    for i in range (0,m-1):
        for j in range (0,n-1):
            if i != 0 and i != m-1 and j != 0 and j != m-1:
                P[i,j] = 0.5/(1/dx+1/dy)*beta*(1/dx*(P[i,j+1]+P[i,j-1])+1/dy*(P[i-1,j]+P[i+1,j])-1/dt*(ut[i,j]-ut[i,j-1]+vt[i,j]-vt[i+1,j])) + (1-beta)*P[i,j]

            if i == 0 and j != 0 and j != n-1:
                P[i,j] = 1/(2/dx+1/dy)*beta*(1/dx*(P[i,j+1]+P[i,j-1])+1/dy*(P[i+1,j])-1/dt*(ut[i,j]-ut[i,j-1]-vt[i+1,j])) + (1-beta)*P[i,j]

            if i == m-1 and j != 0 and j != n-1:
                P[i,j] = 1/(2/dx+1/dy)*beta*(1/dx*(P[i,j+1]+P[i,j-1])+1/dy*(P[i-1,j])-1/dt*(ut[i,j]-ut[i,j-1]+vt[i,j])) + (1-beta)*P[i,j]

            if j == n-1 and i != 0 and i != m-1:
                P[i,j] = 1/(1/dx+2/dy)*beta*(1/dx*(P[i,j-1])+1/dy*(P[i-1,j]+P[i+1,j])-1/dt*(-ut[i,j-1]+vt[i,j]-vt[i+1,j])) + (1-beta)*P[i,j]

            if i == 0 and j == n-1:
                P[i,j] = 1/(1/dx+1/dy)*beta*(1/dx*(P[i,j-1])+1/dy*(P[i-1,j])-1/dt*(-ut[i,j-1]-vt[i+1,j])) + (1-beta)*P[i,j]

            if i == m-1 and j == n-1:
                P[i,j] = 1/(1/dx+1/dy)*beta*(1/dx*(P[i,j-1])+1/dy*(P[i-1,j])-1/dt*(ut[i,j-1]+vt[i,j])) + (1-beta)*P[i,j]


    for i  in range (0, m-2):
        for j in range (0,n-1):
            u[i,j] = ut[i,j] - dt*(P[i,j+1]-P[i,j])

    for i  in range (1, m-1):
        for j in range (0,n-1):
            v[i,j] = vt[i,j] - dt*(P[i-1,j]-P[i,j])
