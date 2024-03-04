import numpy as np
from scipy.stats import expon, norm
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl

#Tiene la misma estructura que el primero, pero no se repiten algunos comentarios
#ya que se asume que se ha entendido el primer script previamente

# Cargar todos los datos del archivo
with open("E2.fallos.txt", 'r') as file:
    fallos_data = file.readlines()

# Convertir los datos a flotantes
fallos_data = [float(fallo.strip()) for fallo in fallos_data]

# Calcular la media y la desviación estándar de los tiempos de fallo
media_fallos = np.mean(fallos_data)
desviacion_std_fallos = np.std(fallos_data)

# Establecer parámetros iniciales
maquinas_operativas = 10
maquinas_reserva = 5
tasa_reparacion_inicial = 0.55  # máquinas/hora
tasa_reparacion_final = 1.65    # máquinas/hora
tiempo_simulacion = 1000         # horas de simulación
tasa_incremento = (tasa_reparacion_final - tasa_reparacion_inicial) / tiempo_simulacion
tiempo_actual = 0
tiempo_suceso = 0

simultaneo = False
tiempo_sim = 0
tiempo_sim_start = 0

tiempo_funcionamiento_sistema = 0
tiempo_funcionamiento_sistema_start = 0

eventos_fallos = []
eventos_reparaciones = []
tiempo_relativo_fallos = []
tiempo_relativo_reparaciones = []

LISTA = {
    "tiempo_llegada_1": -1,
    "tiempo_llegada_2": -1,
    "tiempo_llegada_3": -1,
    "tiempo_llegada_4": -1,
    "tiempo_llegada_5": -1,
    "tiempo_llegada_6": -1,
    "tiempo_llegada_7": -1,
    "tiempo_llegada_8": -1,
    "tiempo_llegada_9": -1,
    "tiempo_llegada_10": -1,
    "tiempo_salida_1": -1,
    "tiempo_salida_2": -1,
    "tiempo_salida_3": -1,
    "tiempo_salida_4": -1
}

num_llegadas = 0
num_salidas_1 = 0
num_salidas_2 = 0
num_salidas_3 = 0
num_salidas_4 = 0
num_clientes = 0
num_clientes_op1 = 0
num_clientes_op2 = 0
num_clientes_op3 = 0
num_clientes_op4 = 0

tiempo_reparacion_op1 = 0
tiempo_reparacion_op2 = 0
tiempo_reparacion_op3 = 0
tiempo_reparacion_op4 = 0

tasa_reparacion = tasa_reparacion_inicial

def reset_values():
    global tiempo_actual, tiempo_suceso, simultaneo, tiempo_sim, tiempo_sim_start, tiempo_funcionamiento_sistema, tiempo_funcionamiento_sistema_start, eventos_fallos
    global eventos_reparaciones, tiempo_relativo_fallos, tiempo_relativo_reparaciones, LISTA, num_llegadas, num_salidas_1, num_salidas_2, num_salidas_3
    global num_clientes, num_clientes_op1, num_clientes_op2, num_clientes_op3, tiempo_reparacion_op1, tiempo_reparacion_op2, tiempo_reparacion_op3, tasa_reparacion
    global maquinas_operativas, maquinas_reserva, num_clientes_op4, tiempo_reparacion_op4
    # Establecer parámetros iniciales
    maquinas_operativas = 10
    maquinas_reserva = 5
    tiempo_actual = 0
    tiempo_suceso = 0

    simultaneo = False
    tiempo_sim = 0
    tiempo_sim_start = 0

    tiempo_funcionamiento_sistema = 0
    tiempo_funcionamiento_sistema_start = 0

    eventos_fallos = []
    eventos_reparaciones = []
    tiempo_relativo_fallos = []
    tiempo_relativo_reparaciones = []

    LISTA = {
        "tiempo_llegada_1": -1,
        "tiempo_llegada_2": -1,
        "tiempo_llegada_3": -1,
        "tiempo_llegada_4": -1,
        "tiempo_llegada_5": -1,
        "tiempo_llegada_6": -1,
        "tiempo_llegada_7": -1,
        "tiempo_llegada_8": -1,
        "tiempo_llegada_9": -1,
        "tiempo_llegada_10": -1,
        "tiempo_salida_1": -1,
        "tiempo_salida_2": -1,
        "tiempo_salida_3": -1,
        "tiempo_salida_4": -1
    }

    num_llegadas = 0
    num_salidas_1 = 0
    num_salidas_2 = 0
    num_salidas_3 = 0
    num_clientes = 0
    num_clientes_op1 = 0
    num_clientes_op2 = 0
    num_clientes_op3 = 0
    num_clientes_op4 = 0

    tiempo_reparacion_op1 = 0
    tiempo_reparacion_op2 = 0
    tiempo_reparacion_op3 = 0
    tiempo_reparacion_op4 = 0

    tasa_reparacion = tasa_reparacion_inicial

