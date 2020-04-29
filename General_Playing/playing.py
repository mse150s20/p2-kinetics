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
num=5
k1s=np.linspace(1,2,num)
k2s=np.linspace(1,2,num)
plot_array=np.empty((num,num))

with open("maxday_vs_k1k2.txt","w") as f:  #copies to maxday_vs_k1k2.txt file
    for i,k1 in enumerate(k1s):
        for j,k2 in enumerate(k2s):
            solution=kinetics(k1,k2,N-1,1,0)
            B=solution.y[1]
            max_B_ind= np.argmax(B)
            max_day= solution.t[max_B_ind]
	
            plot_array[i][j]=max_day
            f.write("{},{},{}\n".format(k1,k2,max_day))

#k1 is infection rate, k2 is recovery rate, prints amount of time in  days until infected is at the maximum

plt.pcolormesh(plot_array)
plt.colorbar()
plt.ylabel("Infection Rate (k1)")
plt.xlabel("Recovery Rate (k2)")
pos = [i+0.5 for i in range(num)]
k1_y = ["{:.2f}".format(k1) for k1 in k1s]#Formats as a string
k2_x = ["{:.2f}".format(k2) for k2 in k2s]
plt.xticks(pos, k2_x)#putting the tick marks halfway between the values
plt.yticks(pos, k1_y)

plt.show()
