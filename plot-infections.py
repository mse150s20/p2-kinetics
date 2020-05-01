import matplotlib.pyplot as plt
import numpy as np
import sys 

filename= sys.argv[1]

infected = np.loadtxt(filename, skiprows =8, delimiter = ',', usecols=(0,2))
infected_people= infected[:,1]
day= infected[:,0]
plt.title("Infection rate of COVID-19 in Idaho", loc= 'center') 
dead= np.loadtxt(filename, skiprows =8, delimiter = ',', usecols=(0,4))
dead_people= dead[:,1]
day = dead[:,0]

plt.plot(day, dead_people,label='Dead',color='k')
plt.plot(day, infected_people, label='Infected',color='r')
plt.xlabel('Time [days]')
plt.ylabel('Number of People')
plt.grid()
plt.title(filename,loc='center') 
plt.legend(loc='best')
plt.show()

plt.savefig(filename + ".png")



log_infected = np.log(infected_people)
plt.plot(day, log_infected, color='green', linestyle='--', label = 'Logarithm of infected people')
plt.xlabel('Time [days]')
plt.ylabel('log(Number of People)')
plt.grid()
plt.title(filename, loc = 'center')
plt.legend(loc = 'best')
plt.show()
plt.savefig(filename + ".png")

