import matplotlib.pyplot as plt
import numpy as np
import sys 

filename= sys.argv[1]

infected= np.loadtxt(filename, skiprows =2, delimiter = ',', usecols=(0,2))
infected_people= infected[:,1]
day= infected[:,0]

plt.plot(day, infected_people)
plt.title("Infection rate of COVID-19 in Idaho") 
plt.xlabel('Time [days]')
plt.ylabel('Population infected')
plt.grid() 
plt.legend()
plt.show()


