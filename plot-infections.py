import matplotlib.pyplot as plt
import numpy as np
import sys 

filename= sys.argv[1]

infected= np.loadtxt(filename, skiprows =2, delimiter = ',', usecols= (2))
infection_rates= infected[:3]
day= [0]

plt.plot(day, infection_rates)
plt.xlabel('Time [days]')
plt.ylabel('Population infected')
plt.grid() 
plt.legend()
plt.show()