# Función para simular el tiempo hasta el próximo fallo
def tiempo_hasta_fallo(media, std):
    return norm.rvs(loc=media, scale=std)

# Función para simular el tiempo hasta reparar una máquina
def tiempo_hasta_reparar(tasa_reparacion):
    return expon.rvs(scale=1/tasa_reparacion)

def rutina_llegada(tsuceso, id):
    global tiempo_actual, media_fallos, desviacion_std_fallos, LISTA, tasa_reparacion, num_clientes, num_llegadas
    global num_clientes_op1, num_clientes_op2, num_clientes_op3, num_clientes_op4, maquinas_operativas, maquinas_reserva, tiempo_reparacion_op1, tiempo_reparacion_op2
    global tiempo_reparacion_op3, tiempo_reparacion_op4, eventos_fallos, tiempo_sim_start,simultaneo
    global tiempo_funcionamiento_sistema_start, tiempo_funcionamiento_sistema
    tiempo_actual = tsuceso
    num_clientes += 1
    num_llegadas += 1
    
    if maquinas_operativas > 0:
        maquinas_operativas -= 1
    
        if maquinas_reserva > 0:
            maquinas_operativas += 1
            maquinas_reserva -= 1
            fallo = tiempo_hasta_fallo(media=media_fallos, std=desviacion_std_fallos)
            tiempo_relativo_fallos.append({
                "nombre": "Fallo " + str(num_llegadas + 1) + " en máquina"+str(id),
                "tiempo_relativo": fallo
            })
            #Asignar siguiente fallo
            if tiempo_actual + fallo < tiempo_simulacion:
                LISTA["tiempo_llegada_"+str(id)] = tiempo_actual + fallo
            else:
                return
            
        if maquinas_operativas == 9:
            #El sistema no está funcionando
            tiempo_funcionamiento_sistema += tsuceso - tiempo_funcionamiento_sistema_start
            pass
    else:
        return
    
    eventos_fallos.append({
        "nombre": "Fallo " + str(num_llegadas),
        "tiempo": tsuceso
    })
        
    #Asignar a uno de 3 operarios
    if num_clientes_op1 == 0 and num_clientes > 0:
        num_clientes_op1 += 1
        num_clientes -= 1
        #Si ambos trabajan a la vez, nos lo apuntamos
        if num_clientes_op2 > 0 and simultaneo == False:
            tiempo_sim_start = tiempo_actual
            simultaneo = True
        reparar = tiempo_hasta_reparar(tasa_reparacion)
        LISTA["tiempo_salida_1"] = tiempo_actual + reparar
        tiempo_relativo_reparaciones.append({
                "nombre": "Rep " + str(num_llegadas + 1) + " en operario 1",
                "tiempo_relativo": reparar
            })
        tiempo_reparacion_op1 += reparar
    if num_clientes_op2 == 0 and num_clientes > 0:
        num_clientes_op2 += 1
        num_clientes -= 1
        #Si ambos trabajan a la vez, nos lo apuntamos
        if num_clientes_op1 > 0 and simultaneo == False:
            tiempo_sim_start = tiempo_actual
            simultaneo = True
        reparar = tiempo_hasta_reparar(tasa_reparacion)
        LISTA["tiempo_salida_2"] = tiempo_actual + reparar
        tiempo_relativo_reparaciones.append({
                "nombre": "Rep " + str(num_llegadas + 1) + " en operario 2",
                "tiempo_relativo": reparar
            })
        tiempo_reparacion_op2 += reparar
    if num_clientes_op3 == 0 and num_clientes > 0:
        num_clientes_op3 += 1
        num_clientes -= 1
        reparar = tiempo_hasta_reparar(tasa_reparacion)
        LISTA["tiempo_salida_3"] = tiempo_actual + reparar
        tiempo_relativo_reparaciones.append({
                "nombre": "Rep " + str(num_llegadas + 1) + " en operario 3",
                "tiempo_relativo": reparar
            })
        tiempo_reparacion_op3 += reparar
        
    if num_clientes_op4 == 0 and num_clientes > 0:
        num_clientes_op4 += 1
        num_clientes -= 1
        reparar = tiempo_hasta_reparar(tasa_reparacion)
        LISTA["tiempo_salida_4"] = tiempo_actual + reparar
        tiempo_relativo_reparaciones.append({
                "nombre": "Rep " + str(num_llegadas + 1) + " en operario 4",
                "tiempo_relativo": reparar
            })
        tiempo_reparacion_op4 += reparar

