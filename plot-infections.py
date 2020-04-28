import matplotlib.pyplot as plt
import numpy as np
import sys 

filename= sys.argv[1]

infected= np.loadtxt(filename, skiprows =8, delimiter = ',', usecols=(0,2))
infected_people= infected[:,1]
day= infected[:,0]
log_infected = np.log(infected_people)

<<<<<<< HEAD
<<<<<<< HEAD
plt.plot(day, infected_people, color='black', linestyle='-')
plt.plot(day, log_infected, color='green', linestyle='--')
plt.title("Infection rate of COVID-19 in Idaho") 
=======
dead= np.loadtxt(filename, skiprows =3, delimiter = ',', usecols=(0,4))
=======
dead= np.loadtxt(filename, skiprows =8, delimiter = ',', usecols=(0,4))
>>>>>>> 84ad8cda52493b4752a4b1d284ff34a77a03d040
dead_people= dead[:,1]
day= dead[:,0]

plt.plot(day, dead_people,label='Dead',color='k')
plt.plot(day, infected_people,label='Infected',color='r')
>>>>>>> 6a8ff2e556048c636af14c52b50ac51841563e80
plt.xlabel('Time [days]')
plt.ylabel('Number of People')
plt.grid()
plt.title(filename,loc='center') 
plt.legend(loc='best')
plt.show()

plt.savefig(filename + ".png")
