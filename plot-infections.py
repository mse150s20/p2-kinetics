import matplotlib.pyplot as plt
import numpy as np

filename= sys.argv[1]

infected= np.loadtxt(filename, skiprows =3, delimiter = ',')
infection_rates= infected[:2]

plt.plot(solution.t,solution.y[0],label='Uninfected')
plt.plot(solution.t,solution.y[1],label='Infected',linestyle='dashed')
plt.xlabel('Time [days]')
plt.ylabel('Population infected')
plt.grid() 
plt.legend()
plt.show()


