import numpy as np

#Funcion que retorna N numeros aleatorios con una probabilidad asociada
def sample_1(N):
    a = np.array([-10,-5,3,9])
    b = np.random.choice(a, N, p = [0.1, 0.4, 0.2, 0.3])
    return b

#Funcion que retorna N numeros aleatorios siguiendo la distribucion exponnecial de probablidiad 
def sample_2(N):
    b = np.random.exponential(scale=0.5, size=N)
    return b

#Funcion que retorna una list de M promedios utilizando un funcion de las escritas anterormente 
def get_mean(sampling_fun,N,M):
    lista_prom =[] 
    #Este ciclo recorre M veces la creacion del promedio 
    for i in range(M):
        mean = np.mean(sampling_fun(N))
        lista_prom.append(mean)
    return lista_prom 
    

M = 10000
funciones = [sample_1,sample_2]
nombres = ["sample_1", "sample_2"]
n = [10,100,1000]
#Este ciclo genera un archivo txt para cada nombre de funcion sample y N 
for i in range(len(funciones)):
    for j in range(len(funciones)):
        promedio = get_mean(funciones[i],n[j],M)
        nombre = nombres[i] + "_" + str(n[j]) + ".txt"
        np.savetxt(nombre, promedio)
