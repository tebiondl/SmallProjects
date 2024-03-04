import matplotlib.pyplot as plt

# Datos simul
etiquetas2 = ['3 Op / 4 Res', '4 Op / 4 Res', '3 Op / 5 Res', '4 Op / 5 Res']
alturas2 = [232.3469318725473, 261.73320046618994, 235.8841188495845, 263.50677068387756]
desvs2 = [11.680187067852344,7.256518757238733,10.052165463866922,7.135420491370501]

# Datos sim
etiquetas1 = ['3 Op / 4 Res', '4 Op / 4 Res', '3 Op / 5 Res', '4 Op / 5 Res']
alturas1 = [877.4334833264375, 924.1854052874967, 880.4338733926302, 935.8829859659253]
desvs1 = [12.210898005137468,34.55459943313512,66.18738775525001,68.5864805192812]

# Crear la gráfica de barras
# Configuración de la primera gráfica de barras
plt.subplot(1, 2, 1)
plt.bar(etiquetas1, alturas1, color='blue', yerr=desvs1, capsize=5, ecolor='black', alpha=0.7)
plt.xlabel('Etiquetas')
plt.ylabel('Tiempo')
plt.title('Tiempo de Funcionamiento del Sistema')

# Configuración de la segunda gráfica de barras
plt.subplot(1, 2, 2)
plt.bar(etiquetas2, alturas2, color='green', yerr=desvs2, capsize=5, ecolor='black', alpha=0.7)
plt.xlabel('Etiquetas')
plt.ylabel('Tiempo')
plt.title('Tiempo de Operarios Simultáneos')

# Ajustar el diseño para evitar superposiciones
plt.tight_layout()

# Mostrar las gráficas
plt.show()

