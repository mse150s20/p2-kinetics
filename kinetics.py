from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import sys

# the maximum time of virus in days
maxtime = 365
pop = 1754000 # Population of Idaho according to U.S. Census
def kinetics(rateInfect, rateRecover, h_0, i_0, r_0):
	#Rates in individuals per day    
	#rateInfect = the rate at which healthy people contract the virus.
	#rateInfect units = people/day    
	#rateRecover = the rate at which infected people recover from the virus.
	#rateRecover units = people/day
    def abc(t, y):
        ''' System of differential equations: y(t) = [Healthy(t),Infected(t),Recovered(t)]
            returns:
                A list containing [dHealthy/dt, dInfected/dt, dRecovered/dt]
        '''
# where A is uninfected, B is infected, C is recovered
        A,B,C = y
        return [-k1*A*B/(A+B+C), k1*A*B/(A+B+C)-k2*B, k2*B] 
    return solve_ivp(abc, [0, maxtime], [a_0,b_0,c_0], t_eval=np.arange(0, maxtime, 1),method='Radau')
# Original k1 is 0.1
filename = sys.argv[1]
#population_infected = np.loadtxt(filename, skiprows = 3, delimiter = ',', usecols = (2))
        healthy,infected,recovered = y
        return [-rateInfect*healthy*infected/(healthy+infected+recovered), rateInfect*healthy*infected/(healthy+infected+recovered)-rateRecover*infected, rateRecover*infected]
	#The equation for Dead will just be (k3*I) where k3 is the death rate, we will have to add (-k3*I) to the infected part of the graph.
    return solve_ivp(abc, [0, maxtime], [h_0,i_0,r_0], t_eval=np.arange(0, maxtime, 1),method='Radau')
filename = sys.argv[1]

time = np.loadtxt(filename, skiprows = 8, delimiter = ',', usecols = (0))
infected = np.loadtxt(filename, skiprows = 8, delimiter = ',', usecols = (2))
dead = np.loadtxt(filename, skiprows = 8, delimiter = ',', usecols = (4))
#filename = idaho_infections.csv
recovered = np.loadtxt(filename, skiprows = 8,  delimiter = ',', usecols = (6))
solution = kinetics(0.3,0.04, pop-1,1,0) #ONE infected person on day0

plt.plot(time, dead, label='Real Dead', color = 'k')
plt.plot(time,infected, label='Real Infections')
plt.plot(time,recovered, label='Real Recovered', color = 'm')
plt.xlabel('Time [days]')
plt.ylabel('Population infected')
plt.title('Real Infection Rate of COVID-19 in Idaho:\nGiven Data')
plt.grid()
plt.legend(loc='best')
plt.show()

plt.savefig('Real_Data.png')

#Break between graphs

plt.plot(time, dead, label='Real Dead', color = 'k')
plt.plot(time,infected, label='Real Infections')
plt.plot(time,recovered, label='Real Recovered', color = 'm')
plt.xlabel('Time [days]')
plt.ylabel('Population infected [log scale]')
plt.yscale('log')
plt.title('Logarithmic Scale of Real Infection Rate of COVID-19 in Idaho:\nGiven Data')
plt.grid()
plt.legend(loc='best')
plt.show()

plt.savefig('Log_Real_Data.png')

