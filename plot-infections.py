import matplotlib.pyplot as plt
import numpy as np
import sys 

filename= sys.argv[1]

infected= np.loadtxt(filename, skiprows =2, delimiter = ',', usecols=(0,2))
infected_people= infected[:,1]
day= infected[:,0]

plt.plot(day, infected_people)
plt.xlabel('Time [days]')
plt.ylabel('Population infected')
plt.yscale('log')
plt.grid() 
plt.legend(['Infected People'], loc='best')
plt.show()
