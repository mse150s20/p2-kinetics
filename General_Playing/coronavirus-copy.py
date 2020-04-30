# Purpose of this is to reduce the maxtime to get a better look at the graph and figure out what k1 and k2 best match the current data 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import sys

# the maximum time of virus in days
maxtime = 65
pop = 1754000 # Population of Idaho according to U.S. Census
def kinetics(rateInfect, rateRecover, h_0, i_0, r_0):
	#Rates in individuals per day    
    def abc(t, y):
        ''' System of differential equations: y(t) = [H(t),I(t),R(t)]
            returns:
                A list containing [dH/dt, dI/dt, dR/dt]
        '''
        healthy,infected,recovered = y
        return [-rateInfect*healthy*infected/(healthy+infected+recovered), rateInfect*healthy*infected/(healthy+infected+recovered)-rateRecover*infected, rateRecover*infected]
	#The equation for Dead will just be (k3*I) where k3 is the death rate, we will have to add (-k3*I) to the infected part of the graph.
    return solve_ivp(abc, [0, maxtime], [h_0,i_0,r_0], t_eval=np.arange(0, maxtime, 1),method='Radau')
filename = sys.argv[1]

time = np.loadtxt(filename, skiprows = 8, delimiter = ',', usecols = (0))
infected = np.loadtxt(filename, skiprows = 8, delimiter = ',', usecols = (2))
dead = np.loadtxt(filename, skiprows = 8, delimiter = ',', usecols = (4))
recovered = np.loadtxt(filename, skiprows = 8,  delimiter = ',', usecols = (6))
solution = kinetics(0.4,0.2, pop-1,1,0) #ONE infected person on day0

plt.plot(time, dead, label='Real Dead', color = 'k')
plt.plot(time,infected, label='Real Infections')
plt.plot(time,recovered, label='Real Recovered', color = 'm')
#plt.plot(solution.t,solution.y[0],label='Model Healthy')
plt.plot(solution.t,solution.y[1],label='Model Infected',linestyle='dashed')
plt.plot(solution.t,solution.y[2],label='Model Recovered',linestyle='dotted')

plt.xlabel('Time [days]')
plt.ylabel('Population infected')

plt.title('Infection Rate of COVID-19 in Idaho:\nModel VS Data')
plt.grid() 

plt.legend(loc='best')
plt.show()
