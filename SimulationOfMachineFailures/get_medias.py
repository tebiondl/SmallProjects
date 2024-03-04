from Sim import start_sim
import numpy as np

total_simulacion = []
total_simultaneo = []
for i in range(100):
    t_simul, t_sim = start_sim()
    total_simulacion.append(t_sim)
    total_simultaneo.append(t_simul)
    
media_sim = np.mean(total_simulacion)
media_simul = np.mean(total_simultaneo)

desv_sim  = np.std(total_simulacion)
desv_simul = np.std(total_simultaneo)

print(media_sim)
print(media_simul)
print(desv_sim)
print(desv_simul)