def rutina_servidor_1(tsuceso):
    global tiempo_actual, media_fallos, desviacion_std_fallos, LISTA, tasa_reparacion, num_clientes, num_salidas_1, num_clientes_op1
    global maquinas_operativas, maquinas_reserva, eventos_reparaciones, num_llegadas, simultaneo, tiempo_sim_start, tiempo_sim
    global tiempo_funcionamiento_sistema_start, tiempo_funcionamiento_sistema
    tiempo_actual = tsuceso
    num_clientes_op1 -= 1
    num_salidas_1 += 1
    
    eventos_reparaciones.append({
        "nombre": "Reparacion " + str(num_salidas_1) + " en el operario 1",
        "tiempo": tsuceso
    })
    
    if maquinas_operativas == 10:
        maquinas_reserva += 1
    else:
        maquinas_operativas += 1
        fallo = tiempo_hasta_fallo(media=media_fallos, std=desviacion_std_fallos)
        #Asignar siguiente fallo
        if tiempo_actual + fallo < tiempo_simulacion:

            for i in range(10):
                if LISTA["tiempo_llegada_"+str(i+1)] == -1:
                    LISTA["tiempo_llegada_"+str(i+1)] = tiempo_actual + fallo
                    tiempo_relativo_fallos.append({
                        "nombre": "Fallo " + str(num_llegadas + 1) + " en máquina"+str(i+1),
                        "tiempo_relativo": fallo
                    })
                    break
                
        if maquinas_operativas == 10:
            #El sistema vuelve a funcionar
            tiempo_funcionamiento_sistema_start = tiempo_actual

    if num_clientes > 0:
        num_clientes_op1 += 1
        num_clientes -= 1
        reparar = tiempo_hasta_reparar(tasa_reparacion)
        LISTA["tiempo_salida_1"] = tiempo_actual + reparar
        tiempo_relativo_reparaciones.append({
                "nombre": "Rep " + str(num_llegadas + 1) + " en el operario 1",
                "tiempo_relativo": reparar
            })
    else:
        if simultaneo:
            tiempo_sim += tiempo_actual - tiempo_sim_start
            simultaneo = False

def rutina_servidor_2(tsuceso):
    global tiempo_actual, media_fallos, desviacion_std_fallos, LISTA, tasa_reparacion, num_clientes, num_salidas_2, num_clientes_op2
    global maquinas_operativas, maquinas_reserva, eventos_reparaciones, tiempo_sim, tiempo_sim_start, simultaneo
    global tiempo_funcionamiento_sistema_start, tiempo_funcionamiento_sistema
    tiempo_actual = tsuceso
    num_clientes_op2 -= 1
    num_salidas_2 += 1
    
    eventos_reparaciones.append({
        "nombre": "Reparacion " + str(num_salidas_2) + " en el operario 2",
        "tiempo": tsuceso
    })
    
    if maquinas_operativas == 10:
        maquinas_reserva += 1
    else:
        maquinas_operativas += 1
        fallo = tiempo_hasta_fallo(media=media_fallos, std=desviacion_std_fallos)
        #Asignar siguiente fallo
        if tiempo_actual + fallo < tiempo_simulacion:

            for i in range(10):
                if LISTA["tiempo_llegada_"+str(i+1)] == -1:
                    LISTA["tiempo_llegada_"+str(i+1)] = tiempo_actual + fallo
                    tiempo_relativo_fallos.append({
                        "nombre": "Fallo " + str(num_llegadas + 1) + " en máquina"+str(i+1),
                        "tiempo_relativo": fallo
                    })
                    break
                
        if maquinas_operativas == 10:
            #El sistema vuelve a funcionar
            tiempo_funcionamiento_sistema_start = tiempo_actual

    if num_clientes > 0:
        num_clientes_op2 += 1
        num_clientes -= 1
        reparar = tiempo_hasta_reparar(tasa_reparacion)
        LISTA["tiempo_salida_2"] = tiempo_actual + reparar
        tiempo_relativo_reparaciones.append({
                "nombre": "Rep " + str(num_llegadas + 1) + " en el operario 2",
                "tiempo_relativo": reparar
            })
    else:
        if simultaneo:
            tiempo_sim += tiempo_actual - tiempo_sim_start
            simultaneo = False

