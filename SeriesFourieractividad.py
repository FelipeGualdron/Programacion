#Series de Fourier
#Se importan las librerias necesarias

import numpy as np
import matplotlib.pylab as plt
from scipy import signal as sp
# Importamos todo el modulo sympy
from sympy import *
# Importamos las variables simbolicas 'n' y 't'
from sympy.abc import n, t

#Definición de variables 

# Definición del periodo
T = 2*pi
# Definición de la frecuencia angular
w = (2*pi)/T
#Definición de la amplitud
A = 1
time = np.arange(-3, 3, 0.001)
#Definición del desfase
Df= np.pi/2
#Funcion por partes
squareWaveFunction = (sp.square(time + Df) ) + 0.01

#Graficación de la onda cuadrada 

plt.plot(time, squareWaveFunction, lw=2)
plt.grid()
plt.annotate('T', xy = (np.pi, 0), xytext = (np.pi, -0.01))
plt.annotate('T/2', xy = (np.pi / 2.0, 0), xytext = (np.pi / 1.2, -0.9))
plt.annotate('T/4', xy = (np.pi / 2.0, 0), xytext = (np.pi / 1.9, -0.9))
plt.annotate('-T/2', xy = (np.pi / -2, 0), xytext = (np.pi / -1.0, -0.9))
plt.annotate('-T/4', xy = (np.pi / -2, 0), xytext = (np.pi / -2.1, -0.9))
plt.ylabel('Amplitude')
plt.xlabel('time(t)')
plt.show()