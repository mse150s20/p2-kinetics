from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# the maximum time of virus in days
maxtime = 365
# people in Idaho
N = 1754000
def kinetics(k1, k2, a_0, b_0, c_0):
    def abc(t, y):
        ''' System of differential equations: y(t) = [A(t),B(t),C(t)]
            returns:
                A list containing [dA/dt, dB/dt, dC/dt]
        '''
        A,B,C = y
        return [-k1*A*B/(A+B+C), k1*A*B/(A+B+C)-k2*B, k2*B]
    return solve_ivp(abc, [0, maxtime], [a_0,b_0,c_0], t_eval=np.arange(0, maxtime, 1),method='Radau')

solution = kinetics(0.07,0.02, N-1000,1000,0) #ONE infected person on day0

#Code will evaluate k1 (infection rate) and k2 (recovery rate) values from 0 to 1, finding the index of the max value of B, this will then copy the code to a text file which is separated commas.

k1s=np.linspace(0,1,10)
k2s=np.linspace(0,1,10)
with open("maxday_vs_k1k2.txt","w") as f:

    for k1 in k1s:
        for k2 in k2s:
            solution=kinetics(k1,k2,N-1,1,0)
            B=solution.y[1]
            max_B_ind= np.argmax(B)
            max_day= solution.t[max_B_ind]
            f.write("{},{},{}\n".format(k1,k2,max_day))

#k1 is infection rate, k2 is recovery rate, prints amount of time in  days until infected is at the maximum

#plt.plot(solution.t,solution.y[0],label='Uninfected')
#plt.plot(solution.t,solution.y[1],label='Infected',linestyle='dashed')
#plt.plot(solution.t,solution.y[2],label='Recovered',linestyle='dotted')
#plt.xlabel('Time [days]')
#plt.ylabel('Population infected')
#plt.grid() 
#plt.legend()
#plt.show()