def rutina_servidor_3(tsuceso):
    global tiempo_actual, media_fallos, desviacion_std_fallos, LISTA, tasa_reparacion, num_clientes, num_salidas_3, num_clientes_op3
    global maquinas_operativas, maquinas_reserva, eventos_reparaciones
    global tiempo_funcionamiento_sistema_start, tiempo_funcionamiento_sistema
    tiempo_actual = tsuceso
    num_clientes_op3 -= 1
    num_salidas_3 += 1
    
    eventos_reparaciones.append({
        "nombre": "Reparacion " + str(num_salidas_3) + " en el operario 3",
        "tiempo": tsuceso
    })
    
    if maquinas_operativas == 10:
        maquinas_reserva += 1
    else:
        maquinas_operativas += 1
        fallo = tiempo_hasta_fallo(media=media_fallos, std=desviacion_std_fallos)
        #Asignar siguiente fallo
        if tiempo_actual + fallo < tiempo_simulacion:

            for i in range(10):
                if LISTA["tiempo_llegada_"+str(i+1)] == -1:
                    LISTA["tiempo_llegada_"+str(i+1)] = tiempo_actual + fallo
                    tiempo_relativo_fallos.append({
                        "nombre": "Fallo " + str(num_llegadas + 1) + " en máquina"+str(i+1),
                        "tiempo_relativo": fallo
                    })
                    break
                
        if maquinas_operativas == 10:
            #El sistema vuelve a funcionar
            tiempo_funcionamiento_sistema_start = tiempo_actual

    if num_clientes > 0:
        num_clientes_op3 += 1
        num_clientes -= 1
        reparar = tiempo_hasta_reparar(tasa_reparacion)
        LISTA["tiempo_salida_3"] = tiempo_actual + reparar
        tiempo_relativo_reparaciones.append({
                "nombre": "Rep " + str(num_llegadas + 1) + " en el operario 3",
                "tiempo_relativo": reparar
            })
        
def rutina_servidor_4(tsuceso):
    global tiempo_actual, media_fallos, desviacion_std_fallos, LISTA, tasa_reparacion, num_clientes, num_salidas_4, num_clientes_op4
    global maquinas_operativas, maquinas_reserva, eventos_reparaciones
    global tiempo_funcionamiento_sistema_start, tiempo_funcionamiento_sistema
    tiempo_actual = tsuceso
    num_clientes_op4 -= 1
    num_salidas_4 += 1
    
    eventos_reparaciones.append({
        "nombre": "Reparacion " + str(num_salidas_4) + " en el operario 4",
        "tiempo": tsuceso
    })
    
    if maquinas_operativas == 10:
        maquinas_reserva += 1
    else:
        maquinas_operativas += 1
        fallo = tiempo_hasta_fallo(media=media_fallos, std=desviacion_std_fallos)
        #Asignar siguiente fallo
        if tiempo_actual + fallo < tiempo_simulacion:

            for i in range(10):
                if LISTA["tiempo_llegada_"+str(i+1)] == -1:
                    LISTA["tiempo_llegada_"+str(i+1)] = tiempo_actual + fallo
                    tiempo_relativo_fallos.append({
                        "nombre": "Fallo " + str(num_llegadas + 1) + " en máquina"+str(i+1),
                        "tiempo_relativo": fallo
                    })
                    break
                
        if maquinas_operativas == 10:
            #El sistema vuelve a funcionar
            tiempo_funcionamiento_sistema_start = tiempo_actual

    if num_clientes > 0:
        num_clientes_op4 += 1
        num_clientes -= 1
        reparar = tiempo_hasta_reparar(tasa_reparacion)
        LISTA["tiempo_salida_4"] = tiempo_actual + reparar
        tiempo_relativo_reparaciones.append({
                "nombre": "Rep " + str(num_llegadas + 1) + " en el operario 4",
                "tiempo_relativo": reparar
            })
        
