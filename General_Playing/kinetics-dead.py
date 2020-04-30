# For simulating deaths in addition to infected and recovered
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# the maximum time of virus in days
maxtime = 65
# people in Idaho
N = 1754000
def kinetics(rateInfect, rateRecover, rateDie, a_0, b_0, c_0, d_0):
    def abc(t, y):
        ''' System of differential equations: y(t) = [A(t),B(t),C(t)]
            returns:
                A list containing [dA/dt, dB/dt, dC/dt]
        '''
# where A is uninfected, B is infected, C is recovered, and D is dead
        healthy,infected,C,D = y
        return [-rateInfect*healthy*infected/(healthy+infected+C+D), rateInfect*healthy*infected/(healthy+infected+C+D)-rateRecover*infected-rateDie*infected, rateRecover*infected, rateDie*infected]
    return solve_ivp(abc, [0, maxtime], [a_0,b_0,c_0,d_0], t_eval=np.arange(0, maxtime, 1),method='Radau')

solution = kinetics(0.139,0.02,0.003167, N-1,1,0,0) # The numbers are 56 dead over 1768 infected currently as of 04-26-20 if there is a findings team member who has the actual death rate, go ahead and change it. Infection rate from www.worldometers.info/coronavirus.


#plt.plot(solution.t,solution.y[0],label='Uninfected')
plt.plot(solution.t,solution.y[1],label='Infected',linestyle='dashed')
plt.plot(solution.t,solution.y[2],label='Recovered',linestyle='dotted')
plt.plot(solution.t,solution.y[3],label='Dead',linestyle= '-.',color='Black')
plt.xlabel('Time [days]')
plt.ylabel('Population infected')
plt.grid() 
plt.legend()
plt.show()
plt.title('States of Covid-19 in the Public')

