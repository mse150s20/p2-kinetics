from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import sys

# the maximum time of virus in days
maxtime = 365
# people in Idaho
N = 1754000 #where did this number come from?
def kinetics(k1, k2, a_0, b_0, c_0):   #Units of k1 
    def abc(t, y):
        ''' System of differential equations: y(t) = [A(t),B(t),C(t)]
            returns:
                A list containing [dA/dt, dB/dt, dC/dt]
        '''
# where A is uninfected, B is infected, C is recovered
        A,B,C = y
        return [-k1*A*B/(A+B+C), k1*A*B/(A+B+C)-k2*B, k2*B]
    return solve_ivp(abc, [0, maxtime], [a_0,b_0,c_0], t_eval=np.arange(0, maxtime, 1),method='Radau')
# Original k1 is 0.1
filename = sys.argv[1]
population_infected = np.loadtxt(filename, skiprows = 3, delimiter = ',', usecols = (2))
time = np.loadtxt(filename, skiprows = 3, delimiter = ',', usecols =(0))
#filename = idaho_infections.csv
#infected = np.loadtxt(filename, skiprows = 3, delimiter = ',', usecols = (2))
solution = kinetics(0.5,0.02, N-1,1,0) #ONE infected person on day0

data='idaho_infections/idaho_infections.csv'
data2=np.delete(data, [0,1], axis=0)
x1=data2[:,0]
y1=data2[:,2]
plt.plot(x1,y1, label='R')
plt.plot(solution.t,solution.y[0],label='A')
plt.plot(solution.t,solution.y[1],label='B',linestyle='dashed')
plt.plot(solution.t,solution.y[2],label='C',linestyle='dotted')

plt.xlabel('Time [days]')
plt.ylabel('Population infected')
plt.grid() 
plt.legend()
plt.show()

