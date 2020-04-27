import matplotlib.pyplot as plt
import numpy as np
import sys 

filename= sys.argv[1]

infected= np.loadtxt(filename, skiprows =3, delimiter = ',', usecols=(0,2))
infected_people= infected[:,1]
day= infected[:,0]

dead= np.loadtxt(filename, skiprows =3, delimiter = ',', usecols=(0,4))
dead_people= dead[:,1]
day= dead[:,0]

plt.plot(day, dead_people,label='Dead',color='k')
plt.plot(day, infected_people,label='Infected',color='r')
plt.xlabel('Time [days]')
plt.ylabel('Number of People')
plt.grid() 
plt.legend(loc='best')
plt.show()
