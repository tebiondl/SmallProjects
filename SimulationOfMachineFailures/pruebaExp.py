import numpy
import matplotlib.pyplot as plt
from scipy.stats import expon

values = numpy.random.exponential(scale=1, size=1000)
values2 = numpy.zeros(1000)
for i in range(1000): 
    values2[i] = expon.rvs(scale=8)

plt.figure(figsize=(10, 6))
plt.plot(values, label='Tiempo de reparación')
plt.xlabel('Iteración')
plt.ylabel('Tiempo (en horas)')
plt.title('Tiempos de reparación siguiendo una distribución exponencial')
plt.legend()
plt.show()