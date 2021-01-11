import numpy as np
import numpy.random as rnd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

t1, It = np.loadtxt('radiation.txt', skiprows=2, unpack=True)
t, Ib = np.loadtxt('background.txt', skiprows=2, unpack=True)

I = It-np.mean(Ib)  # subtract the average background radiation from decay radiation
sI = np.sqrt(I+np.mean(Ib))  # uncertainty for decay radiation

z = np.log(I)  # Change to make a linear regression
sz = sI/np.abs(I)  # uncertainty in geiger counter


def zfit(t, a, b):
    return a*t+b


popt, pcov = curve_fit(zfit, t, z, sigma=sz)
plt.errorbar(t, z, yerr= sz, label='Experimental Data')
# this plot the log of experimental data bs count number

plt.plot(t, zfit(t, *popt), label='Line of Best Fit')
# this plot the line of best fit

plt.xlabel('Sample Number')
plt.ylabel('log(count number)')
plt.title('Radioactive Decay of Barium Plotted With Linear Regression')
plt.legend()
plt.show()


p = popt
dp = np.sqrt([pcov[0, 0], pcov[1, 1]])  # change covariance to standard deviation

dt = (20*60)/len(t)
T = (-1/p[0])*dt*np.log(2)  # decay half life from the form: I=I0*(1/2)^(t/t_half)
sT = abs(T)*dp[0]/abs(p[0])  # uncertainty for half life

print('The half life for Barium decay is {} =/- {} minutes'.format(T/60.0, sT/60))
# The half life for Barium decay is 2.6669022993546276 =/- 0.020132529153895903 minutes



