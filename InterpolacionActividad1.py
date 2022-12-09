# Se importan las librerias necesarias y se les asigna un alias, numpy para los cálculos
# sympy para el algebra del polinomio y matplotlib.pyplot para las gráficas
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Ingresamos los datos de Δβ
Δβ = np.array([20, 40, 60, 80])
# Ingresamos los datos del porcentaje de rectitud ΔCy
sΔCy = np.array([0.0000001, 0.0000004, 0.0000027, 0.00001])

# Número de elementos de xi 
n = len(Δβ)

# Se le asigna el caracter X
x = sym.Symbol('x')

# Se iguala el polinomio en 0
pol= 0

for i in range(0,n,1):
    # Se calcula el primer termino de lagrange 
    num = 1
    den = 1
    # Se recorre todos los puntos del vector Δβ para el numerador
    for j in range(0,n,1):
        if (i != j):
            num= num*(x-Δβ[j])
            den = den*(Δβ[i]-Δβ[j])
        # Calculo de los terminos de lagrange
        tl = (num/den)*ΔCy[i]
    # Sumador de terminos
    pol = pol + tl
    
# Simplificación de la ecuación
polsimple = sym.expand(pol)

# Forma lamda del polinomio px, referencia x y el polinomio que se desea convertir
px = sym.lambdify(x, pol)

# Vectores para graficas
muestras = 100 # Numero cualquiera
a = np.min(Δβ)
b = np.max(Δβ)
p_Δβ = np.linspace(a,b,muestras)
pΔCy = px(p_Δβ)
p55 = px(55)

# Se imprimen los valores
print('polinomio')
print(pol)
print(' ')
print('polinomio simplificado')
print(polsimple)

# Se grafica
plt.plot(Δβ,ΔCy, 'o')
plt.plot(p_Δβ,pΔCy)
plt.plot(55,p55,  '*' )
plt.show()