def start_sim():
    
    global tasa_reparacion
    reset_values()
    
    #Se calcula el primer fallo del sistema
    primeros_fallos = []
    for i in range(10):
        primer_fallo = tiempo_hasta_fallo(media=media_fallos, std=desviacion_std_fallos)
        primeros_fallos.append(primer_fallo)
        tiempo_relativo_fallos.append({
                "nombre": "Fallo " + str(i+1),
                "tiempo_relativo": primer_fallo
            })

    primeros_fallos.sort()
    primer_fallo = primeros_fallos[0]

    i = 1
    for fallo in primeros_fallos:
        LISTA["tiempo_llegada_"+str(i)] = fallo
        i+=1

    if (tiempo_actual + primer_fallo) > tiempo_simulacion:
        #Variables a 0 y terminar programa
        exit(-1)
    else:
        rutina_llegada(primer_fallo, 1)
        pass

    while any(value != -1 for value in LISTA.values()):
        numeros_filtrados = {k: v for k, v in LISTA.items() if v != -1}
        clave_menor = min(numeros_filtrados, key=numeros_filtrados.get)
        
        #Se ejecuta la función específica para el suceso más cercano
        if "tiempo_llegada" in clave_menor:
            tiempo_suceso = LISTA[clave_menor]
            LISTA[clave_menor] = -1
            rutina_llegada(tiempo_suceso, int(clave_menor[-1]))
        elif clave_menor == "tiempo_salida_1":
            tiempo_suceso = LISTA["tiempo_salida_1"]
            LISTA["tiempo_salida_1"] = -1
            rutina_servidor_1(tiempo_suceso)
        elif clave_menor == "tiempo_salida_2":
            tiempo_suceso = LISTA["tiempo_salida_2"]
            LISTA["tiempo_salida_2"] = -1
            rutina_servidor_2(tiempo_suceso)
        elif clave_menor == "tiempo_salida_3":
            tiempo_suceso = LISTA["tiempo_salida_3"]
            LISTA["tiempo_salida_3"] = -1
            rutina_servidor_3(tiempo_suceso)
        elif clave_menor == "tiempo_salida_4":
            tiempo_suceso = LISTA["tiempo_salida_4"]
            LISTA["tiempo_salida_4"] = -1
            rutina_servidor_4(tiempo_suceso)
        
        tasa_reparacion += tasa_incremento

    print("Tiempo simultáneo de los tres operarios: " + str(tiempo_sim))
    print("Tiempo funionamiento del sistema: " + str(tiempo_funcionamiento_sistema))
    
    return tiempo_sim, tiempo_funcionamiento_sistema

#Para crear los histogramas
def print_histogram():
    tiempos = [fallo["tiempo"] for fallo in eventos_fallos]
    plt.hist(tiempos, bins=100, edgecolor='black', cumulative=True)
    
    plt.xlabel('Tiempo')
    plt.ylabel('Cantidad de fallos')
    plt.title('Histograma de tiempos de fallos en el sistema')
    
    plt.show()

def print_excel():
    global eventos_fallos, eventos_reparaciones, tiempo_relativo_fallos, tiempo_relativo_reparaciones
    tiempo_relativo_fallos.pop()
    combined_df = pd.DataFrame(columns=['Nombre Fallo', 'Tiempo Fallo', 'Nombre Reparacion', 'Tiempo Reparacion'])
    combined2_df = pd.DataFrame(columns=['Nombre relativo Fallos', 'Tiempo relativo Fallos', 'Nombre relativo Reparacion', 'Tiempo relativo Reparacion'])

    # Populate the columns with Fallos and Reparaciones data
    combined_df['Nombre Fallo'] = [f['nombre'] for f in eventos_fallos]
    combined_df['Tiempo Fallo'] = [f['tiempo'] for f in eventos_fallos]
    combined_df['Nombre Reparacion'] =[r['nombre'] for r in eventos_reparaciones]
    combined_df['Tiempo Reparacion'] =[r['tiempo'] for r in eventos_reparaciones]
    
    combined2_df['Nombre relativo Fallos'] =[r['nombre'] for r in tiempo_relativo_fallos]
    combined2_df['Tiempo relativo Fallos'] =[r['tiempo_relativo'] for r in tiempo_relativo_fallos]
    combined2_df['Nombre relativo Reparacion'] =[r['nombre'] for r in tiempo_relativo_reparaciones]
    combined2_df['Tiempo relativo Reparacion'] =[r['tiempo_relativo'] for r in tiempo_relativo_reparaciones]

    combined_df.to_excel("excel/maintenance_data_combined.xlsx", index=False)
    combined2_df.to_excel("excel/maintenance_data_combined2.xlsx", index=False)