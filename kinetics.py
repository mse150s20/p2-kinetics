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

solution = kinetics(0.1,0.02,N-1,1,0)
This is a TEST
plt.plot(solution.t,solution.y[0],label='A')
plt.plot(solution.t,solution.y[1],label='B',linestyle='dashed')
plt.plot(solution.t,solution.y[2],label='C',linestyle='dotted')
plt.xlabel('Time [days]')
plt.ylabel('Population')
plt.grid() 
plt.legend()
plt.show()


