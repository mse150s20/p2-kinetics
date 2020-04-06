from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

maxtime = 300
N = 10000
def kinetics(k1, k2, a_0, b_0, c_0):
    def abc(t, y):
        ''' System of differential equations: y(t) = [A(t),B(t),C(t)]
            returns:
                A list containing [dA/dt, dB/dt, dC/dt]
        '''
        A,B,C = y
        return [-k1*A*B/(A+B+C), k1*A*B/(A+B+C)-k2*B, k2*B]
    return solve_ivp(abc, [0, maxtime], [a_0,b_0,c_0], t_eval=np.arange(0, maxtime, 1),method='Radau')

solution = kinetics(0.2,0.04, N-1,1.5,0)

plt.plot(solution.t,solution.y[0]/N,label='A')
plt.plot(solution.t,solution.y[1]/N,label='B',linestyle='dashed')
plt.plot(solution.t,solution.y[2]/N,label='C',linestyle='dotted')
plt.xlabel('time [s]')
plt.ylabel('mole fraction')
plt.grid() 
plt.legend()
plt.show()


